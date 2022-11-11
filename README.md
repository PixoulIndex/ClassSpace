# ClassSpace
CECS 491 Project

ClassSpace Developer Guide 

—————————————————————————————————————— 

Project Description 

—————————————————————————————————————— 

ClassSpace is a web application that aims to provide students with an environment that allows for sharing of knowledge about their school’s reputation, courses, and instructors with the use of rating and forum pages. 

—————————————————————————————————————— 

Features 

—————————————————————————————————————— 

ClassSpace features will include rating pages for school, courses, and professors.  

Reviewers will be able to provide a “survival guide” after the rating for future students taking the course 

Forums that facilitate discussion among students about school subjects 

Personalized profile complete with customization that includes rewards from engaging with the community 

Contact list that users can use to contact each other privately 

—————————————————————————————————————— 

Setting Up Project 

—————————————————————————————————————— 

Visual Studio Code: 

Download the appropriate version of visual studio code for your operating system 

https://code.visualstudio.com/download 

Run the installer. Choose your setup preferences depending on the version chosen 

https://code.visualstudio.com/docs/setup/setup-overview 

Download and Install Python 3  

https://www.python.org/downloads/ 

Flask-SQL Alchemy: 

Install Flask and Flask-SQLAlchemy extension 

pip install flask flask-sqlalchemy 

You need to import the SQLAlchemy class from this module 

from flask_sqlalchemy import SQLAlchemy 

Create Flask application object and set URI for the database 

app = Flask (__name__) 

app.config [‘SQLALCHEMY_URI’] = ‘sqlite:///students.sqlite3’ 

Create/Use database the database mention in the URI 

db.create_all() 

GitHub Desktop: 

Create or use an existing GitHub account to use GitHub services 

Download GitHub Desktop for your system  

https://desktop.github.com/ 

Connect GitHub to GitHub Desktop 

https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/authenticating-to-github 

—————————————————————————————————————— 

Components 

—————————————————————————————————————— 

ClassSpace (Web App):  

ClassSpace will be the main software product that users will interact with 

User can access all features and functionality here 

User information will be sent and stored to in the SQLAlchemy database 

Flask-SQL Alchemy:  

All user information will be stored in ClassSpace’s SQLAlchemy database. 

—————————————————————————————————————— 

Contributions 

———————————————————————————————————————Currently in the planning phase, we’ll be utilizing GitHub to update ongoing and future development. The contribution link can be accessed here at https://github.com/ 

—————————————————————————————————————— 

Support/Contact 

—————————————————————————————————————— 

For any issues, please contact us through email: classspaceservice@gmail.com 

 

 

 
