cancer-lighthouse
=================

Website of resources where people with cancer can connect

Setup
=====

* In top level of cancer-lightouse, create virtual environment:
```bash
  virtualenv env
```

* Start virtualenv
```bash
  source env/bin/activate
```

* Install django
```bash
  pip install git+https://github.com/django/django.git
```
  
* Install django bootstrap
```
  pip install git+https://github.com/dyve/django-bootstrap3.git
``` 

To run:
=======

* Within lighthouse directory:
```bash
  ./manage.py runserver
```

* To view it in broswer, go to localhost:8000

