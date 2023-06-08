from django.db import models

# Create your models here.
class Job(models.Model):
   
    # Image 
    image = models.ImageField( upload_to = 'images/' )
    
    #Summary
    summary = models.CharField( max_length = 2000 ) 

    #name

    name = models.CharField( max_length = 50 , blank=True , null=True)

    #images

    image1 = models.ImageField( upload_to = 'images/' , blank=True)
    image2 = models.ImageField( upload_to = 'images/' , blank=True)
    image3 = models.ImageField( upload_to = 'images/' , blank=True)


    def __str__(self):
        return self.summary

class CV(models.Model):
    file = models.FileField(upload_to = 'images/')
    filename = models.CharField(max_length=50)