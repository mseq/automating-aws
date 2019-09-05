
# automating-aws with python

Repository for AWS Automation with Python

## 01-webotron

  Webotron is a script that will sync a local directory to an S3 bucket,
  and optionally configure Route 53 and cloudfront as well.

### Webotron Features

  Webotron currently has the following features:

- List bucket
- List contents of a bucket
- Create and Setup a Bucket
- Sync directory tree to bucket
- Setup a hosted zone and record set for the host, based on an already existing
registered domain
- Setup CloudFront Distribution using an already created Certificate from ACM
- Set AWS profile with --profile=[profileName]

## 02-notifon

 Notifon is a project to notify slack users of changes to your AWS account
 using CloudWatch Events

### Notifon Features

- Send notifon to Slack when cloudwatch events happen.

## 03-videolyzer

 Videolizer does a video analysis using AWS Rekognition. Is is triggered by 
 video uploads to S3, and insert the Labels detected by Rekognition on a
 DynamoDB table.

### Videolyzer Features

- StartVideoProcessing using Lambda function when new video is uploaded to S3
- HandleLabelDetection using Lambda function when Rekognition finishes the analysis 
and insert the result data on DynamoDB Table.
