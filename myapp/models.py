from audioop import maxpp
import email
from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.
STATE_CHOICE=(
    ('Tikapur','Tikapur'),
    ('kathmandu','kathmandu'),
    ('Pokhara','Pokhara'),
    ('Jhapa','Jhapa'),
    ('Ilam','Ilam'),
    ('Achham','Achham'),
    ('Npljung','Npljung'),
    ('Bardia','Bardia'),
)

class Resume(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=50)
    locality=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE, max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)
