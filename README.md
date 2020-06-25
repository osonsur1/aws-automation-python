# Automating AWS with Python

Repository for AWS automation with python

## 01-webotron

Webotron is a script that will sync a local directory to an S3 bucket, and optionally configure Route 53 and CloudFront as well.

### Features

Webotron currently has the following features:

- List buckets
- List contents of a bucket
- Create and set up bucket
- Sync directory tree to bucket
- Set AWS profile with --profile=<profileName>
- Configure route 53 domain 
- Configure CloudFront CDN and SSL