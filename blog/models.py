from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to="event_images")    

    def __str__(self):
        return self.title
    
    def get_summary(self): # text parametrini faqat 70 belgisini chiqar func
        return self.text[:70]