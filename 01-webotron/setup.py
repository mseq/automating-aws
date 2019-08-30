from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Marcelo Sequeiros',
    author_email='mseq@globo.com',
    description='Webotron 80 is a tool to deploy static websites on AWS S3 Buckets.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/mseq/automating-aws',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)