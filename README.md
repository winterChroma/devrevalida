# classy.io - a web app that classifies images

This web app was created as part of the Accelerated Cloud Cadetship and Enablement (AC2E)'s Developer Associate Stint.

## classy.io showcases 3 features:

1. Dockerized implementation of a functioning classifier app
2. Three classification models trained with fast.ai, a library built on top of PyTorch
3. Ready-to-deploy web app with AWS Elastic Beanstalk

### Note: During the showcase of the web app, a working CI/CD pipeline was also implemented. It allowed the developers to see deploy new changes in the application seamlessly.

## How to Deploy to AWS Elastic Beanstalk

1. Create a **web server environment** from the AWS Elastic Beanstalk Console.
2. Select the **Docker** as the preconfigured platform.
3. Upload the contents of this repository as a zip file.
4. Click **configure more options**.
5. In the section *"Software"*, click modify. Change the **proxy server** from *"nginx"* to **"None"**.
6. In the section *"Instances"*, click modify. Change the **instance type** from *"t2.micro"* to **"t3.small"**.
7. Press create environment.
