# MyCatGenerator
Created git repo
created instances
create firewall rules
git clone repo in instance-1 via vs code
installed docker, ansible and python on instance-1
ssh setup for instance-1/docker/ansible
create ansible folder
create roles with:
- docker-compose
- docker 
- jenkins
- nginx
- python
- swarm-manager
- swarm-worker

edited playbook.yml and inventory.yml
edited the main.yml in the tasks folder of every folder in roles
create new user and add it to visudo. Add instance-1 ssh to authorized_keys

Installed Jenkins and created a new pipeline item as the project

ssh key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCdCUE0i1SPt2CGMAPBs5k0DcxyRHGg2tYhLjGTo0lepDHy7zsp+S1tLKrbu7hdSkKvNVrcmGUFX+RCWXIVRkmzLpdTQq3HrD8n7UPru6byMX2FA8iEvqcxK2e1+0Qe2YEUmGPum5WdacLT6KiSBlAptZD7cw9M6k52FU/PBokTFvjZePzaM34e9x14yl01mLjO+DEmOEwYiYkv1M1Ns26b7LA5WXB2oBUxlYpSi9G5zq48xqC8PeZPXZbUDt+bwqkTuuJ0xKZLJhfDstSQtfNitgq+VTmwy4zwcsVsZi2lloP/75Z+ZpYY0BoU9M40zC+Qk6YCxJhFoj272FiAso+gZdBHMHmY18B6ep8NdKB2BIuvfGSSeBrzCVJxguQr04hEQm9c62jhZ23HU64pO4jho7mdkMuT96/yssuuSK969Y/mehzfuxpmsGDZn0lZJhK9Ce6MMfG4kGTzokkrywqNQsSxYYBRD4LPdM2s+vEj9QrF2ws91ufE52Te8u/R8xqlNYsk0PfoohlruJslzt97epd2/rmRlJlwSsDijIOdclO7iWecMhFuKagJN5xwzQfoPxBPdoajLmuqXOXWqC2h4CBURy9wFtihVEghqhpTaxXu2E8Sw/ymEvIq0CwKrxTIkdtoGB3hq2+sc8xwVkqUqYQf4QomVm/O0X65Tge1A6w== phoenix@PhoenixPC

ssh for instance-1
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCoLGGC8NKE9MRzgaw1iXiuKbvETh4s51gUH5itBZispLG8W68Bk/JwIDJSNxWRTGqZmJQesDq4EXPmE2NmTFeZYAqPwjJTH1a1DyJpt5tdS3kXrkjAxv2nraTrkqm7GiXrkvtTAmYZVQQLjL8Q1y4grnfzQBR7WIWWt6rcTmiwjd9W7+iRvBbh67BzY9jAFt8289Z2xUyzRDanePysg85wDiQdXqUWrH4C21bC37JlCTB6bUcFB7Tbmib/Mbn0TEsPNd0clE5IOP06jv5Y1drdhoJlIbY6a0qwviMRiXsSytYIbSreQ1UAVdHa8ARbKlRKp1UI0XaMld2WuiaOFO5mpccB25saHUzAusGv8K9VA4zxQUAFH/En3Kt9T+BbrkSPBS7j7+sW9TJF8To0exU+maBa/ImLotEoJM/NFLuAG5IqVebeyjIlXhPiubobmjteP9MDkqMRPd2HnuyNKRcFTGPQJ0OuLcLGilmSRxb0kuMlYizZsQfTg/197LVyn40= ellahiphotography@instance-1

Jenkins admin pw 064953079e5b47f796cc9a25c8d85fab

http://34.89.39.79:8080/

Installed Jenkins

# The QA Project

## Intro
This repository contains my QA Practical Project. The purpose of this ReadMe is to outline how I met the key deliverables of the assigned project with supporting documentation.
Welcome to Catman9000's Repository. This .ReadMe file will walk you through how I approached the project, despite numerous difficulties and obstacles, and how I resolved the issues, as well as what I would have liked to do better. 

## Contents

