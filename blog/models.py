from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # name displayed in admin page
    def __str__(self):
        return self.title

    # functions to get better properties of class when called in templates
    def summary(self):
        return self.body[:150]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
