vmgui
=====

vmchecker GUI

install
-------

    ````shell
    # python
    $ sudo apt-get install python2.7
    $ sudo easy_install pip
    $ sudo pip install virtualenv

    # web server
    $ git clone git@github.com:aismail/vmgui.git
    $ cd vmgui
    $ mkvirtualenv vmgui
    $ pip install -r install/requirements.txt

    # sqlite database
    $ cp install/dump/vmc_db vmc_backend

    # TODO instructions to link static content to django
    ````

run
---

    ````shell
    $ cd vmgui
    $ python manage.py run_gunicorn
    ````
