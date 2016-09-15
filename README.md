Changing the structure of entries is done in models.py. Make the changes to relevant fields, save the file, and then make new migrations from the command line. If adding a new field to an existing model, you will need to make sure that it is nullable by adding the tag "null=True" at the end, or it will not function with the existing entries.

To deploy to a Heroku instance, refer to this documentation:

https://devcenter.heroku.com/articles/deploying-python

##WRITE VENV GUIDE

Simply install dependencies using pip and the provided requirements.txt file, then run the following commands:

'''git add .
git commit -m "Added a Procfile."
heroku login'''

Enter your login information, then:

'''heroku create
git push heroku master'''

Once that is complete, you can open your website by typing
'''heroku open'''