A. [The Project](#The-Project)
B. [The App](#The-App)
C. [What's a CI Pipeline?](#Cont-Int-Pipeline)
D. [What went wrong?](#Issues)
E. [Going forward](#For-the-future)


## The Project

First of all, the project itself was very exciting. There were numerous things to learn and I really enjoyed the ins and outs of what it would entail. The primary goal of this objective was to have an application ready that followed the CRUD (Create, Read, Update, Delete) methodology.
The application itself required several key components and tools which would bring it all together. These included a Flask back-end framework which itself allows for use of extended and standard functions via imports, and which would be interacted with via a simple html-coded page hosted on Google's Cloud Servers. It would be written in Python, making use of numerous other imports and extensions and functions. It was also used to show relations between tables.

My project also made use of numerous methods, workflow decisions and tools to assist me in the creation of the application. These included Git, Python development, HTML coding, Jenkins, CI and of course managing the whole workflow of the project itself.

To manage my workflow, I used Jira, which is known to be extremely effective in helping both small developers and enterprise-level company teams manage their workflow. In my own experience, it is very helpful in keeping track of errors, timing the project and also measuring progress. 

Although I did set up Jenkins as shown below, I unfortunately was not able to get it working in time due to several issues with Google Cloud which were shown to my instructor Adam. These took a lot of time and ate into valuable time-based progress as a lot of things were dependent on them. I have also screenshot that particular error too.


![Flask diagram](https://github.com/Catman9000/TheDatingGame/blob/main/ERD.png)

## The App

The basis of my app was to have a very simple website where the idea was I am using it to manage my own stock of cat inventory. Originally, the idea was to have a dating quiz, however due to difficulties in my project and GCS bugs which were Google-Side, I was unable to carry out the original project. As a result, I decided to tame it down and do the best I could until everything was sorted. Unfortunately, this took a bit of time and is not something I expected to face given the time constraints and usual reliability of big cloud vendors. However, this has also taught me a valuable lesson to make sure I plan far ahead in case such occurances happen. 

The tables in the shop were thus 3: 
A Product table which could create entries, delete entries, update entries and read them from the database.
A User table which could create user entries in the event that I need to take a trip and someone needs to look after my cats and can manage it all.
A Shopping Cart-style table which would contain orders on the way as well as who ordered them and what, so that expenditure can be managed and things aren't ordered in excess. 
My ERD Diagram is as follows:

![ERD diagram](https://github.com/Catman9000/TheDatingGame/blob/main/ERD.png)

The ERD diagrams helped me visualise how I wanted to plan the project going forward and what shape and form my database tables would look, as well as what kind of data they would contain. This is helpful because it helps to plan ahead the relationships between the various tables within the database and how they will interact with each other.
The relationship between User and Item is one to many.
The relationship between Item to Orders was many to one, and the relationship between shop orders and user was many to one.

I would have preferred to have a more full-fledged interactive website, which would track the orders and deliveries between my 3 cats, and assign product types, favourites, who issued the orders as well as total cost/expenditure. This is something I plan to do going forward.

## CI Pipeline

A CI Pipeline is a working policy widely adopted, a guideline, so to speak, that allows one to carry out several aspects of their application development, building, integration, testing, deployment and tracking. A good CI Pipeline is one that allows the person to have peace of mind whilst insuring that the project itself is completed on time whilst also being continuously improved, reiterated, and delivered in a timely manner that also automates the more tedious aspects that can have a big impact on one's work, such as automated backing up on the cloud via git or automated deployment via Jenkins.

For tracking, I chose Jira. This is because it's what I learnt on the course, and since I'm familiar with it, I decided it's the best option for me.

I decided to follow the structure I was taught in my 4 week course, including making use of user stories, following the format of "As a user/developer, I want to... So that...."

I also broke down the project planning into 3 parts:
To-Do: The parts of the project that are/were to be done,
In Progress: In progress/things being worked on,
Done: What was completed.

Below is the structure of the tools and my CI Pipeline.

![Project Roadmap](https://github.com/Catman9000/TheDatingGame/blob/main/CI.png)

![Jira](https://github.com/Catman9000/TheDatingGame/blob/main/Jira%20workflow.png)

Git was my dedicated choice of Version Control System, due to it being extremely reliable and also having features in place that work well with a developer workflow. I made use of branches so that everything in my project was not just on the main branch. This was so that if anything went wrong, my main working instance of the whole application wouldn't be affected, causing setbacks or even total loss of functionality.

I also used MySQL to set up the databased and also cross-integrated and managed via SQLAlchemy in Flask.

Below is my network graph, which is something Github generates via insights to show the branches and structure of the changes and commits. This is useful because it gives you a visual representation, and also helps identify at what stages changes were committed, as well who made them and at what level.

![Network Graph](https://github.com/Catman9000/TheDatingGame/blob/main/network.png)

Jenkins was used to build and deploy via automation, as well as running integration testing.

![Jenkins](https://github.com/Catman9000/TheDatingGame/blob/main/jenkins2.png)

![Jenkins Two](https://github.com/Catman9000/TheDatingGame/blob/main/jenkins3.png)


## My App - The Cat Stock Inventory

Here is the main homepage:

![Homepage](https://github.com/Catman9000/TheDatingGame/blob/main/Homepage.png)

Here, the homepage automatically displays the inventory so it's easy to check at a glance. 

![Add User](https://github.com/Catman9000/TheDatingGame/blob/main/Add%20User.png)

Add a user

![Add Item](https://github.com/Catman9000/TheDatingGame/blob/main/Add%20Item.png)

Add Items, Update, Delete, Read.

## Risk Assessment:

![Risk assessment](https://github.com/Catman9000/TheDatingGame/blob/main/Risk%20Assessment.png)


## Known Issues:

GCP's APIs on my account refused to work despite numerous attempts, so I had to halt my project until a fix was found. This severely impacted my progress and was very spontaneous, having no rhyme or rhythm. This resulted in several issues that impacted the whole of the project, including leaving me short on time and affecting Flask development, server instancing, Jenkins too.

## Future Improvements:
Given time to reiterate and further improve the project, I would have preferred to make some final adjustments and changes to the project, in addition to the ones mentioned already. These include:

* - UI - Given the nature of the web application, I would have preferred to have a more aesthetic website that was easier on the eye and not as rough-looking.

* - Bugs - I would have liked to resolve bugs and slight errors that occured. This is because if I have an application, I would want to eliminate all bugs so that it works as smoothly as possible. Given my relative inexperience, this was to be expected but it is the end goal regardless and one I strived to work towards.

* - Jenkins