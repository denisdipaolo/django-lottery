# django-lottery

A (simple) lottery web application in django

## Python requirements

* Django
* django-bootstrap3
* Unipath

Contained in requirements.txt

## Get it running with the development server

Default config makes use of sqlite3 as database:

To get it up and running, run from the Lottery directory:

``` python
python manage.py migrate
python manage.py runserver
```

## Overview

Users can sign up to the platform to access to lottery games and partecipate to extractions.

Lottery games are created by admin users from the admin django panel.


### Draw winners

Command to draw winners

``` python
python manage.py drawwinners
```

Cheers!