# doc-clf

To deploy to AWS Elastic Beanstalk starting from existing Django App with EB CLI: 

From root dir, eb init -p python-<VERSION> <APP NAME>

eb create <ENVIRONMENT NAME> 

Modify the allowed hosts in settings.py to allow the newly created environment

Modify the SECRET_KEY setting for production, e.g. set an environment variable
  - Be sure to set the environment variable on AWS as well

Modify DEBUG to be False before deploying 

eb deploy 

Helpful link: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
