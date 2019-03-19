from django.contrib.auth.models import User
import datetime as dt
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import numpy as np


class Profile(models.Model):
    """
    Class that contains Profile details
    """
    profile_pic = models.ImageField(upload_to='images/', blank=True)
    bio = models.TextField()
    contact = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()

    @classmethod
    def get_by_id(cls, user_id):
        profile = Profile.objects.get(user_id=user_id)
        return profile

    def __str__(self):
        return self.bio


class Project(models.Model):
    """
    Class that contains Project details
    """
    title = models.CharField(max_length=20)
    landing_page = models.ImageField(upload_to='images/')
    description = models.TextField()
    link = models.URLField(max_length=100)
    rating = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_pro(self):
        self.save()

    def del_pro(self):
        self.delete()

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_pro_by_id(cls, id):
        pro = Project.objects.get(id=id)
        return pro

    @classmethod
    def get_pro_by_user(cls, id):
        project = Project.objects.filter(user_id=id).all()
        return project

    def average_design(self):
        all_ratings = list(
            map(lambda x: x.rating, self.designrating_set.all()))
        return np.mean(all_ratings)

    def average_usability(self):
        all_ratings = list(
            map(lambda x: x.rating, self.usabilityrating_set.all()))
        return np.mean(all_ratings)

    def average_content(self):
        all_ratings = list(
            map(lambda x: x.rating, self.contentrating_set.all()))
        return np.mean(all_ratings)

    def __str__(self):
        return self.title


class DesignRating(models.Model):
    RATING_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
                      (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class ContentRating(models.Model):
    RATING_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
                      (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class UsabilityRating(models.Model):
    RATING_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
                      (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
