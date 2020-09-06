from django.db import models

# Create your models here.
class InstalledAppsModel(models.Model):
    app_name = models.CharField(max_length=60)
    app_location = models.CharField(max_length=100)
    app_shorttext = models.TextField()
    
    def __str__(self):
        return self.app_name

    def get_absolute_url(self):
        return ('View APP', None, {'app_location':self.app_location})
    

        