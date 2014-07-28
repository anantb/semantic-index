### Semantic-Index Installation Instruction

#### setup environment

* install postgres


#### install required python packages
* `pip install django`
* `pip install psycopg2`
* `pip install stemming`


#### download semantic-index
* `git clone git@github.com:abhardwaj/semantic-index.git`


#### make configuration changes

* setup postgres database
* create database nlp
* install schema
`python manage.py syncdb`


#### running in development mode

* run semantic-index server
`python manage.py runserver`


