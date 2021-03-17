# Pic Uploader using Django

This is a simple photo repository website built with Django and Postgres. User is able to add a picture along with a name, this can also be edited later or deleted.

## How to run
1. Set up a Postgres database with this information

    Name: PicUploader
  
    User: postgres
  
    Password: 123
  
    host: localhost
  
    port: 5432
    
 1. Make sure you have Django
 1. Create a virtual env
 
     ` $ python -m venv env_name`
     
     ` $ env_name\Scripts\activate`
 
 1. You might also need to install these two:
      
      `$ pip install psycopg2`
      
      `$ python -m pip install Pillow`
 
 1. Finally run the server:
 
      `$ python manage.py runserver`
      
1. You can go to the http address in your web browser of choice
 

## How to use
- Your photo repository should be empty at first
- You can upload pictures right at the top in the Upload Form
- Once you add pictures to the repository you are able to edit the name or picture
- Inside the edit form you can also delete the picture or if you changed your mind, click the `cancel` button
 

## Learning Outcomes
- Got familiarized and learned the basics of Django
- Learned how to use python along with HTML to build a website
- Familiarized with PostgreSQL


