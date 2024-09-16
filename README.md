  # Streamlining Deployment with AWS: A Comprehensive CI/CD Project

  Introduction:
  
In the ever-evolving landscape of software development, the quest for efficiency and automation is relentless. Embracing this ethos, I embarked on a journey to construct a robust Continuous Integration and Continuous Deployment (CI/CD) pipeline using AWS services. Leveraging the power of CodePipeline, GitHub, CodeBuild, and Elastic Beanstalk, I sculpted a seamless deployment mechanism to propel my projects forward. 

# DEVELOPMENT OF CI/CD USING AWS :
 SOURCE AS : CODECOMMIT

 BUILD AS  : CODEBUILD

 DEPLOY AS : ELASTICBEANSTALK


# Created a Git repository Using CodeCommit

repo name : sathishrepo3

Clone Url : https://git-codecommit.ap-south-1.amazonaws.com/v1/repos/sathishrepo3

added the files:

.ebextensions

app.py

buildspec.yaml

requirements.txt

Commited the files:

Git commit -m " added the app.py , requirements.txt , .ebextensions and buildspec.yml files "

used "git push origin main" to push the changes to central repository

codecommit image : ![1](https://github.com/user-attachments/assets/13535eba-0faf-47b3-b7f4-cd7556992b0d)

# ELASTICBEANSTALK :

The elasticbeanstalk is works as a platform as a service

Elastic Beanstalk is a service for deploying and scaling web applications and services. Upload your code and Elastic Beanstalk automatically handles the deployment—from capacity provisioning, load balancing, and auto scaling to application health monitoring.

Elastic Beanstalk image : ![Screenshot 2024-09-10 161412 2](https://github.com/user-attachments/assets/e32fdc2e-1d0d-4a24-8ef9-4b02264f9b71)

Click on the create application

Environment Creation :![Screenshot 2024-09-16 135519 3](https://github.com/user-attachments/assets/5b43b0cc-dd59-41a9-8732-a0f26e77290c)

Give the application name and configure the environment

Check the availability of domain because it should be unique

Image :![Screenshot 2024-09-16 135659 3](https://github.com/user-attachments/assets/31502c76-e11e-4a2c-bdeb-4aa75d9a6361)

Select application code as sample application

set the ec2 virtual machine as single instance(free-tier-eligible)

Image : ![Screenshot 2024-09-16 135800 4](https://github.com/user-attachments/assets/72e0456d-5f85-4094-b1f3-6901855b67c5)

Configure the service access :

Give the service role for the elasticbeanstalk

Give the keypair for the ec2-instance

Create and Give the ec2-instance-profile for the elasticbeanstalk to access the ec2

Next enter the option Skip to review because we don't need any other services for this project

Image : ![Screenshot 2024-09-16 135900 5](https://github.com/user-attachments/assets/1425f6e7-866a-4b3a-85fc-e4cd2a6fbe13)

Than click on the submit button

Image : ![Screenshot 2024-09-16 140103 6](https://github.com/user-attachments/assets/73827d49-a856-4c90-9176-d6e69c2ff9bb)

The environment creation is started

Image :![Screenshot 2024-09-16 140205 7](https://github.com/user-attachments/assets/9c842517-0891-4685-a0cb-ff0c75536ed4)

The Environment is successfully created

![Screenshot 2024-09-16 140353 8](https://github.com/user-attachments/assets/d9c5aec8-8402-413c-a842-a27756500f26)
![Screenshot 2024-09-16 140407 9](https://github.com/user-attachments/assets/59755a4f-df74-4962-af76-1bd22791d6c4)

# CODEPIPELINE

Now go to the codepipeline and click on the Create Pipeline

Image : ![Screenshot 2024-09-16 140440 10](https://github.com/user-attachments/assets/2accb033-8d7b-4153-9aee-76c15763e5a2)

Give the pipeline name, select the pipeline-type and execution-mode

Image : ![Screenshot 2024-09-16 140522 11](https://github.com/user-attachments/assets/bbe0ca46-a567-4ae9-a654-ee8cfed156ba)

# SOURCE

Click on Create a new-service-role

than click on next option

Image : ![Screenshot 2024-09-16 141420 12](https://github.com/user-attachments/assets/844cb7c0-e406-40ae-a6aa-18a5de0c9d89)

# CODEBUILD

Give the provider name as codebuild

Select the region

Image : ![Screenshot 2024-09-16 141614 13](https://github.com/user-attachments/assets/23ecc86f-1cdd-4740-82de-96a172bb4ff2)

Click on the create project

Select the build environment details

Image :![Screenshot 2024-09-16 151910 14](https://github.com/user-attachments/assets/c204a511-4906-4b3d-b0e1-c2affc41b93f)

 Select the details regarding the operating system and the runtime

create the new-service role

Image : ![Screenshot 2024-09-16 151929 15](https://github.com/user-attachments/assets/b6e0cbfe-32b4-4f16-8edb-d7868387f23a)

Enter the buildspec.yaml file name in the build specifications

Image : ![Screenshot 2024-09-16 152001 16](https://github.com/user-attachments/assets/6a7c948f-8759-4b14-bdd1-c48cb7eb385f)

select the cloudwatch for logs and click on the continue to the codepipeline

than click on next to go to deploy stage

Image : ![Screenshot 2024-09-16 152037 17](https://github.com/user-attachments/assets/d498df64-6eb6-43cd-8691-39d52f578fbf)

# DEPLOY

Select the ElsticBeanstalk as deployer in deploy provider

Select the application name and environment name you have created in the elastic beanstalk and click on next to create the pipeline

The pipeline is created

Image : ![Screenshot 2024-09-16 152054 18](https://github.com/user-attachments/assets/6eee9efd-0368-4933-883c-74d824d37c6d)

The source stage is successfully succeeded

The Build stage is successfully succeeded

Image : ![Screenshot 2024-09-16 152116 19](https://github.com/user-attachments/assets/62d752d8-79c5-47c9-b681-35621bdca725)

The deploy stage is Successfully Executed

Image :  ![Screenshot 2024-09-16 152116 19](https://github.com/user-attachments/assets/62d752d8-79c5-47c9-b681-35621bdca725)

The Environment is successfully updated in&by the elasticbeanstalk

Image : ![Screenshot 2024-09-16 145653 20](https://github.com/user-attachments/assets/1b62e784-d86a-4c59-9e09-f08a67166fa3)

The Application is Successfully Deployed in the Production Level and made Available for the users

Due to the Autoscaling and loadbalancing features of elasticbeanstalk the application works continuously and consistensly

![Screenshot 2024-09-16 152135 21](https://github.com/user-attachments/assets/128a6a2b-2daf-496c-aa0f-8fe5afae8395)



  # Architectural Blueprint:

1. GitHub Repository: At the heart of the operation lies the GitHub repository, serving as the sanctuary for my source code. GitHub's collaborative environment fosters teamwork and version control, enabling smooth code management and collaboration.
2. CodeBuild Build Spec: With CodeBuild, I crafted a build specification meticulously tailored to my project's needs. This blueprint guides CodeBuild in executing tasks such as compilation, testing, and artifact generation, ensuring the production of pristine deployable artifacts.
3. CodePipeline Orchestration: CodePipeline emerges as the conductor of the symphony, orchestrating the entire release process. It orchestrates the flow of changes from GitHub to Elastic Beanstalk, seamlessly transitioning through stages of Source, Build, and Deploy.
4. Elastic Beanstalk Deployment: Elastic Beanstalk serves as the launchpad for my applications, providing a managed platform for deployment and scalability. Its auto-scaling capabilities and environment configurations simplify the deployment process, ensuring swift and hassle-free launches.

 # Crafting the Pipeline:

1. GitHub Integration: I established a connection between GitHub and CodePipeline, enabling automatic triggering of pipeline execution upon code commits. This bidirectional integration fosters a seamless workflow, ensuring rapid feedback loops and iterative development cycles.
2. CodeBuild Configuration: Configuring CodeBuild involved defining a build environment tailored to my project's requirements. I fine-tuned parameters such as build specifications, environment variables, and caching mechanisms to optimize performance and efficiency.
3. CodePipeline Setup: Within CodePipeline, I delineated distinct stages to encapsulate the deployment journey. The Source stage fetches the latest code changes from GitHub, while the Build stage invokes CodeBuild to generate deployable artifacts. Finally, in the Deploy stage, Elastic Beanstalk takes center stage, orchestrating the deployment of the application.
4. IAM Permissions and Security: Security is paramount in the cloud ecosystem. I meticulously configured IAM roles and permissions to govern access and execution privileges, ensuring the integrity and confidentiality of my CI/CD pipeline.

 # Validation and Iteration:
Before unleashing the pipeline into the wild, rigorous testing and validation were imperative. I subjected the pipeline to a battery of tests, including integration tests, end-to-end testing, and performance evaluations. Through iterative refinement and optimization, I fine-tuned the pipeline to perfection, primed for production deployment.

 # Conclusion:
In weaving together the threads of GitHub, CodePipeline, CodeBuild, and Elastic Beanstalk, I've woven a tapestry of automation and efficiency. This CI/CD pipeline stands as a testament to the power of AWS in empowering developers to accelerate the software delivery lifecycle. With every commit and deployment, the journey continues, propelled by the relentless pursuit of innovation and excellence.


# The Project Is Completed Successfully


