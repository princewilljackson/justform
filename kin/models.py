from django.db import models

# Create your models here.
    

RELATIONSHIP = (
    ('father', 'Father'),
    ('mother', 'Mother'),
    ('husband', 'Husband'),
    ('wife', 'Wife'),
    ('son', 'Son'),
    ('daughter', 'Daughter'),
)
class UserData(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Please_upload_valid_ID_front_view = models.FileField(upload_to='documents/')
    Please_upload_valid_ID_back_view = models.FileField(upload_to='documents/')
    relationship_with_Mr_Fred_Swanson = models.CharField(max_length=8, choices=RELATIONSHIP)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    SSN = models.CharField(max_length=10)
    Current_Address = models.TextField()