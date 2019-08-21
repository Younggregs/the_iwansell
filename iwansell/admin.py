# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Listing, Channel, Thread, Comment, Reply, Account,Category, Media, Product, Campus,EShopCategory, EShop, Sponsored, Trending, Messenger,EHaggler, Blog, SubCategory, PaymentMethod
from django.contrib import admin

# Register your models here.
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Campus)
admin.site.register(Sponsored)
admin.site.register(Trending)
admin.site.register(Messenger)
admin.site.register(EHaggler)
admin.site.register(SubCategory)
admin.site.register(Media)
admin.site.register(EShop)
admin.site.register(Blog)
admin.site.register(EShopCategory)
admin.site.register(PaymentMethod)
admin.site.register(Listing)
admin.site.register(Channel)
admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Reply)
