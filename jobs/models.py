from django.db import models

class Job(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.title
