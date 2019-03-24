# Créez une plateforme pour amateurs de Nutella

## 1 - Plannification du projet (6h30)

[Dépot Github](https://github.com/Zepmanbc/oc_dapython_pr8)

[Tableau Trello](https://trello.com/invite/b/HjxFQIEN/e531e67f68bfe12dcc2c9b96dd546097/ocdapythonpr8)

[Analyse fonctionnelle](https://github.com/Zepmanbc/oc_dapython_pr8/blob/master/doc/analyse_fonctionnelle.md)

## 2 - Création d'un nouveau projet Django (1h)

création d'un environnement virtuel avec pipenv puis installation du packet django 2.1.7

Création du projet

    django-admin startproject purbeurre
    cd purbeurre
    manage.py startapp

création de variables d'environnement
    .env
        ENV=DEV
        SECRET_KEY= [SECRETKEY]
        DB_NAME=purbeurre
        DB_USER=root
        DB_PASSWORD=root

Modification du fichier de configuration

* Langue et fuseau horaire
* configuration PROD/DEV
* ajout de la fonction `get_env_variable()`
* configuration de la base de donnée

Création des dossiers static et templates

        .
        └── purbeurre
           ├── manage.py
           ├── products
           │   ├── __init__.py
           │   ├── admin.py
           │   ├── apps.py
           │   ├── migrations
           │   │   └── __init__.py
           │   ├── models.py
           │   ├── static
           │   │   └── products
           │   ├── templates
           │   │   └── products
           │   ├── tests.py
           │   └── views.py
           └── purbeurre
               ├── __init__.py
               ├── settings.py
               ├── urls.py
               └── wsgi.py


## 3 - Mise en place du Front

découpage du front

## 4 - Authentification

réalisation du package Authentication

## 5 - Products

réalisation du package Products

## 6 - Mise en ligne

Mise en place de Travis, Coverage et HEroku