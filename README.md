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

codecommit image : ![alt text](<Screenshot 2024-04-21 182138-1.png>)

# ELASTICBEANSTALK :

The elasticbeanstalk is works as a platform as a service

Elastic Beanstalk is a service for deploying and scaling web applications and services. Upload your code and Elastic Beanstalk automatically handles the deployment—from capacity provisioning, load balancing, and auto scaling to application health monitoring.

Elastic Beanstalk image : ![alt text](<Screenshot 2024-04-21 173619.png>)

Click on the create application

Environment Creation : ![alt text](<Screenshot 2024-04-21 173715.png>)

Give the application name and configure the environment

Check the availability of domain because it should be unique

Image : ![alt text](<Screenshot 2024-04-21 173818-1.png>)

Select application code as sample application

set the ec2 virtual machine as single instance(free-tier-eligible)

Image : ![alt text](<Screenshot 2024-04-21 173914.png>)

Configure the service access :

Give the service role for the elasticbeanstalk

Give the keypair for the ec2-instance

Create and Give the ec2-instance-profile for the elasticbeanstalk to access the ec2

Next enter the option Skip to review because we don't need any other services for this project

Image : ![alt text](<Screenshot 2024-04-21 174019.png>)

Than click on the submit button

Image : ![alt text](<Screenshot 2024-04-21 174153.png>)

The environment creation is started

Image : ![alt text](<Screenshot 2024-04-21 174402.png>)

The Environment is successfully created

![alt text](<Screenshot 2024-04-21 174510.png>)
![alt text](<Screenshot 2024-04-21 174526.png>)

# CODEPIPELINE

Now go to the codepipeline and click on the Create Pipeline

Image : ![alt text](<Screenshot 2024-04-21 174651.png>)

Give the pipeline name, select the pipeline-type and execution-mode

Image : ![alt text](<Screenshot 2024-04-21 174903.png>)

# SOURCE

Click on Create a new-service-role

than click on next option

Image : ![alt text](<Screenshot 2024-04-21 174925.png>)

# CODEBUILD

Give the provider name as codebuild

Select the region

Image : ![alt text](<Screenshot 2024-04-21 175118.png>)

Click on the create project

Select the build environment details

Image : ![alt text](<Screenshot 2024-04-21 175303-2.png>)
 
Select the details regarding the operating system and the runtime

create the new-service role

Image : ![alt text](<Screenshot 2024-04-21 175321.png>)

Enter the buildspec.yaml file name in the build specifications

Image : ![alt text](<Screenshot 2024-04-21 175343.png>)

select the cloudwatch for logs and click on the continue to the codepipeline

than click on next to go to deploy stage

Image : ![alt text](<Screenshot 2024-04-21 175353.png>)

# DEPLOY

Select the ElsticBeanstalk as deployer in deploy provider

Select the application name and environment name you have created in the elastic beanstalk and click on next to create the pipeline

The pipeline is created

Image : ![alt text](<Screenshot 2024-04-21 175449.png>)

The source stage is successfully succeeded

The Build stage is successfully succeeded

Image : ![alt text](<Screenshot 2024-04-21 181612.png>)

The deploy stage is Successfully Executed

Image : ![alt text](<Screenshot 2024-04-21 181627.png>)

The Environment is successfully updated in&by the elasticbeanstalk

Image : ![alt text](<Screenshot 2024-04-21 181520.png>)

The Application is Successfully Deployed in the Production Level and made Available for the users

Due to the Autoscaling and loadbalancing features of elasticbeanstalk the application works continuously and consistensly

Image : ![alt text](<Screenshot 2024-04-21 181554.png>)


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


