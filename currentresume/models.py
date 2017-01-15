from django.db import models

class Resume(models.Model):
    '''
    Model to store a simple resume
    '''
    resume_body = models.CharField(max_length=500, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    