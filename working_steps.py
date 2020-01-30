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
