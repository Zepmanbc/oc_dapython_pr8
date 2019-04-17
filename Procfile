release: python purbeurre/manage.py makemigrations
release: python purbeurre/manage.py migrate
web: gunicorn purbeurre.wsgi --chdir purbeurre/ --log-file -