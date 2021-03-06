
# QA Practical Project

## Intro
This repository contains my QA Practical Project. The purpose of this ReadMe is to outline how I met the key deliverables of the assigned project with supporting documentation.

## The Project

The aim of this project was in line with the brief assigned by QA, the objective of which was to utilise an architecture comprised of a front-end service and three other apis which were containerised via the use of Docker, which would allow them to communicate with each other. The brief required, amongst other things:

* Ansible knowledge

* Advanced Python knowledge

* Use of virtualised containers

* Basic website html coding

* Flask knowledge

* Requiring 4 APIs that can cross-interact

To this end, my CI pipeline consisted of:

* Software Planning/Tracking = Jira

* VCS = Git

* CI Server: Jenkins

* Virtual Containerisation: Docker

and more.

# Breakdown of the application


![Website in action](https://github.com/Catman9000/MyCatGenerator/blob/main/Website%20in%20action.jpg)


![ApplicationVSCode](https://github.com/Catman9000/MyCatGenerator/blob/main/The%20application%20in%20vscode.jpg)

As everyone in the class surely knows, I have a soft spot for cats. I have three of them so I decided to once again include them in my project, and by definition, the application and its contents.

I have broken down the application in this readme as it appears logically.




![Service 1](https://github.com/Catman9000/MyCatGenerator/blob/main/Service%201.jpg)




## Service 1 - Front-End
First and foremost is what is known as the front-end. 
This is what the end-user interacts with, and it acts as a sort of tunnel from which the other 3 services can cross-communicate and output to the user. The services operate on a combination of methods, including GET and POST. This is also mentioned again when describing each service so you can know how the application functions.
An sql database container is where the results are stored so that they can then be output on the webpage to show previous results. 


![Service 2](https://github.com/Catman9000/MyCatGenerator/blob/main/service%202.jpg)


## Service 2 
Secondly, we have something known as Service 2. In my application, this is the service that operates on a GET method. This service responds assigns a cat.


![Service 3](https://github.com/Catman9000/MyCatGenerator/blob/main/service%203.jpg)

## Service 3
Thirdly, Service 3 operates on a GET method too. It determines a treat name assigned at random to be given to the cat picked at random.




![Service 4](https://github.com/Catman9000/MyCatGenerator/blob/main/Service%204.jpg)

## Service 4
Finally, Service 4 operates on a POST method. Making the use of JSON scripting which allows us to manipulate data and code in various ways, the ultimate goal is to allow it to post a randomly generated day the cats will be fed on. This object is created based on the results of the other two services.


## Ansible-Roles

![Ansible-Roles](https://github.com/Catman9000/MyCatGenerator/blob/main/ansible-roles.jpg)


Ansible galaxy roles were used to provision the underlying infrastructure of my virtual environment, as well as provision resources and assign roles inside my cloud network alongside Docker.

## Risk Assessment

A risk assessment is important to be carried out as it allows me to take any possible setbacks into account and allows me to have some failsafes in place, as well as employ best practices which have been proven to mitigate against numerous risks. Below is my risk assessment:



![Risk-Assessment](https://github.com/Catman9000/MyCatGenerator/blob/main/Risk%20Assessment.png)



## CI Pipeline

A CI Pipeline is a working policy widely adopted, a guideline, so to speak, that allows one to carry out several aspects of their application development, building, integration, testing, deployment and tracking. A good CI Pipeline is one that allows the person to have peace of mind whilst insuring that the project itself is completed on time whilst also being continuously improved, reiterated, and delivered in a timely manner that also automates the more tedious aspects that can have a big impact on one's work, such as automated backing up on the cloud via git or automated deployment via Jenkins.

## Jira

For tracking, I chose Jira. This is because it's what I learnt on the course, and since I'm familiar with it, I decided it's the best option for me.



![Devstory](https://github.com/Catman9000/MyCatGenerator/blob/main/Devstory.jpg)



![Userstory](https://github.com/Catman9000/MyCatGenerator/blob/main/Userstory.jpg)


I decided to follow the structure I was taught over my 8 weeks so far, including making use of user stories, following the format of "As a user/developer, I want to... So that...."

![Jiraboard](https://github.com/Catman9000/MyCatGenerator/blob/main/Process%20of%20making%20Jira%20backlog-sprint.jpg)

The Kanban-style board helped me visualise how I wanted to plan the project going forward. This is helpful because it helps me to plan ahead the relationships between the various services and the data contained within, as well as how they will interact with each other.

![Colourcoded](https://github.com/Catman9000/MyCatGenerator/blob/main/Colour%20coded.jpg)

The colour-coding also helps me focus and helps me keep track of what is going on easier as well.



I also broke down the project planning into 3 parts:
To-Do: The parts of the project that are/were to be done,
In Progress: In progress/things being worked on,
Done: What was completed.
This was also managed with respect to time, so different tasks of different importance were given variable lengths of time and weighing in the importance of the application too.

![Roadmap](https://github.com/Catman9000/MyCatGenerator/blob/main/My%20Roadmap%20Jira.jpg)

And here is a view of the Sprint in progress and the backlogs in accordance.

![ProcessSprintJira](https://github.com/Catman9000/MyCatGenerator/blob/main/Jira%20board%20sprint.jpg)

## GIT

Git was my dedicated choice of Version Control System, due to it being extremely reliable and also having features in place that work well with a developer workflow. I made use of branches so that everything in my project was not just on the main branch. This was so that if anything went wrong, my main working instance of the whole application wouldn't be affected, causing setbacks or even total loss of functionality.

![Gmain](https://github.com/Catman9000/MyCatGenerator/blob/main/Github%20%2B%20readme%20main.jpg)

Below is my network graph, which is something Github generates via insights to show the branches and structure of the changes and commits. This is useful because it gives you a visual representation, and also helps identify at what stages changes were committed, as well who made them and at what level.

![Network Graph](https://github.com/Catman9000/MyCatGenerator/blob/main/Github%20network%20insight%20graph.jpg)

## Jenkins

Jenkins was used to build and deploy via automation, as well as running integration testing. It's also extremely useful for its many features including webhooks, deploying images, rolling updates and more!


![Webhook](https://github.com/Catman9000/MyCatGenerator/blob/main/Jenkins%20git%20webhook.jpg)


## Postman

I used Postman to test the website and see how the various json code manipulation worked and whether all the methods were working as intended. Below is an example of Postman in action:

![Postman](https://github.com/Catman9000/MyCatGenerator/blob/main/postman.jpg)




## Google Cloud Platform

Google Cloud Platform was used to host the virtual machines. I chose GCP as I am familiar with the setup and it offers high risk and security, as well as features such as backing up disk images, snapshots and SSH security as well as vTPM.


![Firewall](https://github.com/Catman9000/MyCatGenerator/blob/main/firewall.jpg)


Setting up firewall rules and opening ports:

![Previous VM Instances](https://github.com/Catman9000/MyCatGenerator/blob/main/Previous%20VM%20instances.jpg)

![New VM Instances](https://github.com/Catman9000/MyCatGenerator/blob/main/New%20VM%20Instances.jpg)


Due to the result of issues in the first project, I decided to create a separate project and migrated my VMs across and continued from there.

![New VM Instances2](https://github.com/Catman9000/MyCatGenerator/blob/main/new%20vm%20instances%202.jpg)

## Readme

The readme, as you can see, has been completed, and was updated alongside the project along with screenshots taken at each stage to profile the nature of issues when and where they arose, as well as provide a detailed trail of my journey with this project.

![Imagesbeingpushed](https://github.com/Catman9000/MyCatGenerator/blob/main/images%20being%20pushed%20to%20github%20alongside%20application%20and%20readme.jpg)

## Known Issues:

## Jenkins

I encountered a lot of difficulty with Jenkins during my project, especially when it came to solving the fingerprint authentication and SSH and Authorized key bugs.

![JenkinsKeyError](https://github.com/Catman9000/MyCatGenerator/blob/main/Jenkins%20public%20key%20error.jpg)

Researching on keygens and authenticating methods in linux

![Researching](https://github.com/Catman9000/MyCatGenerator/blob/main/researching%20up%20on%20keygen.jpg)

Below is me in the process of fixing this error.

![JenkinsFixingStage](https://github.com/Catman9000/MyCatGenerator/blob/main/Jenkins%20fixing%20stage.jpg)

Modifying SSHD configs:

![SSHD](https://github.com/Catman9000/MyCatGenerator/blob/main/sshd%20config.jpg)


And here I was successful in finally ssh'ing as Jenkins through the Swarm VM.

![JenkinsFixed](https://github.com/Catman9000/MyCatGenerator/blob/main/jenkins%20fixed%20.jpg)


Rolling Update of the website:

![WebsiteRolling](https://github.com/Catman9000/MyCatGenerator/blob/main/Website%20rolling%20update.jpg)

## Future Improvements:


* - UI - Given the nature of the web application, I would have preferred to have a more aesthetic website that was easier on the eye and not as rough-looking.

* - Jenkins
