# System Specification Requirements

## Purpose

This project is a quiz platform for enabling students to attempt quizzes. It has been created using Django (a Python framework for web development) and with MySQL as the database.

## Scope

The platform is for conducting a single quiz. Users can register and login to the portal. The questions are reassigned at login. The leaderboard does not store past performance, ie, it will contain a single entry for a given student. Questions can be added/removed/modified by updating the database through SQL or using the Django admin page. The platform is capable of servicing multiple students through a single system at the same time. 

The database must contain atleast 10 questions when the app is run. We have included this in the demo SQL file. The program also allows to change the number of questions in the quiz by changing the `nquestions` parameter passed to the `assign_questions()` function defined in the file `users/views.py` 

In the future, additional functionality can be provided through the Django admin functionality by calling the MySQL procedures that we have written.

## System requirements

First, clone the repository from the link:

```bash
git clone https://github.com/Rohan-Witty/DBS-Quiz-App.git
```

and `cd` into the directory. Ensure that there is a working installation of python (>=3.8) on your system. To set up, initialise a new environment (with conda, venv or any other tool of your choice) and run

```bash
pip install -r requirements.txt
```

in the home folder of the project.

## Setup

Run the contents of the sql file titled DBS_PR_13_SQL_2020A7PS0081P.sql on SQL workbench.

On the terminal, run 

```bash
python manage.py makemigrations
python manage.py migrate --fake
python manage.py migrate --fake sessions zero
python manage.py migrate
python manage.py runserver
```

Now the app should be accessible through the url displayed on the terminal.
