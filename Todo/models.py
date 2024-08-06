from django.db import models

# Create your models here.


class Students(models.Model): 
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100, blank=True)
    enrolled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.first_name
    
    class Meta: 
        verbose_name = 'Students'
        verbose_name_plural = 'Students'