# -*- coding: utf-8 -*-

"""Classes for CloudFrontDistribution (CDN)."""

import uuid


class DistributionManager:
    """Manage the CloudFront Distribution."""

    def __init__(self, session):
        """Create a distribution_manager object."""
        self.session = session
        self.client = self.session.client('cloudfront')

    def find_matching_dist(self, domain_name):
        """Find a dist matching domain_name."""
        paginator = self.client.get_paginator('list_distributions')
        for page in paginator.paginate():
            for dist in page['DistributionList']['Items']:
                for alias in dist['Aliases']['Items']:
                    if alias == domain_name:
                        return dist

        return None

    def create_dist(self, domain_name, cert):
        """Create a dist for domain_name using cert."""
        origin_id = 'S3-' + domain_name
        ressult = self.client.create_distribution(
            DistributionConfig={
                'CallerReference': str(uuid.uuid4()),
                'Aliases': {
                    'Quantity': 1,
                    'Items': [domain_name]
                },
                'DefaultRootObject': 'index.html',
                'Comment': 'Created by webotron',
                'Enabled': True,
                'Origins': {
                    'Quantity': 1,
                    'Items': [{
                        'Id': origin_id,
                        'DomainName':
                            '{}.s3.amazonaws.com'.format(domain_name),
                        'S3OriginConfig': {'OriginAccessIdentity': ''}
                    }]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': origin_id,
                    'ViewerProtocolPolicy': 'redirect-to-https',
                    'TrustedSigners': {
                        'Enabled': False,
                        'Quantity': 0
                    },
                    'ForwardedValues': {
                        'QueryString': False,
                        'Cookies': {
                            'Forward': 'all'
                        },
                        'Headers': {
                            'Quantity': 0
                        },
                        'QueryStringCacheKeys': {
                            'Quantity': 0
                        }
                    },
                    'DefaultTTL': 86400,
                    'MinTTL': 3600
                },
                'ViewerCertificate': {
                    'ACMCertificateArn': cert['CertificateArn'],
                    'SSLSupportMethod': 'sni-only',
                    'MinimumProtocolVersion': 'TLSv1.1_2016'
                },
            }
        )

        return ressult['Distribution']

    def await_deploy(self, dist):
        """Wait for dist to be deployed."""
        waiter = self.client.get_waiter('distribution_deployed')
        waiter.wait(
            Id=dist['Id'],
            WaiterConfig={
                'Deplay': 30,
                'MaxAttempts:': 50
            }
        )
