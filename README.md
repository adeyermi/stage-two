# stage-two
zuri task 
 rest {Project name}



 Table of Contents
- [Overview]
- [Getting Started]
  - [Prerequisites]
  - [Installation]
- [Usage]
- [API Endpoints]
- [Deployment]
- [License]
- [Acknowledgments]


--Overview

The project is  created as part of task given in zuri internship, the goal of the project is to build a swift and simple REST API which is capable of CRUD operations on a "person" resource interfacing with Django framework  

--Getting Started
A good working pc and a good wokring enviroment is required, django is a less complicated framework, so you will love using the framework 

	Prerequisites

  How to set up and run the project locally.
If you are new to Python we are going to need the following to carry out operations:  
- Python 3.11
- Django
- Django REST framework

Download Python 3.11 and above to your pc depending on your operating system 

	Installation

After installation, open your cmd/bash and install python django;

To install Django on your pc with the following instructions/code
   --pip install django
create folder on your pc for the project;
Create a virtual environment (recommended)
-----python -m venv venv
Activate the virtual environment
source venv/bin/activate
Install dependencies
----pip install -r requirements.txt
Locate your folder on cmd and startproject
---- python django-admin startproject (projectname) rest 
cd to your project dir (rest) 

Then startapp
-----python manage.py startapp

 Run migrations
python manage.py migrate

 Start the development server
python manage.py runserver

USAGE:
Click on the link yermi.pythonanywhere.com/api, yuo will be directed to create a new users details, submit your details like User_id which are ussually integers, your fullname which are strings, your email(strings and/or integers) and lastly your Phonenumber which are ussually integers. Click submit button and you will be led to the "show page".

https://yermi.pythonanywhere.com/show the show page displays all the data available in the database, it allows you to view, edit/update and Delete a data in the database 

API Endpoints:
POST/api: 		yermi.pythonanywhere.com/api
GET /api/{user_id}:	https://yermi.pythonanywhere.com/show
PUT /api/{user_id}:	https://yermi.pythonanywhere.com/edit/2 (the last integer at the back of edit refers to the user_id)
DELETE /api/{user_id} 	https://yermi.pythonanywhere.com/show (click on the delete button) 

Deployment
Create repository and hosted on pythonanywhere.com 

License
This project is licensed under the [Adeyermi] with the help of ZURI internship

Acknowledgments
Special thanks to ZURI internship/ alot of helps come from youtube video, google search,tackoverflow comments, reddit and fellow zuri intership 
