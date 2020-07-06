from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Written(models.Model):
    # written_by=models.ForeignKey(User,on_delete=models.CASCADE,default='User')
    content=models.CharField(max_length=50,default='ABC')
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering=['-date_added']
    
    def get_absolute_url(self):
        
        return reverse('index', kwargs={'pk': self.pk})