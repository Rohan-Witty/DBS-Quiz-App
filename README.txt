## Running Instruction

`cd` into the code directory. Ensure that there is a working installation of python (>=3.8) and MySQL(>= 8.0) on your system. Make sure that the MySQL local server is running. To set up, initialise a new environment (with conda, venv or any other tool of your choice) and run

```
pip install -r requirements.txt
```

in the home folder of the project.

## Setup

Run the contents of the sql file titled DBS_PR_13_SQL_2020A7PS0081P.sql on MySQL workbench.

On the terminal, run

```
python manage.py makemigrations
python manage.py migrate --fake
python manage.py migrate --fake sessions zero
python manage.py migrate
python manage.py runserver
```

Now the app should be accessible through the url displayed on the terminal.