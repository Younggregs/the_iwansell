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
    password = models.CharField(max_length = 250)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    phone = models.CharField(max_length=11)
    display_pic = models.FileField(default='anon.png')
    campus = models.ForeignKey(Campus, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.phone


class Category(models.Model):
    name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=50)
    image = models.FileField(default='anon.png')
    icon = models.FileField(default='anon.png')
    date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['name']

    def __str__(self):
         return self.name




class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    image = models.FileField(default='anon.png')
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']






class Product(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, default=1, on_delete=models.CASCADE)
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField()
    video = models.FileField()


class Sponsored(models.Model):
    campus = models.ForeignKey(Campus, default=1, on_delete=models.CASCADE)
    product_image = models.FileField(default='product.png')
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
         return 'succesful'


class Trending(models.Model):
    campus = models.ForeignKey(Campus, default=1, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.FileField(default='product.png')
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
         return 'succesful'




class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    views = models.IntegerField()

    def __str__(self):
         return self.views


class RecentView(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

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
    account_1 = models.ForeignKey(Account, on_delete=models.CASCADE)
    account_2 = models.IntegerField()
    delete_for_1 = models.BooleanField(default=False)
    delete_for_2 = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)


class Messenger(models.Model):
    ehaggler = models.ForeignKey(EHaggler, on_delete=models.CASCADE)
    messenger = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.message

    class Meta:
        ordering = ['date']



    


class EShop(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=150, default="")
    catch_board = models.FileField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name





class EShopCategory(models.Model):
    eshop = models.ForeignKey(EShop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return 'eShopCategory'





class EShopProduct(models.Model):
    eshop = models.ForeignKey(EShop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)

     
    class Meta:
        ordering = ['subcategory']


class FavoriteProduct(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    


class FavoriteClient(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    client = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)


class FavoriteEShop(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    eshop = models.ForeignKey(EShop, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)

class RateReview(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length= 150)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.review


class ClientRateReview(models.Model):
    ratereview = models.ForeignKey(RateReview, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class EShopRateReview(models.Model):
    ratereview = models.ForeignKey(RateReview, on_delete=models.CASCADE)
    eshop = models.ForeignKey(EShop, on_delete=models.CASCADE)




class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length= 150)
    blog_post = models.TextField()
    image = models.FileField(default='anon.png')
    blog_top = models.BooleanField(default= False)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']

    




