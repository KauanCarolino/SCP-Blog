from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=50)
    item_number = models.CharField(max_length=50)
    name_SCP = models.CharField(max_length=50)
    image = models.ImageField(upload_to='scpImage/cover/%Y/%m/%d/', blank=True, default='')
    resume = models.CharField(max_length=50)
    special_containment_procedures = models.TextField()
    description = models.TextField()
    addendum =  models.TextField()
    #administration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    