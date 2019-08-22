# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django_random_queryset import RandomManager
import pytz





class Campus(models.Model):
    campus = models.CharField(max_length=100, default="Federal University of Technology Minna")
    campus_code = models.CharField(max_length = 10, default="FUTminna")

    def __str__(self):
        return self.campus_code









class Account(models.Model):
    email = models.EmailField(default="iwansell@gmail.com")
    password = models.CharField(max_length = 150)
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    phone = models.CharField(max_length=14)
    display_pic = models.FileField(default='anon.png')
    campus = models.ForeignKey(Campus, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.firstname + ' ' + self.lastname











class AlternatePhone(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14)

    def __str__(self):
        return self.phone1 + ' ' + self.phone2









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
    product_name = models.CharField(max_length=150)
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

    
    class Meta:
        ordering = ['-date']











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












class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length = 30)







class Transaction(models.Model):
    seller = models.ForeignKey(Account, on_delete=models.CASCADE)
    buyer = models.IntegerField(default = 0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    agreed_price = models.CharField(max_length= 10)
    quantity = models.IntegerField()
    token = models.CharField(max_length = 7)
    status = models.BooleanField(default = False)
    date = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return 'transaction'

    class Meta:
        ordering = ['date']













class Sold(models.Model):
    product_name = models.CharField(max_length= 150)
    frequency = models.IntegerField(default = 1)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return product_name + ': ' + frequency

    class Meta:
        ordering = ['-frequency']













class NotFound(models.Model):
    product_name = models.CharField(max_length= 150)
    frequency = models.IntegerField(default = 1)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return product_name + ': ' + frequency

    class Meta:
        ordering = ['-frequency']













class TopSearched(models.Model):
    product_name = models.CharField(max_length= 150)
    frequency = models.IntegerField(default = 1)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return product_name + ': ' + frequency

    class Meta:
        ordering = ['-frequency']
















class TopForSell(models.Model):
    product_name = models.CharField(max_length= 150)
    frequency = models.IntegerField(default = 1)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return product_name + ': ' + frequency

    class Meta:
        ordering = ['-frequency']





###### New ##########

class Listing(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    product_name = models.CharField(max_length= 200)
    product_description = models.TextField()
    product_image = models.FileField()
    budget = models.CharField(max_length=100)
    success = models.BooleanField(default = False)
    status = models.BooleanField(default = False)
    date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
         return self.product_name













class Channel(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    channel = models.CharField(max_length= 200)
    catch = models.CharField(max_length = 100)
    logo = models.FileField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.channel












class Following(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-date']












class Thread(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=4)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length= 200)
    thread = models.TextField()
    media = models.FileField()
    date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.thread













class ThreadVote(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
         return self.upvote + ' ' + self.downvote
    












class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.comment
    
    class Meta:
        ordering = ['-date']
        











class CommentVote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.vote













class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    reply = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.reply

    
    class Meta:
        ordering = ['-date']
        








class ReplyVote(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)











###### Reply1
class Reply1(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    reply_t = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.reply

    
    class Meta:
        ordering = ['-date']
        









class Reply1Vote(models.Model):
    reply1 = models.ForeignKey(Reply1, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)












######## Reply2 #######
class Reply2(models.Model):
    reply1 = models.ForeignKey(Reply1, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    reply = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.reply

    
    class Meta:
        ordering = ['-date']
        












class Reply2Vote(models.Model):
    reply2 = models.ForeignKey(Reply2, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)


















####### Reply3
class Reply3(models.Model):
    reply2 = models.ForeignKey(Reply2, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    reply = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.reply

    
    class Meta:
        ordering = ['-date']
        

class Reply3Vote(models.Model):
    reply3 = models.ForeignKey(Reply3, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)


















######Reply4
class Reply4(models.Model):
    reply3 = models.ForeignKey(Reply3, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    reply = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.reply

    
    class Meta:
        ordering = ['-date']
        










class Reply4Vote(models.Model):
    reply4 = models.ForeignKey(Reply4, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)










    






    




    










    









