# squiz
A web portal created to provide platform to host quiz.

## About
This project is based on Django.

## Features:

  - Teachers and students can signup and login into the portal.
  - Teachers and students have differente features(interface)
  - Leaderboard page for viewing the perofrmance of fellow mates in different quiz
   
This portal is provided with interface for both students and teachers, where:--
### Teachers can: - 
  - add quiz
  - view performance of students
  - view their profile
  - view response of students corresponding to each questions
  - view the score of each students
  - view the quiz(questions, options and correct answer)
 
 ### Students can: -
  - give quiz
  - can only view response if quiz is already given
  - can view their answer corresponding to each question
  - can see their profile
  - on profile, they can view all the quizes attempted, with their scores and the teacher who conducted the quiz
  
 ## Install
  - setup virtual environment on your system

  - Run the following command from your terminal: 
  ```
  git clone https://github.com/kks0101/squiz
  ```
  - Switch to the directory *squiz/*
  
  - create and activate virtual environment using following commands: 
  ```
  virtualenv venv
  source venv/bin/activate
  ```
  - install necessary packages using :
  ```
  pip install -r requirements.txt
  ```
  - switch to the directory having **manage.py** file
  
  - Execute
  ```
  python3 manage.py runserver
  ```
  - open the given link in the browser and there you go :)
  
