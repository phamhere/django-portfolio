from django.db import models


'''Sets up a table to be migrated to db.sqlite3 after registering app in
porfolio/settings.py'''


class Jobs(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
