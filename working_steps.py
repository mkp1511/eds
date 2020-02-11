(1)

MK:~ purohit$ cd projects
MK:projects purohit$ mkdir edsystems
MK:projects purohit$ cd edsystems

(2)
MK:edsystems purohit$ python3 -m venv eds


(3)
MK:edsystems purohit$ source eds/bin/activate


(4)
(eds) MK:edsystems purohit$ python -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/54/0c/d01aa759fdc501a58f431eb594a17495f15b88da142ce14b5845662c13f3/pip-20.0.2-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 8.7MB/s 
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
      Successfully uninstalled pip-19.0.3
Successfully installed pip-20.0.2


(5)
(eds) MK:edsystems purohit$ nano requirements.txt


(6)
(eds) MK:edsystems purohit$ cat requirements.txt
django~=3.0.2


(7)
(eds) MK:edsystems purohit$ pip install -r requirements.txt
Collecting django~=3.0.2
  Downloading Django-3.0.2-py3-none-any.whl (7.4 MB)
     |████████████████████████████████| 7.4 MB 1.3 MB/s 
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.3.0-py2.py3-none-any.whl (39 kB)
Collecting pytz
  Using cached pytz-2019.3-py2.py3-none-any.whl (509 kB)
Collecting asgiref~=3.2
  Downloading asgiref-3.2.3-py2.py3-none-any.whl (18 kB)
Installing collected packages: sqlparse, pytz, asgiref, django
Successfully installed asgiref-3.2.3 django-3.0.2 pytz-2019.3 sqlparse-0.3.0


(8)
(eds) MK:edsystems purohit$ django-admin startproject mysite .
(eds) MK:edsystems purohit$ 


(9)
eds) MK:edsystems purohit$ tree -L 2
.
├── eds
│   ├── bin
│   ├── include
│   ├── lib
│   └── pyvenv.cfg
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── working_steps_eds.rtf

5 directories, 9 files
(eds) MK:edsystems purohit$ 


(10) 
Edit the setting.py file, No need to change the database setting as we are using the default database sqlite3.
ensure that it has the following entries:
(i) LANGUAGE_CODE = 'en-us'
(ii) TIME_ZONE = 'Asia/Kolkata'
(iii) STATIC_URL = '/static/'
(iv) STATIC_ROOT = os.path.join(BASE_DIR, 'static')
(v) ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']


(11)
(eds) MK:edsystems purohit$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK


(12)
(eds) MK:edsystems purohit$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 30, 2020 - 17:25:34
Django version 3.0.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


(13) create .gitignore with the following entries
*.pyc
*~
/.vscode
__pycache__
eds
db.sqlite3
/static


(14)
(eds) MK:edsystems purohit$ git init
Initialized empty Git repository in /Users/purohit/projects/edsystems/.git/


(15)
(eds) MK:edsystems purohit$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore
	manage.py
	mysite/
	requirements.txt
	working_steps.py

nothing added to commit but untracked files present (use "git add" to track)


(16)
(eds) MK:edsystems purohit$ git add -A


(17)
(eds) MK:edsystems purohit$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   .gitignore
	new file:   manage.py
	new file:   mysite/__init__.py
	new file:   mysite/asgi.py
	new file:   mysite/settings.py
	new file:   mysite/urls.py
	new file:   mysite/wsgi.py
	new file:   requirements.txt
	new file:   working_steps.py


(18)
(eds) MK:edsystems purohit$ git commit -m "initial commit"
[master (root-commit) 49b36ab] initial commit
 9 files changed, 324 insertions(+)
 create mode 100644 .gitignore
 create mode 100755 manage.py
 create mode 100644 mysite/__init__.py
 create mode 100644 mysite/asgi.py
 create mode 100644 mysite/settings.py
 create mode 100644 mysite/urls.py
 create mode 100644 mysite/wsgi.py
 create mode 100644 requirements.txt
 create mode 100644 working_steps.py
(eds) MK:edsystems purohit$ 



(19)
In the browser, login to github.com.
We already have an account on github with the user name mkp1511.
Create a new repository on github with the name 'eds'. 
Leave the "initialize with a README" checkbox unchecked, leave the .gitignore option blank (we've done that manually) 
and leave the License as None.


(20) Push the repository through terminal
(eds) MK:edsystems purohit$ git remote add origin https://github.com/mkp1511/eds.git
(eds) MK:edsystems purohit$ git push -u origin master
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 4 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 4.26 KiB | 2.13 MiB/s, done.
Total 12 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/mkp1511/eds.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
(eds) MK:edsystems purohit$ 



Static files include stuff like CSS, JavaScript and images that you may want to serve alongside your site. 
Django is very opinionated about how you should include your static files.
For now, let's add/edit some lines in the settings.py file at the end so that it looks like this.


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "mysite/assets")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


STATIC_URL = '/static/'
This line tells Django to append static to the base url (in our case localhost:8000) when searching for static files. 

In Django, you could have a static folder almost anywhere you want. You can even have more than one static folder 
e.g. one in each app. However, to keep things simple, We will use just one static folder in the root of our project folder. 


STATICFILES_DIRS = [os.path.join(BASE_DIR, "mysite/assets")]
The STATICFILES_DIRS tells Django where to look for static files that are not tied to a particular app. 
In this case, we just told Django to also look for static files in a folder called assets in our mysite folder, 
not just in our apps.

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
Django also provides a mechanism for collecting static files into one place so that they can be served easily. 
Using the collectstatic command, Django looks for all static files in your apps and collects them wherever you told it to, 
i.e. the STATIC_ROOT. In our case, we are telling Django that when we run python manage.py collectstatic, 
gather all static files into a folder called staticfiles in our project root directory. 
This feature is very handy for serving static files, especially in production settings.

Inside this folder is where we will have any custom CSS and JS we choose to write. On that note, 
let's add two folders inside the static folder to hold our files, one called css and the other called js. 
Inside css, create a file called main.css. Add a main.js in the js folder as well. 
Your static folder should now look like this: