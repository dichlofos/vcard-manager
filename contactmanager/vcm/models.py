from django.db import models


class Contact(models.Model):
    # names, ;-separated
    family_name = models.CharField(max_length=200)
    # from vCard
    display_name = models.CharField(max_length=200)
    # birth date, in format YYYY-MM-DD
    bday = models.CharField(max_length=12)
    email = models.CharField(max_length=64)
    tel_mobile = models.CharField(max_length=20)
    tel_work = models.CharField(max_length=20)
    tel_home = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

