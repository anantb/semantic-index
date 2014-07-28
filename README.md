### Semantic-Index Installation Instruction

#### setup environment

* install required linux packages
* sudo apt-get install postgresql


#### install required python packages
pip install django
pip install psycopg2
pip install stemming


#### download semantic-index
git clone git@github.com:abhardwaj/semantic-index.git


#### make configuration changes

edit django configuration settings
vi server/settings.py 

setup postgres database
psql -U postgres -W -h localhost
create database nlp

 install schema
cd src/
python manage.py syncdb


#### running in development mode

run semantic-index server
python manage.py runserver


