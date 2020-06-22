from django.db import models
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm
from django.urls import reverse
from django import forms

Branch_choices = [
        ('IT','Information Technology'),
        ('CE','Computer'),
        ('EC','Electronics and Communication'),
        ('IC','Intrumantation and Control'),
        ('MET','Metallurgy'),
        ('BM', 'Bio-Medical')
    ]

Year_choices = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
]

class Donate(models.Model):
    
    owner = models.ForeignKey(User, related_name='books',default=None,on_delete=models.PROTECT)
    Branch = models.CharField(choices = Branch_choices,default='IT', max_length=6)
    Year = models.CharField(choices = Year_choices,default='1',max_length=4)
    Subject =  models.CharField(max_length=70,default=None)
    Publication =  models.CharField(max_length=70,default=None)   
    Author =  models.CharField(max_length=70, default=None)   
    Subject_code =  models.IntegerField(default=None)   
    Image = models.ImageField( blank=False ,upload_to='pics/',default="10", height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.Subject
    
    def get_absolute_url(self,id):
        return reverse("book_details", kwargs={"id":self.id})
