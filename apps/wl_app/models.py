# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if 'name' in postData:
            if len(postData['name']) < 3:
                errors["name"] = "name must be at least 3 characters"
        if len(postData['username']) < 3:
            errors["username"] = "username must be at least 3 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password must be at least 8 characters"
        if 'datehired' in postData:
            if len(postData['datehired']) < 1:
                errors["password"] = "please enter your hire date"

        return errors

# class TripManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['destination']) < 1:
#                 errors["destination"] = "destination in blank, please add a destination"
#         if len(postData['description']) < 1:
#             errors["description"] = "description in blank, please add a description"
#         if len(postData['TravelDateFrom']) < 1:
#             errors["TravelDateFrom"] = "TravelDateFrom is blank, please add TravelDateFrom"
#         if len(postData['TravelDateTo']) < 1:
#             errors["TravelDateTo"] = "TravelDateTo is blank, please add a TravelDateTo"
#         if len(postData['TravelDateTo']) > 0 and len(postData['TravelDateFrom']) > 0:
#             if postData['TravelDateFrom'] <= str(timezone.now().date()):
#                 errors["TravelDateFrom"] = "TravelDateFrom must be in the future"
#             if postData['TravelDateTo'] <= str(timezone.now().date()):
#                 errors["TravelDateTo"] = "TravelDateTo must be in the future"
#             if postData['TravelDateFrom'] >= postData['TravelDateTo']:
#                 errors["TravelDateFrom"] = "TravelDateFrom must be before TravelDateTo"
#         return errors
        
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
         return self.name

class ItemList(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name = 'users') #added, a user can have many tripscheudles.
    # objects = ItemManager()

class Follow(models.Model): 
    item = models.ForeignKey(ItemList, related_name = 'users')
    follower= models.ForeignKey(User, related_name = 'items')
