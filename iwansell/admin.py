# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Account,Category, Media, Product, Campus, Sponsored, Trending, Messenger,EHaggler, SubCategory
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