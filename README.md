### How to run the app ?
 - virtualenv -p python3 myenv --no-site-packages
 - source activate myenv
 - pip install -r requirements.txt
  - python manage.py runserver
 
### Maintaining requirements.txt file ( register packages based on imports )
 - pipreqs . --force
