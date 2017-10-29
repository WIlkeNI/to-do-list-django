# to-do-list-django

Django version: 1.11.2
python version: 3.5.2
virtualenv version: 15.1.0

If you have already installed python and you don't want to break those settings you can start a virtualenv environment, install the django and go through all the others steps.

In order to execute:

1) Download the project and the database.

2) Create a mysql user database named 'usertodolist', and password 'usertodolist' #if you want, you can change the name and pass, and then modify the django config file

3) Import the mysql database.
$mysql -u <username> -p <databasename> < <filename.sql>

4) Enter the app root directory, and run:
$python3 manage.py migrate
$python3 manage.py runserver

5) Enter to your localhost, port 8000 (django default) and enter with the user you want:

*)super_admin_user --> username: e_user_tdl password: e_user_tdl
**)regular_user --> username: usuario password:envolsers

If step 5 doesn't work, create a superuser with python manage.py createsuperuser, loggin with those credentials and create a regular user.
