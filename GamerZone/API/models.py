from django.db import models
from django.conf import settings

def upload_update_image(instance, filename):
    return "updates/{filename}".format(filename=filename)

class Game(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    system_requirements = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=upload_update_image, blank =True, null= True)
    release_date = models.DateTimeField(null=True,blank=True)
    digital = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title or ""