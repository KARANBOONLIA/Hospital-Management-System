from django.db import models
from django.urls import reverse
class Patient(models.Model):
    pat_name=models.CharField(max_length=64 , default='default')
    pat_code = models.CharField(max_length=4)
    pat_illness = models.CharField(max_length=64)

    def get_absolute_url(self):         #returns to site mentioned below after use of create view or any view
        return reverse('indexOFpats')

class Doc(models.Model):

    name=models.CharField(max_length=64)
    type=models.CharField(max_length=64)
    all_pats=models.ManyToManyField(Patient , blank=True , related_name='all_pats_rel')
