# coding: utf-8
"""
vCard db models description
"""

from django.db import models


class Card(models.Model):
    """Card data"""
    # names, ;-separated (FN)
    family_name = models.CharField(
        max_length=200,
    )
    # from vCard (N)
    display_name = models.CharField(
        max_length=200,
        #required=False,
    )
    # birth date, in format YYYY-MM-DD
    bday = models.CharField(
        max_length=12,
        #required=False,
    )
    # 1.6 does not support TextField?
    vdata = models.TextField(
        #required=True,
    )
