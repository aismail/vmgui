vmgui
=====

vmchecker GUI

install
-------

````shell
# install python and virtualenv.
$ sudo apt-get install python2.7
$ sudo easy_install pip
$ sudo pip install virtualenv

# get the code and create an env for it.
$ git clone git@github.com:aismail/vmgui.git
$ cd vmgui
$ mkvirtualenv vmgui
$ pip install -r install/requirements.txt

# populate database with test data.
$ python manage.py populate_db

# start the python server
$ python manage.py run_gunicorn

# serve static content through nginx
$ sudo apt-get install nginx
# TODO add configuration to serve the static content, admin and api.
````
