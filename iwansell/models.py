# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
import pytz

class Campus(models.Model):
    campus = models.CharField(max_length=100, default="Federal University of Technology Minna")
    campus_code = models.CharField(max_length = 10, default="FUTminna")

    def __str__(self):
        return self.campus_code

class Account(models.Model):
    email = models.EmailField(default="iwansell@gmail.com")
    password = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    phone = models.CharField(max_length=11)
    display_pic = models.FileField(default='anon.png')
    campus = models.ForeignKey(Campus,default="1")
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=50)
    date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['date']

    def __str__(self):
         return self.name


class Product(models.Model):
    account = models.ForeignKey(Account)
    category = models.ForeignKey(Category)
    campus = models.ForeignKey(Campus, default=1)
    description = models.TextField()
    product_name = models.CharField(max_length=100)
    product_image = models.FileField(default='product.png')
    starting_price = models.CharField(max_length=100)
    sold = models.BooleanField(default = False)
    removed = models.BooleanField(default = False)
    date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
         return self.product_name


class Media(models.Model):
    product = models.ForeignKey(Product)
    image = models.FileField()
    video = models.FileField()


class Sponsored(models.Model):
    campus = models.ForeignKey(Campus, default=1)
    product_image = models.FileField(default='product.png')
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
         return 'succesful'


class Trending(models.Model):
    campus = models.ForeignKey(Campus, default=1)
    category = models.ForeignKey(Category)
    product_image = models.FileField(default='product.png')
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
         return 'succesful'




class ProductView(models.Model):
    product = models.ForeignKey(Product)
    views = models.IntegerField()

    def __str__(self):
         return self.views


class RecentView(models.Model):

    product = models.ForeignKey(Product)
    account = models.ForeignKey(Account)

    def __str__(self):
         return self.product


class Feedback(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    feed = models.TextField()

    def __str__(self):
         return self.feed

class ForgotPassword(models.Model):
    email = models.EmailField()
    reset_code = models.CharField(default = '123579', max_length = 30)
    date = models.DateTimeField(default = timezone.now)


class EHaggler(models.Model):
    account_1 = models.ForeignKey(Account)
    account_2 = models.IntegerField()
    delete_for_1 = models.BooleanField(default=False)
    delete_for_2 = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)


class Messenger(models.Model):
    ehaggler = models.ForeignKey(EHaggler)
    messenger = models.ForeignKey(Account)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.message

    class Meta:
        ordering = ['date']


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length = 100)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name

    


class EShop(models.Model):
    account = models.ForeignKey(Account)
    campus = models.ForeignKey(Campus, default=1)
    name = models.CharField(max_length=20)
    catch_board = models.FileField()
    date = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.name


class EShopProduct(models.Model):
    eshop = models.ForeignKey(EShop)
    product = models.ForeignKey(Product)
    subcategory = models.ForeignKey(SubCategory)
    date = models.DateTimeField(default = timezone.now)

     
    class Meta:
        ordering = ['subcategory']


class FavoriteProduct(models.Model):
    account = models.ForeignKey(Account)
    product = models.ForeignKey(Product)
    date = models.DateTimeField(default = timezone.now)
    


class FavoriteClient(models.Model):
    account = models.ForeignKey(Account)
    client = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)


class FavoriteEShop(models.Model):
    account = models.ForeignKey(Account)
    eshop = models.ForeignKey(EShop)
    date = models.DateTimeField(default = timezone.now)

class RateReview(models.Model):
    account = models.ForeignKey(Account)
    rating = models.IntegerField()
    review = models.CharField(max_length= 150)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.review


class ClientRateReview(models.Model):
    ratereview = models.ForeignKey(RateReview)
    account = models.ForeignKey(Account)


class EShopRateReview(models.Model):
    ratereview = models.ForeignKey(RateReview)
    eshop = models.ForeignKey(EShop)


