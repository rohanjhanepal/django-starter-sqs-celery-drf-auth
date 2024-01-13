

1. Before installing requirements, run command:
`sudo apt-get install libcurl4-openssl-dev libssl-dev`


2. To run project and celery use following:

    make migrations before running:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
    Now to run, use first one, and second one to start celery:
    - `python manage.py runserver`
    - `celery --app=LabelWebApp.celery worker --loglevel=info --concurrency 2`


