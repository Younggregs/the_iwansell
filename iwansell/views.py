from __future__ import unicode_literals
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password , make_password
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from django.core import serializers
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate , login
from django.http import JsonResponse
from django_random_queryset import RandomManager
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account, AlternatePhone, Category, Media, Product, Campus, Sponsored, EHaggler, Messenger, EShop, SubCategory, EShopProduct, EShopCategory, RateReview, ClientRateReview, EShopRateReview, FavoriteClient, FavoriteProduct, FavoriteEShop, Trending, Blog, ForgotPassword, PaymentMethod, Transaction, Sold, NotFound, TopSearched, TopForSell, Listing, Thread, Channel, Following, ThreadVote, Comment, Reply, Reply1, Reply2, Reply3, Reply4, CommentVote, ReplyVote, Reply1Vote, Reply2Vote, Reply3Vote, Reply4Vote
from .serializers import AccountSerializer, AlternatePhoneSerializer, AddAccountSerializer,SignInSerializer, CategorySerializer, ResultListSerializer,CampusSerializer, TrendSerializer, SponsoredSerializer, ProductSerializer,MessageSerializer, HaggleClientSerializer, EShopSerializer, EShopExistSerializer, SubCategorySerializer, ClientRRSerializer, EShopRRSerializer, ProductImagesSerializer, ProductVideoSerializer, EShopStoreSerializer, ForgotPasswordSerializer, ErrorCheckSerializer, SuccessCodeSerializer, FavoriteListClient, FavoriteListEShop, FavoriteListProduct, ProductSnippetSerializer, AboutEShopSerializer, BlogSerializer, EShopCategorySerializer, PaymentMethodSerializer, TransactionSerializer, BuyerSerializer, ReceiptSerializer, BusinessSerializer, ProductValuationSerializer, ListingSerializer, ListingProductSerializer, ThreadSerializer, CommentSerializer, ReplySerializer
import random
import string
import tweepy





















IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
VIDEO_FILE_TYPES = ['webm', 'mp4', 'ogg']



###########################
#TraffleDraw
###########################

consumer_key = 'gRsXuMIT59JtyIv2to5oc9ovS'
consumer_secret = '4e3jnVdmQLT7oce2lIbr1zU4wIE9FFXKFnK30SN98i62VVA0ap'





def send_retweet(access_token='743877620706779136-SUgvFOrU7NaXSlxiKvcTXDnJL3dYxot', access_secret='DbFYyUrJ3gwU8N7aCtzooibhvet7LyO99yXQfte1x4AjZ', tweet_id = 1141470601711955968) : 

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    rt_object = api.retweet(tweet_id)
    
    if rt_object: 

        return 117
    
    return False



def traffle_ticket_generator():

    return random.randint(999999, 999999999)




def get_tweet(access_token='743877620706779136-SUgvFOrU7NaXSlxiKvcTXDnJL3dYxot', access_secret='DbFYyUrJ3gwU8N7aCtzooibhvet7LyO99yXQfte1x4AjZ', tweet_id = 1141470601711955968):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    tweet = api.get_status(tweet_id)
    if tweet: 
        return tweet.text

    return False



def get_retweet(access_token='743877620706779136-SUgvFOrU7NaXSlxiKvcTXDnJL3dYxot', access_secret='DbFYyUrJ3gwU8N7aCtzooibhvet7LyO99yXQfte1x4AjZ', tweet_id = 1141470601711955968):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    tweet = api.get_status(tweet_id)
    if tweet: 
        return tweet.text

    return False
    





##########################################




















def index(request):

    return render(request ,'iwansell/index.html')












def reset_code_generator(size=16, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))















def token_code_generator(size=5, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))




















def get_account(request):

    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        phone = user.username


        account = Account.objects.get(phone=phone)

        return account

    else:
        
        return -1








































class AddAccount(APIView):

    def get(self,request):

        account = Account.objects.all()
        serializer = AddAccountSerializer(account, many=True)

        return Response(serializer.data)

    def post(self,request):


        serializer = AddAccountSerializer(data=request.data)
        if serializer.is_valid():


            firstname = serializer.data['firstname']
            lastname = serializer.data['lastname']
            phone = serializer.data['phone']
            campus = serializer.data['campus']
            campus = Campus.objects.get(id = campus)

            try:

                Account.objects.get(phone = phone)

                error_message = 'Oops an account with that username already exist'
                err = {
                    'error_message' : error_message
                }
                serializer = ErrorCheckSerializer( err, many=False)

                return Response(serializer.data)

            except:

                pass


            password = serializer.data['password']
            raw_password = password
            password = make_password(password)
            

            user = User()
            user.username = phone
            user.password = password
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            user = authenticate(username=phone, password=raw_password)


            if user is not None and user.is_active:

                login(request, user)

                account = Account()
                account.firstname = firstname
                account.lastname = lastname
                account.phone = phone
                account.campus = campus
                account.password = password
                account.save()

                code = 11

                success = {
                    'code' : code
                }

                serializer = SuccessCodeSerializer(success , many = False)

                return Response(serializer.data)

            else:

                error_message = 'Yay something broke, please try again '
                err = {
                    'error_message' : error_message
                }
                serializer = ErrorCheckSerializer( err, many=False)

                return Response(serializer.data)




        else :
            error_message = 'oooouu something went wrong, please try again '
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)














































class SignIn(APIView):

    def get(self,request):
        pass

    def post(self,request):

        username = request.POST.get("username","")
        password = request.POST.get("password","")


        user = authenticate(username=username, password=password)

        
        if user is not None and user.is_active:
            login(request, user)

            code = 11
            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'Ye! username and password did not match '
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)


        error_message = 'Invalid login, try again please '
        
        err = {
            'error_message' : error_message
        }
        serializer = ErrorCheckSerializer( err, many=False)

        return Response(serializer.data)
                
                







































class AccountDetail(APIView):

    def get(self,request,account_id):

        try:
            account = Account.objects.get(id=account_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        #account = Account.objects.all()
        serializer = AccountSerializer(account, many=False)

        return Response(serializer.data)


    def put(self,request,account_id):
        try:
            account = Account.objects.get(id=account_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,account_id):
        try:
            account = Account.objects.get(id=account_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


































class ResetPhone(APIView):

    def get(self, request):
        pass

    
    def post(self, request):
        
        account = get_account(request)

        if account:
            
            phone = request.POST.get("phone","")
            account.phone = phone
            account.save()

            code = 11

            success = {
            'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'Oops something went wrong, try again'
        
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)
                






























class ResetDP(APIView):

    def get(self, request):
        pass

    
    def post(self, request):
        

        display_pic = request.FILES.get("display_pic","")
        
        try: 
            account = get_account(request)
            account.display_pic = display_pic
            account.save()

            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        except: 

            error_message = 'Ye! something broke, please try again '
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)































class UpdatePassword(APIView):

    def get(self, request):
        pass

    
    def post(self, request):
        

        old_password = request.POST.get("old_password", "")
        new_password = request.POST.get("new_password","")
        confirm_password = request.POST.get("confirm_password","")

        if new_password == confirm_password:

            
            try:
                account = get_account(request)
                password = account.password

                if old_password == int(password):

                    account.password = make_password(new_password)
                    account.save()

                    user = User.objects.get(username = email)
                    user.password = make_password(new_password)
                    user.save()

                    code = 11

                    success = {
                        'code' : code
                    }

                    serializer = SuccessCodeSerializer(success, many = False)

                    return Response(serializer.data)

                
                else:

                    error_message = 'Invalid old password'

                    err = {
                        'error_message' : error_message
                    }

                    serializer = ErrorCheckSerializer(err, many=False)

                    return Response(serializer.data)


            except:

                error_message = 'Ye! something went wrong'

                err = {
                    'error_message' : error_message
                }

                serializer = ErrorCheckSerializer(err, many=False)

                return Response(serializer.data)

        else:

            error_message = 'Passwords do not match'

            err = {
                'error_message' : error_message
            }

            serializer = ErrorCheckSerializer(err, many=False)

            return Response(serializer.data)

        
       

        



























class IsLoggedIn(APIView):

    def get(self, request):

        signed_in = False

        try:
            account = get_account(request)
            signed_in = True

        except:

            pass
            

        return Response(signed_in)


    
    def post(self, request):

        pass

    





























class UpdateDP(APIView):

    def get(self, request):
        pass

    
    def post(self, request):
        

        display_pic = request.FILES.get("display_pic","")
        
        try: 
            account = get_account(request)
            account.display_pic = display_pic
            account.save()

            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        except: 

            error_message = 'Ye! something broke, please try again '
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)



































class UpdatePassword(APIView):

    def get(self, request):
        pass

    
    def post(self, request):
        
        try:
            account = get_account(request)
            old_password = request.POST.get("old_password","")
            new_password = request.POST.get("new_password","")
            confirm_password = request.POST.get("confirm_password","")

            if old_password == account.password:

                if new_password == confirm_password:

                    account.password = make_password(new_password)
                    account.save()

                    code = 11

                    success = {
                        'code' : code
                    }

                    serializer = SuccessCodeSerializer(success, many = False)

                    return Response(serializer.data)

                else:
                    error_message = 'Ooouuu! passwords did not match'
                    err = {
                        'error_message' : error_message
                    }
                    serializer = ErrorCheckSerializer( err, many=False)

                    return Response(serializer.data)

        except: 

            error_message = 'Ye! something broke, please try again '
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)


































class IsMyProfile(APIView):

    def get(self, request, profile_id):

        my_account = False

        try:
            account = get_account(request)
            account_id = account.id

            if account_id == int(profile_id) :
                my_account = True


        except:
            pass

        
        return Response(my_account)

    def post(self, request, profile_id):
        pass

































class MyAccountID(APIView):

    def get(self, request):

        try: 
            account = get_account(request)
            account_id = account.id

            return Response(account_id)

        except:
            pass

        return Response(1)


    def post(self, request):
        pass


































class IsMyEShop(APIView):

    def get(self, request, eshop_id):

        my_eshop = False

        try:
            account = get_account(request)
            eshop = EShop.objects.get(id = eshop_id)

            if account:
                if int(account.id) == eshop.account_id :
                    my_eshop = True
                


        except:
            pass
        

        return Response(my_eshop)
        
        


    
    def post(self, request, eshop_id):
        pass































class MyEShopID(APIView):

    def get(self, request):


        eshop_id = ''
        try:
            account = get_account(request)
            account_id = account.id

            eshop = EShop.objects.get(account_id = account_id)
            eshop_id = eshop.id
        except:
            pass


        return Response(eshop_id)
        
        


    
    def post(self, request, eshop_id):
        pass




































class CategoryView(APIView):

    def get(self,request):

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)

    def post(self,request):

        pass







































class RecentBlogPost(APIView):

    def get(self, request):
        
        try:
            blog = Blog.objects.all()[:9]

            serializer = BlogSerializer(blog, many=True)
            return Response(serializer.data)
        except:
            pass

        return Response(False)
    

    def post(self, request, blog_id):
        pass



























class BlogPost(APIView):

    def get(self, request, blog_id):
        
        try:
            blog = Blog.objects.get(id = blog_id)

            serializer = BlogSerializer(blog, many=False)
            return Response(serializer.data)
        except:
            pass

        return Response(False)
    

    def post(self, request, blog_id):
        pass























    


class BlogTop(APIView):

    def get(self, request):
        
        try:
            blog = Blog.objects.get(blog_top = True)

            serializer = BlogSerializer(blog, many=False)
            return Response(serializer.data)
        except:
            pass

        return Response(False)
    

    def post(self, request, blog_id):
        pass



























class CategoryBlog(APIView):

    def get(self, request, category_id):
        
        blog = Blog.objects.filter(category = category_id)

        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
    

    def post(self, request, blog_id):
        pass

































class BlogSnippet(APIView):

    def get(self, request):
        
        blog = Blog.objects.all()[:13]

        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
    

    def post(self, request, blog_id):
        pass



































class SubCategoryView(APIView):

    def get(self,request, category_id):

        subcategory = SubCategory.objects.filter( category_id = category_id )
        serializer = SubCategorySerializer(subcategory, many=True)

        return Response( serializer.data )

    def post(self,request, category_id):

        pass






























class SubCategoryMain(APIView):

    def get(self,request):

        subcategory = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategory, many=True)

        return Response( serializer.data )

    def post(self,request, category_id):

        pass



































class SubCategoryProduct(APIView):

    def get(self, request, campus_id, subcategory_id):

        try:
            if subcategory_id == '99':
                product = Product.objects.all()[:21]

            else:
                subcategory = SubCategory.objects.get(id = subcategory_id)
                category_id = subcategory.category_id
                product = Product.objects.filter(category_id = category_id)[:21]

            serializer = ProductSnippetSerializer(product, many=True)
            return Response( serializer.data )
        except:
            bug = []
            return Response(bug)

    def post(self,request, category_id):

        pass







































class SubCategoryIcon(APIView):

    def get(self, request):

        subcategory = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategory, many=True)

        return Response( serializer.data )

    
    def post(self, request):
        
        pass





































class CampusView(APIView):

    def get(self,request):

        campus = Campus.objects.all()
        serializer = CampusSerializer(campus, many=True)

        return Response(serializer.data)

    def post(self,request):

        pass




































class CampusSearch(APIView):

    def get(self, request):
        pass
        
    
    def post(self, request):
        
        key_word = request.POST.get("key_word","")

        campus = Campus.objects.filter(campus__icontains = key_word) | Campus.objects.filter(campus_code__icontains = key_word)
        serializer = CampusSerializer(campus, many=True)

        return Response(serializer.data)












































class CategoryProduct(APIView):

    def get(self, request, campus_id, category_id, show_more):

        if show_more == '1':
            if category_id == '99' :
                product = Product.objects.filter(campus_id = campus_id)[:9]

            else: 
                product = Product.objects.filter(campus_id = campus_id, category_id = category_id)[:9]

        else:
            if category_id == '99' :
                product = Product.objects.filter(campus_id = campus_id)[:21]

            else: 
                product = Product.objects.filter(campus_id = campus_id, category_id = category_id)[:21]
    
        serializer = ProductSnippetSerializer(product, many=True)
        return Response(serializer.data)


       

    
    def post(self, request):
        pass












































class NewProductView(APIView):

    def get(self,request, account_id):
        pass

    
    def post(self, request, account_id):
        

        category = request.POST.get("category","")
        description = request.POST.get("description","")
        product_name = request.POST.get("product_name","")
        #product_image = request.FILES.get("product_image","")
        starting_price = request.POST.get("starting_price","")
        media = request.FILES.getlist("files","")

        if True:
            account = Account.objects.get(id=account_id)
            campus_id = account.campus_id

            campus = Campus.objects.get(id = campus_id)

            category = Category.objects.get(id = category)
        

            newProduct = Product()
            newProduct.account = account
            newProduct.category = category
            newProduct.campus = campus
            newProduct.description = description
            newProduct.product_name = product_name
            #newProduct.product_image = product_image
            newProduct.starting_price = starting_price

           
            i = 0
            for m in media :

                if i == 0:
                    newProduct.product_image = m
                    newProduct.save()

                    i = i + 1
               

                else:
                    media_register = Media()
        
                    media_register.image = m
                    media_register.video = m

                    file_type = media_register.image.url.split('.')[-1]
                    file_type = file_type.lower()

                    if file_type in IMAGE_FILE_TYPES:

                        media_register.video = 0

                    else:

                        file_type = media_register.video.url.split('.')[-1]
                        file_type = file_type.lower()

                        if file_type in VIDEO_FILE_TYPES:

                            media_register.image = 0

                        else:

                            err_msg = 'Unsupported file format, file should be valid image, audio or/and video files'
                    

                    media_register.product = newProduct
                    media_register.save()

                    i = i + 1
            



            ## upForSell Products, business mode
            try :
                topForSell = TopForSell.objects.get(product_name = product_name)
                topForSell.frequency = topForSell.frequency + 1
                topForSell.save()

            except:
                topForSell = TopForSell()
                topForSell.product_name = product_name
                topForSell.save()


            code = newProduct.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)



















class NewListingView(APIView):

    def get(self,request, account_id):
        pass
    
    def post(self, request, account_id):
        
        category = request.POST.get("category","")
        description = request.POST.get("description","")
        product_name = request.POST.get("product_name","")
        #product_image = request.FILES.get("product_image","")
        budget = request.POST.get("budget","")
        media = request.FILES.getlist("files","")

        if True:
            account = Account.objects.get(id=account_id)
            campus_id = account.campus_id

            campus = Campus.objects.get(id = campus_id)

            category = Category.objects.get(id = category)
        

            newProduct = Listing()
            newProduct.account = account
            newProduct.category = category
            newProduct.campus = campus
            newProduct.product_description = description
            newProduct.product_name = product_name
            #newProduct.product_image = product_image
            newProduct.budget = budget

           
            i = 0
            for m in media :

                if i == 0:
                    newProduct.product_image = m
                    newProduct.save()

                    i = i + 1
               

                else:
                    pass


            code = account.campus_id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)
























class ListingView(APIView):

    def get(self, request, campus_id):
        
        buffer = Listing.objects.filter(campus_id = campus_id)

        listings = []

        for item in buffer:

                account_id = item.account_id
                account = Account.objects.get(id = account_id)
                phone = account.phone

                product_name = item.product_name
                product_image = item.product_image
                product_description = item.product_description
                budget = item.budget

                context_list = {
                    'product_name' : product_name,
                    'product_image' : product_image,
                    'product_description' : product_description,
                    'budget' : budget,
                    'phone' : phone
                }

                listings.append(context_list)


        serializer = ListingSerializer( listings, many=True)

        return Response(serializer.data)

    

    def post(self, request, campus_id):
        
        search_phrase = request.POST.get("listing", "")
        search_bucket = search_phrase.split()

        result_bucket = []

        for word in search_bucket :

            result =  Listing.objects.filter(product_name__icontains = word, campus_id = campus_id, status = False) | Listing.objects.filter(product_description__icontains = word, campus_id = campus_id, status = False) 
            result_bucket.append(result)
        

        listings = []
        for buffer in result_bucket :

            for item in buffer:

                account_id = item.account_id
                account = Account.objects.get(id = account_id)
                phone = account.phone

                product_name = item.product_name
                product_image = item.product_image
                product_description = item.product_description
                budget = item.budget

                context_list = {
                    'product_name' : product_name,
                    'product_image' : product_image,
                    'product_description' : product_description,
                    'budget' : budget,
                    'phone' : phone
                }

                listings.append(context_list)

        serializer = ListingSerializer( listings, many=True)

        return Response(serializer.data)



















class ListingProduct(APIView):

    def get(self, request):
        
        listing = []
        try:
            account = get_account(request)
            listing = Listing.objects.filter(account_id = 3, status=False)
        except:
            pass

        
        serializer = ListingProductSerializer( listing, many=True)

        return Response(serializer.data)

    
    def post(self, request):
        pass















class RemoveListing(APIView):

    def get(self, request, product_id, status):
        
        try:
            listing = Listing.objects.get(id = product_id)
            
            listing.status = True

            if status == '1':
                listing.success = True

            listing.save()

        except:
            pass

        return Response(True)

    
    def post(self, request, product_id, status):
        pass













class ListingCategory(APIView):

    def get(self, request, campus_id, category_id):
        
        if category_id == '99':
            buffer = Listing.objects.all()
        else:
            buffer = Listing.objects.filter(campus_id = campus_id, category_id = category_id)
        
        listings = []

        for item in buffer:

                account_id = item.account_id
                account = Account.objects.get(id = account_id)
                phone = account.phone

                product_name = item.product_name
                product_image = item.product_image
                product_description = item.product_description
                budget = item.budget

                context_list = {
                    'product_name' : product_name,
                    'product_image' : product_image,
                    'product_description' : product_description,
                    'budget' : budget,
                    'phone' : phone
                }

                listings.append(context_list)

        serializer = ListingSerializer( listings, many=True)

        return Response(serializer.data)

    

    def post(self, request, campus_id, category_id):
        pass





















class MediaUpload(APIView):

    def get(self, request, product_id):
        pass

    
    def post(self, request, product_id):
        

        media = request.FILES.getlist("files","")

        if True:
            product = Product.objects.get(id = product_id)


            i = 0
            for m in media :

                if i == 0:
                    product.product_image = m
                    product.save()

                    i = i + 1
               

                else:
                    media_register = Media()
        
                    media_register.image = m
                    media_register.video = m

                    file_type = media_register.image.url.split('.')[-1]
                    file_type = file_type.lower()

                    if file_type in IMAGE_FILE_TYPES:

                        media_register.video = 0

                    else:

                        file_type = media_register.video.url.split('.')[-1]
                        file_type = file_type.lower()

                        if file_type in VIDEO_FILE_TYPES:

                            media_register.image = 0

                        else:

                            err_msg = 'Unsupported file format, file should be valid image, audio or/and video files'
                    

                    media_register.product = product
                    media_register.save()

                    i = i + 1
            



            code = product.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong, please try again'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)



























        













class ProductList(APIView):

    def get(self, request):
        
        

        try: 
            account = get_account(request)
            account_id = account.id

            product = Product.objects.filter(account_id = account_id)

            register = []

            for buffer in product :

                product_id = buffer.id
                product_name = buffer.product_name
                product_image = buffer.product_image
                starting_price = buffer.starting_price

                context_list = {
                    'product_id': product_id,
                    'product_name': product_name,
                    'product_image' : product_image,
                    'starting_price' : starting_price,
                }   

                register.append(context_list)

            serializer = ResultListSerializer(register, many=True)

            return Response(serializer.data)

        except:
            pass


        return Response(False)


    
    def post(self, request):
        pass








































class EShopProductList(APIView):

    def get(self, request):
        
        email = 'dretzam@gmail.com'


        account = Account.objects.get(email = email)
        account_id = account.id

        eshop = EShop.objects.get(account_id = account_id)
        eshop_id = eshop.id

        eshop_product = EShopProduct.objects.filter(eshop_id = eshop_id)


        register = []

        for product in eshop_product:

            product_id = product.product_id

            item = Product.objects.get(id = product_id)
            
            product_name = item.product_name
            product_image = item.product_image
            starting_price = item.starting_price

            context_list = {
                'product_id': product_id,
                'product_name': product_name,
                'product_image' : product_image,
                'starting_price' : starting_price,
            }

            register.append(context_list)
            

            

        serializer = ResultListSerializer(register, many=True)

        return Response(serializer.data)


    
    def post(self, request):
        pass




































class Search(APIView):

    def get(self, request,campus_id, category_id):

        search_phrase = "Samsung s5 edge"
        search_bucket = search_phrase.split()

        results = []
        result_bucket = []

        for word in search_bucket :

            if category_id != '99' :

                buffer_result =  Product.objects.filter(product_name__icontains = word,category_id=category_id, campus_id = campus_id, sold = False) | Product.objects.filter(description__icontains = word, category_id=category_id, campus_id = campus_id, sold = False) 
                
            
            else:
             
                buffer_result = Product.objects.filter(product_name__icontains = word, campus_id = campus_id, sold = False) | Product.objects.filter(description__icontains = word, campus_id = campus_id, sold = False)
       

            result_bucket.append(buffer_result)

         

        for buffer in result_bucket :

            for item in buffer :
                

                product_id = item.id
                product_name = item.product_name
                product_image = item.product_image
                starting_price = item.starting_price

                context_list = {
                    'product_id': product_id,
                    'product_name': product_name,
                    'product_image' : product_image,
                    'starting_price' : starting_price,
                }

                results.append(context_list)

               

        serializer = ResultListSerializer(results, many=True)

        return Response(serializer.data)





    
    def post(self, request,campus_id, category_id):

        search_phrase = request.POST.get("search_phrase", "")
        search_bucket = search_phrase.split()

        results = []
        result_bucket_list = []

        for word in search_bucket :

            if category_id != '99' :

                buffer_result =  Product.objects.filter(product_name__icontains = word,category_id=category_id, campus_id = campus_id, sold = False) | Product.objects.filter(description__icontains = word, category_id=category_id, campus_id = campus_id, sold = False) 

            else:
             
                buffer_result = Product.objects.filter(product_name__icontains = word, campus_id = campus_id, sold = False) | Product.objects.filter(description__icontains = word, campus_id = campus_id, sold = False)
    
            result_bucket_list.append(buffer_result)

         

        for buffer in result_bucket_list :

            for item in buffer :

                product_id = item.id
                product_name = item.product_name
                product_image = item.product_image
                starting_price = item.starting_price

                context_list = {
                    'product_id': product_id,
                    'product_name': product_name,
                    'product_image' : product_image,
                    'starting_price' : starting_price,
                }

                results.append(context_list)

            

        ## Search Products, business mode
        try :
            top_searched = TopSearched.objects.get(product_name = search_phrase)
            top_searched.frequency = top_searched.frequency + 1
            top_searched.save()

        except:
            top_searched = TopSearched()
            top_searched.product_name = search_phrase
            top_searched.save()

        
        ## Not Found, business mode
        if results:
            pass
        
        else:

            try :
                not_found = NotFound.objects.get(product_name = search_phrase)
                not_found.frequency = not_found.frequency + 1
                not_found.save()

            except:
                not_found = NotFound()
                not_found.product_name = search_phrase
                not_found.save()
            

               

        serializer = ResultListSerializer(results, many=True)

        return Response(serializer.data)































class TrendingView(APIView):

    def get(self, request, campus_id, trending_url):

        try:
            category = Category.objects.get(url_name = trending_url)
            trending = Product.objects.filter(category_id = category.id, campus_id = campus_id)[:8] 

            serializer = TrendSerializer(trending, many=True)

            return Response(serializer.data)

        except:
            pass

        empty_array = []

        return Response(empty_array)

        

    def post(self, request, campus_id, category):
        pass


































class SponsoredView(APIView):

    def get(self, request, campus_id):

        sponsored = Sponsored.objects.filter(campus_id = campus_id)[:12]
        serializer = SponsoredSerializer(sponsored, many=True)

        return Response(serializer.data)

    def post(self, request, campus_id):
        pass





































class ProductView(APIView):

    def get(self, request, product_id):
        
        
        try :

            buffer_result = Product.objects.get(id = product_id)

            product_id = buffer_result.id
            product_name = buffer_result.product_name
            product_descrition = buffer_result.description
            product_image = buffer_result.product_image
            starting_price = buffer_result.starting_price

            account_id = buffer_result.account_id
            account = Account.objects.get(id=account_id)

            profile_id = account.id
            firstname = account.firstname
            lastname = account.lastname
            phone = account.phone
            display_pic = account.display_pic

            context_list = {
                'product_id': product_id,
                'product_name': product_name,
                'product_description' : product_descrition,
                'product_image' : product_image,
                'starting_price' : starting_price,
                'profile_id' : profile_id,
                'firstname' : firstname,
                'lastname' : lastname,
                'phone' : phone,
                'display_pic' : display_pic
            }

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)   

        serializer = ProductSerializer(context_list, many=False)

        return Response(serializer.data)

        

    def post(self, request, product_id):
         pass















































class ProductImages(APIView):

    def get(self, request, product_id ):
        
        product_images = Media.objects.filter(product_id = product_id)

        serializer = ProductImagesSerializer( product_images, many = True )

        return Response(serializer.data)

    def post(self, request, product_id ):
        pass






































class ProductVideo(APIView):

    def get(self, request, product_id):

        try :
            product_video = Media.objects.get(product_id = product_id)
            serializer = ProductVideoSerializer( product_video, many = False )

            return Response(serializer.data)
        except :
            empty_set = []
            return Response(empty_set)


    def post(self, request, product_id):
        pass





































class HaggleClients(APIView):

    def get(self, request):
        
        try:
            account = get_account(request)
            account_id = account.id

            chats = EHaggler.objects.filter(account_1_id = account_id) | EHaggler.objects.filter(account_2 = account_id)

            client_register = []
            if chats !=  0 :

                for client in chats:

                    client_buffer = []

                    if client.account_1_id == account_id :

                        account = Account.objects.get(id = client.account_2)
                        name = account.firstname + ' ' + account.lastname
                        client_id = account.id
                        haggle_id = client.id

                        client_buffer = {
                            'name' : name,
                            'client_id' : client_id,
                            'haggle_id' : haggle_id
                        }

                        client_register.append(client_buffer)

                    else:

                        account = Account.objects.get(id = client.account_1_id)
                        name = account.firstname + ' ' + account.lastname
                        client_id = account.id
                        haggle_id = client.id

                        client_buffer = {
                            'name' : name,
                            'client_id' : client_id,
                            'haggle_id' : haggle_id
                        }

                        client_register.append(client_buffer)


            else :
                pass
        
        except:
            pass


        serializer = HaggleClientSerializer(client_register, many=True)

        return Response(serializer.data)



    def post(self, request):
        pass



















































class NewHaggler(APIView):

    def get(self, request, client_id):

        try:

            account = get_account(request)
            account_id = account.id

            account_2 = Account.objects.get( id = client_id )

        except:

            error_message = 'Wrong turn'

            err = {
                'error_message' : error_message
            }

            serializer = ErrorCheckSerializer(err, many= False)

            return Response(serializer.data)


        is_chat = False

        try:
            chat_exist_1 = EHaggler.objects.get(account_1_id = client_id, account_2 = account_id)
            is_chat = True
        except:
            pass

        try:
            chat_exist_2 = EHaggler.objects.get(account_1_id = account_id, account_2 = client_id)
            is_chat = True
        except:
            pass

        if is_chat:

            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many= False)

            return Response(serializer.data)

        else:

            ehaggler = EHaggler()
            ehaggler.account_1 = account
            ehaggler.account_2 = client_id
            ehaggler.save()

            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many= False)

            return Response(serializer.data)



      
           
           

    
    def post(self, request, client_id):

        pass



















































class MessengerView(APIView):

    def get(self, request, client_id):
        
        
        try:
            account = get_account(request)
            account_id = account.id

            evaluator = 0
            try:

                chat_exist = EHaggler.objects.get(account_1 = client_id, account_2 = account_id)
                evaluator = 1

            except:
                pass

            try:
            
                chat_exist = EHaggler.objects.get(account_1 = account_id, account_2 = client_id)
                evaluator = 1

            except:
                pass
        

            haggle_register = [] 

            if evaluator == 1:
            
                try :
                    ehaggler = EHaggler.objects.get(account_1 = client_id, account_2 = account_id)
                    ehaggler_id = ehaggler.id
            
                except :

                    ehaggler = EHaggler.objects.get(account_1 = account_id, account_2 = client_id)
                    ehaggler_id = ehaggler.id


                messages = Messenger.objects.filter(ehaggler_id = ehaggler_id)

                for message in messages:

                    from_or_to = True

                    if int(message.messenger_id) == int(client_id):

                        msg = message.message
                        from_or_to = True

                        haggle_buffer = {
                            'msg' : msg,
                            'from_or_to' : from_or_to,
                        }

                        haggle_register.append(haggle_buffer)

                    else :

                        msg = message.message
                        from_or_to = False

                        haggle_buffer = {
                            'msg' : msg,
                            'from_or_to' : from_or_to,
                        }

                        haggle_register.append(haggle_buffer)

                 


            #messages_from = Messenger.objects.filter(ehaggler_id = ehaggler_id, messenger = client_id)
            #messages_to = Messenger.objects.filter(ehaggler_id = ehaggler_id, messenger = account_id)
        


        except :

           error_message = 'Oops something went wrong, mmhmm'
           err = {
               'error_message' : error_message
           }

           serializer = ErrorCheckSerializer(err, many= False)

           return Response(serializer.data)

        
        serializer = MessageSerializer(haggle_register, many=True)

        return Response(serializer.data)


    def post(self, request, client_id):
        pass











































class SendMessage(APIView):

    def get(self, request, client_id):
        pass

    def post(self, request, client_id):
        
        haggle_register = []

        try:
            account = get_account(request)
            account_id = account.id

            status = 0

            try :

                ehaggler = EHaggler.objects.get(account_2 = client_id, account_1_id = account_id)

                status = 1 

            except:
                pass

        
            if status == 0:
                try: 

                    ehaggler = EHaggler.objects.get(account_2 = account_id, account_1_id = client_id)
                    status = 1

                except:
                    pass



            msg = request.POST.get("message","")

       
            if msg:
                pass

            else:
                msg="Angel"

            messenger = Messenger()
            messenger.ehaggler = ehaggler
            messenger.message = msg
            messenger.messenger = account
            messenger.save()


            messages = Messenger.objects.filter(ehaggler_id = ehaggler.id)
            
 

            if True :
                for message in messages:

                    from_or_to = True

                    if message.messenger == client_id :

                        msg = message.message
                        from_or_to = True

                        haggle_buffer = {
                            'msg' : msg,
                            'from_or_to' : from_or_to,
                        }

                        haggle_register.append(haggle_buffer)

                    else :

                        msg = message.message
                        from_or_to = False

                        haggle_buffer = {
                            'msg' : msg,
                            'from_or_to' : from_or_to,
                        }

                        haggle_register.append(haggle_buffer)

                else:
                    pass

        except:
            pass
        
        serializer = MessageSerializer(haggle_register, many=True)

        return Response(serializer.data)


















































class UnreadMessages(APIView):

    def get(self, request):

        try:
            account = get_account(request)
            account_id = account.id
       
        
            unread_msg = EHaggler.objects.filter(account_1 = account_id) | EHaggler.objects.filter(account_2 = account_id)

            count = 0
            for msg in unread_msg :

                if Messenger.objects.filter(ehaggler_id = msg.id, messenger_id = account_id).exists:
                    pass

                else:

                    unread = Messenger.objects.filter(ehaggler_id = msg.id, seen = False).count

                    count += unread

        

            code = count

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)
             
        except:
            code = 0
            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)

        return Response(serializer.data)
        
        

    
    def post(self, request):
        pass





















































        

class NewEShop(APIView):

    def get(self, request):
        
        pass
       



    def post(self, request):

        try:
            account = get_account(request)
            account_id = account.id

            category = request.POST.getlist("category","")
            name = request.POST.get("eshop_name","")
            about = request.POST.get("about","")

            try:
                eshop_exist = EShop.objects.get(account_id = account_id)

                error_message = 'Oops looks like this account has an e-shop already'

                err = {
                    'error_message': error_message
                }

                serializer = ErrorCheckSerializer(err, many=False)

                return Response(serializer.data)

        
            except:
                pass


        
        
            try:
                eshop_name_exist = EShop.objects.get(name = name)

                error_message = 'Owww, this e-shop name has been taking already, try again, pls'

                err = {
                    'error_message': error_message
                }

                serializer = ErrorCheckSerializer(err, many=False)

                return Response(serializer.data)

        
            except:
                pass


            if True:

                eshop = EShop()
                eshop.account = account
                eshop.name = name
                eshop.about = about
                eshop.save()


                for id in category:
                    eshop_category = EShopCategory()
                    category_item = Category(id = id)
                    eshop_category.eshop = eshop 
                    eshop_category.category = category_item
                    eshop_category.save()


                code = eshop.id

                success = {
                    'code' : code
                }

                serializer = SuccessCodeSerializer(success, many=False)

                return Response(serializer.data)

            else:
                pass
       

            

        except:
            
            error_message = 'Ye, something went wrong, please try again'

            err = {
                'error_message': error_message
            }

            serializer = ErrorCheckSerializer(err, many=False)

            return Response(serializer.data)

















































class HaveEShop(APIView):

    def get(self, request):

        code = False

        try:
            account = get_account(request)
            account_id = account.id

            try :

                eshop = EShop.objects.get(account_id = account_id)
                code = True

            except:
                pass
        
        except:
            pass
        
        return Response(code)

        
    

    def post(self, request):
        pass


















































class EShopView(APIView):

    def get(self, request, eshop_id):
        
        try:

            eshop = EShop.objects.get(id = eshop_id)

        except:

            return Response(status=status.HTTP_404_NOT_FOUND)



        serializer = EShopSerializer(eshop, many = False)

        return Response(serializer.data)

        
    
    def post(self, request):
        pass


































class AboutEShop(APIView):

    def get(self, request, eshop_id):

        try:
            eshop = EShop.objects.get(id = eshop_id)
            account_id = eshop.account_id
            account = Account.objects.get(id = account_id)

            id = account.id
            boss = account.firstname + ' ' + account.lastname
            dp = account.display_pic
            phone = account.phone

            boss_info = {
                'id' : id,
                'boss' : boss,
                'dp' : dp,
                'phone' : phone
            }   

            serializer = AboutEShopSerializer( boss_info, many = False)
            
            return Response( serializer.data )
        
        except:
            pass

        
        return Response(False)


    def post(get, request, eshop_id):
        pass








































class EShopExist(APIView):

    def get(self, request):

        try:
            account = get_account(request)
            account_id = account.id

            eshop_exist = EShop.objects.filter(account_id = account_id).exists()

            json_object = {
                'eshop_exist' : eshop_exist
            }

            serializer = EShopExistSerializer( json_object, many = False)
            
            return Response( serializer.data )

        except:
            pass


        return Response(False)


    def post(get, request):
        pass


    































class NewEShopProduct(APIView):

    def get(self,request, account_id):
        pass

    
    def post(self, request, account_id):

       
        category = request.POST.get("category","")
        description = request.POST.get("description","")
        product_name = request.POST.get("product_name","")
        subcategory = request.POST.get("subcategory","")
        #product_image = request.FILES.get("product_image","")
        starting_price = request.POST.get("starting_price","")
        media = request.FILES.getlist("files","")


        if True:
            account = Account.objects.get(id=account_id)
            campus_id = account.campus_id

            campus = Campus.objects.get(id = campus_id)

            category = Category.objects.get(id = category)
        

            newProduct = Product()
            newProduct.account = account
            newProduct.category = category
            newProduct.campus = campus
            newProduct.description = description
            newProduct.product_name = product_name
            #newProduct.product_image = product_image
            newProduct.starting_price = starting_price
            

           
            i = 0
            for m in media :

                if i == 0:
                    newProduct.product_image = m
                    newProduct.save()

                    i = i + 1
               

                else:
                    media_register = Media()
        
                    media_register.image = m
                    media_register.video = m

                    file_type = media_register.image.url.split('.')[-1]
                    file_type = file_type.lower()

                    if file_type in IMAGE_FILE_TYPES:

                        media_register.video = 0

                    else:

                        file_type = media_register.video.url.split('.')[-1]
                        file_type = file_type.lower()

                        if file_type in VIDEO_FILE_TYPES:

                            media_register.image = 0

                        else:

                            err_msg = 'Unsupported file format, file should be valid image, audio or/and video files'
                    

                    media_register.product = newProduct
                    media_register.save()

                    i = i + 1
            



            sub_category = SubCategory.objects.get(id = subcategory)
            eshop_exist = EShop.objects.filter(account_id = account_id).exists


            if eshop_exist:
                eshop =  EShop.objects.get(account_id = account_id)
                eshop_id = eshop.id

                eshop_product = EShopProduct()
                eshop_product.eshop = eshop
                eshop_product.product = newProduct
                eshop_product.subcategory = sub_category
                eshop_product.save()

            else:
                pass


            ## upForSell Products, business mode
            try :
                topForSell = TopForSell.objects.get(product_name = product_name)
                topForSell.frequency = topForSell.frequency + 1
                topForSell.save()

            except:
                topForSell = TopForSell()
                topForSell.product_name = product_name
                topForSell.save()




            code = newProduct.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)




































class EShopCategoryView(APIView):

    def get(self, request, eshop_id):

        eshop_category = EShopCategory.objects.filter(eshop = eshop_id)

        dumb = []
        for category in eshop_category:
            item = Category.objects.get(id = category.category_id)
            name = item.name

            bucketlist = {
                'category_name': name
            }

            dumb.append(bucketlist)


        serializer = EShopCategorySerializer(dumb, many = True)

        return Response(serializer.data)


    def post(self, request, campus_id, subcategory_id):
        pass



































class EShopListCategory(APIView):

    def get(self, request, campus_id, category_id):

        if category_id == '99':
            eshoplist = EShop.objects.all()

            serializer = EShopSerializer(eshoplist, many=True)
            return Response(serializer.data)

        else:
            eshoplist = EShopCategory.objects.filter(category = category_id)

            bucketlist = []
            for eshop in eshoplist:
                shop = EShop.objects.get(id = eshop.eshop_id)
                bucketlist.append(shop)
        
            serializer = EShopSerializer(bucketlist, many = True)

            return Response(serializer.data)

        


    def post(self, request, campus_id, subcategory_id):
        pass

































class EShopList(APIView):

    def get(self, request, campus_id):
        
        eshoplist = EShop.objects.all()

        serializer = EShopSerializer(eshoplist, many = True)

        return Response(serializer.data)

    

    def post(self, request, campus_id):
        
        eshop_name = request.POST.get("eshop_name","")

        eshoplist = EShop.objects.filter(name__icontains = eshop_name)

        serializer = EShopSerializer(eshoplist, many = True)

        return Response(serializer.data)





































class EShopStore(APIView):


    def get(self, request, eshop_id, subcategory_id):

        eshopstore = EShopProduct.objects.filter(eshop_id = eshop_id, subcategory_id=subcategory_id)

        store = []
        for product in eshopstore:

            id = product.product_id

            goods = Product.objects.get(id = id)

            product_name = goods.product_name
            product_image = goods.product_image
            starting_price = goods.starting_price

            buffer = {
                'id' : id,
                'product_name' : product_name,
                'product_image' : product_image,
                'starting_price' : starting_price
            }

            store.append(buffer)


        serializer = EShopStoreSerializer( store, many=True)

        return Response(serializer.data)




    def post(self, request, eshop_id, subcategory_id):
        pass


























class EShopSubCategory(APIView):


    def get(self, request, eshop_id):

        eshopstore = EShopProduct.objects.filter(eshop_id = eshop_id)

        store = []
        id = 0
        for product in eshopstore:

            if id == product.subcategory_id:
                pass

            else:

                id = product.subcategory_id
                sub_category = SubCategory.objects.get(id = id)
                name = sub_category.name
                image = sub_category.image

                buffer = {
                    'id' : id,
                    'name' : name,
                    'image' : image
                }

                store.append(buffer)


        serializer = SubCategorySerializer( store, many=True)

        return Response(serializer.data)




    def post(self, request, eshop_id):
        pass

























class EditEShop(APIView):

    def get(self, request):
        pass

    def post(self, request):

        try:
            account = get_account(request)
            account_id = account.id

            eshop = EShop.objects.get(account_id = account_id)

            catch_board  = request.FILES.get("catch_board","")
            about = request.POST.get("about","")

            eshop.catch_board = catch_board
            if about :
                eshop.about = about
            eshop.save()

            code = eshop.id

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many=False)
            
            return Response(serializer.data)
        
        except:

            pass

        
        error_message = 'mhhmm, sorry update could not be executed'

        err = {
            'error_message' : error_message
        }

        serializer = ErrorCheckSerializer(err, many=False)
            
        return Response(serializer.data)

        

        
       




























class EShopSearch(APIView):


    def get(self, request, eshop_id, search_phrase):

        results = []
      

        buffer_result = Product.objects.filter(product_name__icontains = search_phrase) | Product.objects.filter(description__icontains = search_phrase) 
     

        for buffer in buffer_result :

            product_id = buffer.id

            try:

                eshop_product = EShopProduct.objects.get(eshop_id= eshop_id, product_id = product_id)
                product_name = buffer.product_name
                product_image = buffer.product_image
                starting_price = buffer.starting_price

                context_list = {
                    'product_id': product_id,
                    'product_name': product_name,
                    'product_image' : product_image,
                    'starting_price' : starting_price,
                }

                results.append(context_list)


            except:

                pass
            
            

               

        serializer = ResultListSerializer(results, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        pass

        
























class Rating(APIView):

    def get(self, request, eshop_id):
        
        if True:
            eshop_rating = EShopRateReview.objects.filter(eshop_id = eshop_id)
            
            rating_count = 0
            rating_no = 0

            for item in eshop_rating:

                ratereview = RateReview.objects.get(id = item.ratereview_id)

                rating_no = rating_no + 1

                rating_count = rating_count + ratereview.rating

            
            final_rating = int(rating_count / rating_no)

            return Response(final_rating)


        else:
            pass

        return Response(0)
    
    def post(self, request, eshop_id):
        pass








































class RRView(APIView):

    def get(self, request, status_code, id):
       
     
        rr_buffer = []
        
        if status_code == '0' :
            
            clientrr = ClientRateReview.objects.filter(account_id = id)
        
            for rr in clientrr :

                ratereview_id = rr.ratereview_id
                ratereview = RateReview.objects.get(id = ratereview_id )

                account_id = ratereview.account_id

                try:
                    rr_account = Account.objects.get(id=account_id)
                except:
                    error_message = 'control reached here 2'
                    return Response(error_message)

                client_name = rr_account.firstname + ' ' + rr_account.lastname
                client_image = rr_account.display_pic
                rating = ratereview.rating
                review = ratereview.review 

                ratings_reviews = {
                    'client_name' : client_name,
                    'client_image' : client_image,
                    'rating' : rating,
                    'review' : review
                }

                rr_buffer.append(ratings_reviews)
        
            serializer = ClientRRSerializer(rr_buffer, many=True )

            return Response(serializer.data)





        elif status_code == '1' :

            productrr = EShopRateReview.objects.filter(eshop_id = id)
        
            for rr in productrr :

                ratereview_id = rr.ratereview_id
                ratereview = RateReview.objects.get(id = ratereview_id )

                account_id = ratereview.account_id

                try:
                    rr_account = Account.objects.get(id=account_id)
                except:
                    error_message = 'control reached here 2'
                    return Response(error_message)

                client_name = rr_account.firstname + ' ' + rr_account.lastname
                client_image = rr_account.display_pic
                rating = ratereview.rating
                review = ratereview.review 

                ratings_reviews = {
                    'client_name' : client_name,
                    'client_image' : client_image,
                    'rating' : rating,
                    'review' : review
                }

                rr_buffer.append(ratings_reviews)
        
            serializer = EShopRRSerializer(rr_buffer, many=True )

            return Response(serializer.data)


        else:
           
            error_message = 'control reached here'
            return Response(error_message)





    
    def post(self, request, status_code, id):

        try:
            account = get_account(request)

        except:

            error_message = "invalid account"

            err = {
                'error_message' : error_message
            }

            serializer = ErrorCheckSerializer(err, many = False)
            return Response(serializer.data)


        if status_code == '0' :

            ratereview = RateReview()


            rating = request.POST.get("rating","")
            review = request.POST.get("review","")

            ratereview.account = account
            ratereview.rating = rating
            ratereview.review = review
            ratereview.save()

            try:
                client_account = Account.objects.get(id=id)
            except:
                
                error_message = "invalid account"

                err = {
                    'error_message' : error_message
                }

                serializer = ErrorCheckSerializer(err, many = False)
                return Response(serializer.data)

            clientrr = ClientRateReview()
            clientrr.ratereview = ratereview
            clientrr.account = client_account
            clientrr.save()
                

            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)
            return Response(serializer.data)



        elif status_code == '1' :

            ratereview = RateReview()

            rating = request.POST.get("rating","")
            review = request.POST.get("review","")

            ratereview.account = account
            ratereview.rating = rating
            ratereview.review = review
            ratereview.save()


            try:
                client_eshop = EShop.objects.get(id=id)
            except:
                
                error_message = "invalid eshop account"

                err = {
                    'error_message' : error_message
                }

                serializer = ErrorCheckSerializer(err, many = False)
                return Response(serializer.data)


            eshoprr = EShopRateReview()
            eshoprr.ratereview = ratereview
            eshoprr.eshop = client_eshop
            eshoprr.save()

            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)
            return Response(serializer.data)



        else:

            error_message = "wrong turn"

            err = {
                'error_message' : error_message
            }

            serializer = ErrorCheckSerializer(err, many = False)
            return Response(serializer.data)
























































class RRViewForm(APIView):

    def get(self, request, status_code, id):
        pass


    
    def post(self, request, status_code, id):

        if status_code == '0' :

            try: 
                account = get_account(request)

            except:
                pass

            ratereview = RateReview()


            rating = request.POST.get("rating","")
            review = request.POST.get("review","")

            ratereview.account = account
            ratereview.rating = rating
            ratereview.review = review
            ratereview.save()

            try:
                client_account = Account.objects.get(id=id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            clientrr = ClientRateReview()
            clientrr.ratereview = ratereview
            clientrr.account = client_account
            clientrr.save()
                

            return HttpResponseRedirect('https:/iwansell.com/profile/' + id)



        elif status_code == '1' :

            if request.session.has_key('email'):
                email = request.session['email']

            try:
                account = Account.objects.get(email=email)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            ratereview = RateReview()

            rating = request.POST.get("rating","")
            review = request.POST.get("review","")

            ratereview.account = account
            ratereview.rating = rating
            ratereview.review = review
            ratereview.save()


            try:
                client_eshop = EShop.objects.get(id=id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            eshoprr = EShopRateReview()
            eshoprr.ratereview = ratereview
            eshoprr.eshop = client_eshop
            eshoprr.save()

            return HttpResponseRedirect('https://iwansell.com/eshop/' + id)


        else:

            return Response(status=status.HTTP_404_NOT_FOUND)

            













































class SoldProduct(APIView):

    def get(self, request, product_id):

        sold = False
        
        try :
            product = Product.objects.get(id = product_id)
        except: 
             return Response(status=status.HTTP_404_NOT_FOUND)

        if product.sold :
            product.sold = False
            product.save()
        

        else:
            product.sold = True
            product.save()
            sold = True


        return Response(sold)



    
    def post(self, request, eshop_id):
        pass







































    








class RemovedProduct(APIView):

    def get(self, request, product_id):

        removed = False
        
        try :
            product = Product.objects.get(id = product_id)
        except: 
             return Response(status=status.HTTP_404_NOT_FOUND)

        if product.removed :
            product.removed = False
            product.save()
        

        else:
            product.removed = True
            product.save()
            sold = True


        return Response(removed)



    
    def post(self, request, eshop_id):
        pass















































class FavoriteView(APIView):

    def get(self, request, status_code, id):

        favorited = False

        if status_code == '0':
        

            try:
                account = get_account(request)
            except:
                pass

            try:
                fav_client = FavoriteClient.objects.get(client = id)
                fav_client.delete()

            except:
                    
                fav_client = FavoriteClient()
                fav_client.account = account
                fav_client.client = id
                fav_client.save()

                favorited = True


            

            return Response(favorited)
            

        elif status_code == '1':
            
            

            try:
                account = get_account(request)
                product = Product.objects.get(id = id)
            except:
                pass
            
            try:

                fav_product = FavoriteProduct.objects.get(product_id = id)
                fav_product.delete()

            except:

                fav_product = FavoriteProduct()
                fav_product.account = account
                fav_product.product = product
                fav_product.save()

                favorited = True


            

            return Response(favorited)


        elif status_code == '2':
            
            
            try:
                account = get_account(request)
                eshop = EShop.objects.get(id=id)
            except:
                pass

            try:

                fav_eshop = FavoriteEShop.objects.get(eshop_id = id)
                fav_eshop.delete()

            except:

                fav_eshop = FavoriteEShop()
                fav_eshop.account = account
                fav_eshop.eshop = eshop
                fav_eshop.save()

                favorited = True

            

            return Response(favorited)

        
        else:

            return Response(favorited)

    
    def post(self, request,  status_code, id):

        pass
        








































class FavoriteList(APIView):

    def get(self, request, status_code, profile_id):

        favorite_buffer = []

        if status_code == '0':

            fav_client = FavoriteClient.objects.filter(account_id = profile_id)

            
            for client in fav_client:

                account = Account.objects.get( id = client.id)

                profile_id = account.id
                name = account.firstname + ' ' + account.lastname
                display_pic = account.display_pic

                register = {
                    'profile_id' : profile_id,
                    'name' : name,
                    'display_pic' : display_pic
                }

                favorite_buffer.append(register)

            serializer = FavoriteListClient(favorite_buffer, many= True)

            return Response(serializer.data)


        elif status_code == '1':

            fav_product = FavoriteProduct.objects.filter(account_id = profile_id)

            
            for product in fav_product:

                product = Product.objects.get( id = product.id)

                product_id = product.id
                product_name = product.product_name
                product_image = product.product_image

                register = {
                    'product_id' : product_id,
                    'product_name' : product_name,
                    'product_image' : product_image
                }

                favorite_buffer.append(register)

            serializer = FavoriteListProduct(favorite_buffer, many= True)

            return Response(serializer.data)


        elif status_code == '2':

            fav_eshop = FavoriteEShop.objects.filter(account_id = profile_id)

            
            for eshop in fav_eshop:

                eshop = EShop.objects.get( id = eshop.id)

                eshop_id = eshop.id
                eshop_name = eshop.name
                catch_board = eshop.catch_board

                register = {
                    'eshop_id' : eshop_id,
                    'eshop_name' : eshop_name,
                    'catch_board' : catch_board
                }

                favorite_buffer.append(register)

            serializer = FavoriteListEShop(favorite_buffer, many= True)

            return Response(serializer.data)


        else:
            pass


    def post(self, request, status_code, profile_id):

        pass





















































class GetAccount(APIView):

    def get(self,request):
        
        
        try:
            account = get_account(request)
            account_id = account.id
        except:
            
            account_id = False

        return Response(account_id)
    
    def post(self, request):
        pass






































class GetCampus(APIView):

    def get(self,request):
        
        try:
            account = get_account(request)
            campus_id = account.campus_id
        except:
            campus_id = 1


        return Response(campus_id)
    
    def post(self, request):
        pass














class CampusCode(APIView):

    def get(self,request, campus_id):
        
        try:
            campus = Campus.objects.get(id = campus_id)
            campus_code = campus.campus_code

        except:
            campus_code = "The"
        
        

        return Response(campus_code)
    
    def post(self, request):
        pass


































class ProductName(APIView):

    def get(self, request, product_id):
        
        try:
            product = Product.objects.get(id = product_id)
            product_name = product.product_name

            return Response(product_name)

        
        except:
            pass
        
        return Response("Invalid product selected!")


    def post(self, request, product_id):
        pass




























class PaymentMethodView(APIView):

    def get(self, request):
        
        payment_method = PaymentMethod.objects.all()

        serializer = PaymentMethodSerializer(payment_method, many=True)

        return Response(serializer.data)

    
    def post(self, request):
        pass



































class InitiateTransaction(APIView):

    def get(self, request):
        pass


    
    def post(self, request):
       
            
        try:
            seller = get_account(request)

            product_id = request.POST.get("product_id", "")
            agreed_price = request.POST.get("agreed_price", "")
            quantity = request.POST.get("quantity", "")
            payment_method = request.POST.get("payment_method", "")

            product = Product.objects.get(id = product_id)
            payment_method = PaymentMethod.objects.get(id = payment_method)

            token = token_code_generator()

            new_transaction = Transaction()
            new_transaction.seller = seller
            new_transaction.product = product
            new_transaction.payment_method = payment_method
            new_transaction.agreed_price = agreed_price
            new_transaction.quantity = quantity
            new_transaction.token = token
            new_transaction.save()

            return Response(token)

        except:
            pass

        
        return Response("Yikes wrong turn, please try again")































class ConfirmBuyer(APIView):

    def get(self, request):
        
        pass

    
    def post(self, request):
        
        try:
            account = get_account(request)
            token = request.POST.get("token","")

            transaction = Transaction.objects.get(seller_id = account.id, token= token )
            buyer_account = Account.objects.get(id = transaction.buyer)

            buyer = buyer_account.firstname + ' ' + buyer_account.lastname
            transaction_id = transaction.id

            item = {
                'buyer' : buyer,
                'transaction_id': transaction_id
            }

            serializer = BuyerSerializer(item, many = False)

            return Response(serializer.data)

        except:
            pass

        
        return Response(False)
            




























class ConfirmTransactionSeller(APIView):

    def get(self, request):
        pass

    
    def post(self, request):
        
        try:
            account = get_account(request)
            token = request.POST.get("token","")

            transaction = Transaction.objects.get(seller_id = account.id, token= token )
            transaction.status = True
            transaction.save()


            ## Sold, business mode
            try: 
                product = Product.object.get(id = transaction.product_id)
                product_name = product.product_name

                try :
                    sold = Sold.objects.get(product_name = product_name)
                    sold.frequency = sold.frequency + 1
                    sold.save()

                except:
                    sold = Sold()
                    sold.product_name = product_name
                    sold.save()
                
            except:
                pass



            return Response(True)

        except:
            pass

        
        return Response(False)

























class Receipt(APIView):

    def get(self, request, transaction_id):
        
        try:

            token = request.POST.get("token", "")
          
            new_transaction = Transaction.objects.get(id = transaction_id)
            
            product = Product.objects.get(id = new_transaction.product_id)
            payment = PaymentMethod.objects.get(id = new_transaction.payment_method_id)
            seller_account = Account.objects.get(id = new_transaction.seller_id)
            buyer_account = Account.objects.get(id = new_transaction.buyer)

            campus = Campus.objects.get(id = seller_account.campus_id)
            

            transaction_id = new_transaction.id
            seller = seller_account.firstname + ' ' + seller_account.lastname
            buyer = buyer_account.firstname + ' ' + buyer_account.lastname
            token = token
            product_name = product.product_name
            product_image = product.product_image
            price = new_transaction.agreed_price
            payment_method = payment.payment_method
            quantity = new_transaction.quantity
            campus_code = campus.campus_code
            date = new_transaction.date
            


            bucketlist  = {
                'transaction_id' : transaction_id,
                'seller' : seller,
                'buyer' : buyer,
                'token' : token,
                'product_name' : product_name,
                'product_image' : product_image,
                'price' : price,
                'payment_method' : payment_method,
                'quantity' : quantity,
                'campus_code' : campus_code,
                'date' : date
            }

            serializer = ReceiptSerializer(bucketlist, many=False)


            return Response(serializer.data)

        except:
            pass


        
        error_message = 'Ye! something broke, please try again '
        err = {
            'error_message' : error_message
        }
        serializer = ErrorCheckSerializer( err, many=False)

        return Response(serializer.data)

    
    def post(self, request, transaction_id):
        pass
        

        



























class JoinTransaction(APIView):

    def get(self, request):
        pass

    
    def post(self, request):

        try:
            buyer = get_account(request)

            token = request.POST.get("token", "")
          
            new_transaction = Transaction.objects.get(token = token)

            product = Product.objects.get(id = new_transaction.product_id)
            payment = PaymentMethod.objects.get(id = new_transaction.payment_method_id)
            seller_account = Account.objects.get(id = new_transaction.seller_id)

            transaction_id = new_transaction.id
            seller = seller_account.firstname + ' ' + seller_account.lastname
            token = token
            product_name = product.product_name
            product_image = product.product_image
            agreed_price = new_transaction.agreed_price
            payment_method = payment.payment_method
            quantity = new_transaction.quantity

            bucketlist  = {
                'transaction_id' : transaction_id,
                'seller' : seller,
                'token' : token,
                'product_name' : product_name,
                'product_image' : product_image,
                'agreed_price' : agreed_price,
                'payment_method' : payment_method,
                'quantity' : quantity
            }

            serializer = TransactionSerializer(bucketlist, many=False)


            return Response(serializer.data)

        except:
            pass


        
        error_message = 'Ye! something broke, please try again '
        err = {
            'error_message' : error_message
        }
        serializer = ErrorCheckSerializer( err, many=False)

        return Response(serializer.data)



































class ConfirmTransactionBuyer(APIView):

    def get(self, request, transaction_id):
        pass

    
    def post(self, request, transaction_id):
        
        try:
            account = get_account(request)
            token = request.POST.get("token","")

            transaction = Transaction.objects.get(token= token )
            transaction.buyer = account.id
            transaction.save()

            return Response(True)

        except:
            pass

        
        return Response(False)
            


























class TransactionStatus(APIView):

    def get(self, request):
        pass

    
    def post(self, request):
        try:
            account = get_account(request)
            token = request.POST.get("token","")

            transaction = Transaction.objects.get(seller_id = account.id, token= token )
            if transaction.status :
                return Response(True)
                     

        except:
            pass

        
        return Response(False)




























class TopSearchedView(APIView):

    def get(self, request):
        top_seached = TopSearched.objects.all()

        serializer = BusinessSerializer(top_seached, many=True)

        return Response(serializer.data)

    
    def post(self, request):
        pass



















class TopSoldView(APIView):

    def get(self, request):
        top_sold = Sold.objects.all()

        serializer = BusinessSerializer(top_sold, many=True)

        return Response(serializer.data)

    
    def post(self, request):
        pass
















class TopForSellView(APIView):

    def get(self, request):
        top_for_sell = TopForSell.objects.all()

        serializer = BusinessSerializer(top_for_sell, many=True)

        return Response(serializer.data)

    
    def post(self, request):
        pass


















class TopNotFoundView(APIView):

    def get(self, request):
        
        top_not_found = NotFound.objects.all()

        serializer = BusinessSerializer(top_not_found, many=True)

        return Response(serializer.data)

    
    def post(self, request):
        pass


















class LeastSoldView(APIView):

    def get(self, request):
        
        least_sold = Sold.objects.all().reverse()

        serializer = BusinessSerializer(least_sold, many=True)

        return Response(serializer.data)

    
    def post(self, request):
        pass



























class LeastForSellView(APIView):

    def get(self, request):
        
        least_for_sell = TopForSell.objects.all().reverse()

        serializer = BusinessSerializer(least_for_sell, many=True)

        return Response(serializer.data)

    
    def post(self, request):
        pass






















class ProductValuation(APIView):

    def get(self, request):
        pass

    
    def post(self, request):

        product = request.POST.get("product","")

        try:
            searched  = TopSearched.objects.get(product_name = product)
            searched_frequency = searched.frequency

        except:
            searched_frequency = 0

        
        try:
            notFound  = NotFound.objects.get(product_name = product)
            notFound_frequency = notFound.frequency

        except:
            notFound_frequency = 0

        
        try:
            forSell  = TopForSell.objects.get(product_name = product)
            forSell_frequency = forSell.frequency

        except:
            forSell_frequency = 0


        try:
            sold = Sold.objects.get(product_name = product)
            sold_frequency = sold.frequency

        except:
            sold_frequency = 0

        product_review = {
            'searched_frequency' : searched_frequency,
            'notFound_frequency' : notFound_frequency,
            'forSell_frequency' : forSell_frequency,
            'sold_frequency' : sold_frequency
        }

        serializer = ProductValuationSerializer( product_review, many= False)

        return Response(serializer.data)



























class AlternatePhoneView(APIView):

    def get(self, request):

        try:
            account = get_account(request)
            account_id = account.id

            alternate_phone = AlternatePhone.objects.get(account_id = account.id)

            serializer = AlternatePhoneSerializer(alternate_phone, many=False)

            return Response(serializer.data)

        except:
            pass  

        empty_set = {}
        return Response(empty_set)      

    
    def post(self, request):
        
        try:
            account = get_account(request)

            phone1 = request.POST.get("phone1","")
            phone2 = request.POST.get("phone2","")

            try :
                alternate_phone = AlternatePhone.objects.get(account_id = 5)
                
                if phone1:
                    alternate_phone.phone1 = phone1
                
                if phone2:
                    alternate_phone.phone2 = phone2

                alternate_phone.save()

                code = 11
                context = {
                    'code' : code
                }

                serializer = SuccessCodeSerializer(context, many = False)

                return Response(serializer.data)

                

            except:
                alternate_phone = AlternatePhone()
                alternate_phone.account = account
                alternate_phone.phone1 = phone1
                alternate_phone.phone2 = phone2
                alternate_phone.save()
                

                code = 11
                context = {
                    'code' : code
                }

                serializer = SuccessCodeSerializer(context, many = False)

                return Response(serializer.data)

            
            


        except:
            pass 
                
        error_message = 'Oops something wrong happened'

        context = {             
            'error_message' : error_message
        }    

        serializer = ErrorCheckSerializer(context, many = False)

        return Response(serializer.data)












class AlternatePhoneSellerView(APIView):

    def get(self, request, account_id):

        try:
            account = Account.objects.get(id = account_id)
            account_id = account.id

            alternate_phone = AlternatePhone.objects.get(account_id = account.id)

            serializer = AlternatePhoneSerializer(alternate_phone, many=False)

            return Response(serializer.data)

        except:
            pass  

        empty_set = {}
        return Response(empty_set)      

    
    def post(self, request, account_id):
        pass
        




















class GetPhone(APIView):

    def get(self, request):
        
        try:
            account = get_account(request)
            phone = account.phone

            return Response(phone)

        except:
            pass
        
        empty_set = {}
        return Response(empty_set)

    
    def post(self, request):
        pass




























class ForgotPasswordView(APIView):


    def get(self,request):
        pass


    def post(self,request):

        

        email = request.POST.get("email", "")

        if Account.objects.filter(email = email).exists():

            reset_code = reset_code_generator()

            clear_cache = ForgotPassword.objects.filter(email = email).delete()

            new_reset = ForgotPassword()
            new_reset.reset_code = reset_code
            new_reset.email = email
            new_reset.save()

            message = 'Hey dear! You are nearly done with your password reset process, Follow this link to reset your password http://127.0.0.1:3000/reset_password/' +  str(reset_code) + ' You have done well'
            email = EmailMessage('Your password reset details from Iwansell', message, to=[email])
            email.send()

            success_message = 'Hey dear, Your password reset details has been sent to your email account(username), get the email and reset password'

            code = 11
            context = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(context, many = False)

            return Response(serializer.data)


        else:

                
            error_message = ' Account with that username does not exist'

            context = {             
                'error_message' : error_message
            }

            serializer = ErrorCheckSerializer(context, many = False)

            return Response(serializer.data)



        

        error_message = 'Oops Sorry something unexpected happened, please try again'

        context = {
            'error_message' : error_message
        }

        serializer = ErrorCheckSerializer(context, many = False)

        return Response(serializer.data)

    































class ResetPassword(APIView):

    def get(self, request, reset_code):
        pass

    
    def post(self, request, reset_code):

        new_password = request.POST.get("new_password", "")

        bug_net = 1

        try :
            forgot_pass = ForgotPassword.objects.get(reset_code = reset_code)
            email = forgot_pass.email

            account = Account.objects.get(email = email)
            account.password = make_password(new_password)
            account.save()
            bug_net = 11

            user = User.objects.get(email = email)
            bug_net = 911
            user.password = make_password(new_password)
            user.save()

            forgot_pass.delete()

            code = 11
            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)
            
        except:
            
            error_message = 'We didn\'t provide this link, wrong turn'

            err = {
                'error_message' : error_message
            }

            serializer = ErrorCheckSerializer(err, many= False)

            return Response(bug_net)


        

        






















class ChannelView(APIView):

    def get(self, request, campus_id):
        
        threadlist = Thread.objects.filter(campus_id = campus_id)

        thread_bucket = []

        for t in threadlist:

            title = t.title
            thread = t.thread
            media = t.media
            date = t.date
            thread_id = t.id

            account = Account.objects.get(id = t.account_id)
            firstname = account.firstname
            lastname = account.lastname

            channel = Channel.objects.get(id = t.channel_id)
            channel_id = channel.id
            logo = channel.logo
            channel = channel.channel

            following = False
            try:
                myaccount = get_account(request)
                following = Following.objects.get(account_id = myaccount.id, channel_id = channel_id )
                following = True

            except:
                pass

            comment_count = Comment.objects.filter(thread_id = thread_id).count()

            upvote = ThreadVote.objects.filter(thread_id = t.id, upvote=True).count()
            downvote = ThreadVote.objects.filter(thread_id = t.id, downvote=True).count()
            votes = upvote - downvote

            thread_register = {
                'comment_count': comment_count,
                'channel_id': channel_id,
                'following' : following,
                'firstname' : firstname,
                'lastname' : lastname,
                'thread_id': thread_id,
                'channel' : channel,
                'thread' : thread,
                'title' : title,
                'media' : media,
                'votes' : votes,
                'date' : date,
                'logo' : logo,
            }

            thread_bucket.append(thread_register)

    
        serializer = ThreadSerializer(thread_bucket, many=True)

        return Response(serializer.data)

    
    def post(self, request, campus_id):
        pass


















class ThreadView(APIView):

    def get(self, request, thread_id):
        
        try: 
            t = Thread.objects.get(id = thread_id)

            title = t.title
            thread = t.thread
            media = t.media
            date = t.date
            thread_id = t.id

            account = Account.objects.get(id = t.account_id)
            firstname = account.firstname
            lastname = account.lastname

            channel = Channel.objects.get(id = t.channel_id)
            channel_id = channel.id
            logo = channel.logo
            channel = channel.channel

            following = False
            try:
                myaccount = get_account(request)
                following = Following.objects.get(account_id = myaccount.id, channel_id = channel_id )
                following = True

            except:
                pass

            comment_count = Comment.objects.filter(thread_id = thread_id).count()

            upvote = ThreadVote.objects.filter(thread_id = t.id, upvote=True).count()
            downvote = ThreadVote.objects.filter(thread_id = t.id, downvote=True).count()
            votes = upvote - downvote

            thread_register = {
                'channel_id': channel_id,
                'following' : following,
                'firstname' : firstname,
                'lastname' : lastname,
                'thread_id': thread_id,
                'channel' : channel,
                'thread' : thread,
                'title' : title,
                'media' : media,
                'votes' : votes,
                'comment_count' : comment_count,
                'date' : date,
                'logo' : logo,
            }

            serializer = ThreadSerializer(thread_register, many=False)

            return Response(serializer.data)


        except:
            pass
        
        return Response(bug_net)



    
    def post(self, request, thread_id):
        
        title = request.POST.get("title","")
        thread = request.POST.get("post","")
        media = request.FILES.getlist("files", "")
      
        if True:
            account = Account.objects.get(id=5)
            channel = Channel.objects.get(account_id = account.id)
            campus = Campus.objects.get(id = account.campus_id)

            newThread = Thread()
            newThread.account = account
            newThread.channel = channel
            newThread.campus = campus
            newThread.title = title
            newThread.thread = thread
           

           
            i = 0
            for m in media :

                if i == 0:
                    newThread.media = m
                    newThread.save()

                    i = i + 1

            code = newThread.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)





















class FollowView(APIView):

    def get(self, request, channel_id):

        status = False
        try:
            account = get_account(request)
            channel = Channel.objects.get(id = channel_id)

            following = Following()
            following.channel = channel
            following.account = account
            following.save()

            status = True
        
        except: 
            pass

        
        return Response(status)
        
        
       
        

    
    def post(self, request, channel_id):
        pass

















class VoteView(APIView):

    def get(self, request, toggle, thread_id):

        upvote = ThreadVote.objects.filter(thread_id = thread_id, upvote=True).count()
        downvote = ThreadVote.objects.filter(thread_id = thread_id, downvote=True).count()
        votes = upvote - downvote

        try:
            #account = get_account(request)
            account = Account.objects.get(id = 3)
            try: 
                threadvote = ThreadVote.objects.get(thread_id = thread_id, account_id = account.id)
            except:
                thread = Thread.objects.get(id = thread_id)
                vote = ThreadVote()
                vote.thread = thread
                vote.account = account
                if toggle == '1':
                    vote.upvote = True
                else:
                    vote.downvote = True
                vote.save()
               
                
                
            upvote = ThreadVote.objects.filter(thread_id = thread_id, upvote=True).count()
            downvote = ThreadVote.objects.filter(thread_id = thread_id, downvote=True).count()
            votes = upvote - downvote
        
        except: 
            pass

        
        return Response(votes)
        
        
       
        

    
    def post(self, request, toggle, thread_id):
        pass


























class CommentView(APIView):

    def get(self, request, thread_id):

        comment = Comment.objects.filter(thread_id = thread_id)

        comment_bucket = []

        for c in comment:

            account = Account.objects.get(id = c.account_id)
            firstname = account.firstname
            lastname = account.lastname
            dp = account.display_pic

            comment_id = c.id
            comment = c.comment
            date = c.date

            comment_count = Reply.objects.filter(comment_id = comment_id).count()

            upvote = CommentVote.objects.filter(comment_id = c.id, upvote=True).count()
            downvote = CommentVote.objects.filter(comment_id = c.id, downvote=True).count()
            votes = upvote - downvote

            comment_register = {
                'comment_id' : comment_id,
                'comment' : comment,
                'comment_count' : comment_count,
                'firstname' : firstname,
                'lastname' : lastname,
                'votes' : votes,
                'dp' : dp,
                'date' : date,
            }

            comment_bucket.append(comment_register)
        
        serializer = CommentSerializer(comment_bucket, many=True)

        return Response(serializer.data)
        



    def post(self, request, thread_id):
        
        comment = request.POST.get("comment","")
       
      
        if True:
            account = Account.objects.get(id=5)
            thread = Thread.objects.get(id = thread_id)

            newComment = Comment()
            newComment.account = account
            newComment.thread = thread
            newComment.comment = comment
            newComment.save()

            code = newComment.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)







        













        




class ReplyView(APIView):

    def get(self, request, comment_id):

        reply = Reply.objects.filter( comment_id = comment_id)

        reply_bucket = []

        for r in reply:

            account = Account.objects.get(id = r.account_id)
            firstname = account.firstname
            lastname = account.lastname
            dp = account.display_pic

            reply_id = r.id
            reply = r.reply
            date = r.date

            reply_count = Reply1.objects.filter(reply_id = reply_id).count()

            upvote = ReplyVote.objects.filter(reply_id = r.id, upvote=True).count()
            downvote = ReplyVote.objects.filter(reply_id = r.id, downvote=True).count()
            votes = upvote - downvote

            reply_register = {
                'reply_id' : reply_id,
                'reply' : reply,
                'reply_count' : reply_count,
                'firstname' : firstname,
                'lastname' : lastname,
                'votes' : votes,
                'dp' : dp,
                'date' : date,
            }

            reply_bucket.append(reply_register)

        serializer = ReplySerializer(reply_bucket, many=True)
        
        return Response(serializer.data)



    
    def post(self, request, comment_id):
        
        
        reply = request.POST.get("reply","")
       
      
        if True:
            account = Account.objects.get(id=5)
            comment = Comment.objects.get(id = comment_id)

            newReply = Reply()
            newReply.account = account
            newReply.comment = comment
            newReply.reply = reply
            newReply.save()

            code = newReply.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)








################################ Reply Tree Redesign
class Reply1View(APIView):

    def get(self, request, reply_id):

        reply = Reply1.objects.filter( reply_id = reply_id)

        reply_bucket = []

        for r in reply:

            account = Account.objects.get(id = r.account_id)
            firstname = account.firstname
            lastname = account.lastname
            dp = account.display_pic

            reply_id = r.id
            reply = r.reply_t
            date = r.date

            reply_count = Reply2.objects.filter(reply1_id = reply_id).count()

            upvote = Reply1Vote.objects.filter(reply1_id = r.id, upvote=True).count()
            downvote = Reply1Vote.objects.filter(reply1_id = r.id, downvote=True).count()
            votes = upvote - downvote

            reply_register = {
                'reply_id' : reply_id,
                'reply' : reply,
                'reply_count' : reply_count,
                'firstname' : firstname,
                'lastname' : lastname,
                'votes' : votes,
                'dp' : dp,
                'date' : date,
            }

            reply_bucket.append(reply_register)

        serializer = ReplySerializer(reply_bucket, many=True)
        
        return Response(serializer.data)



    
    def post(self, request, reply_id):
        
        
        reply_t = request.POST.get("reply","")
       
      
        if True:
            account = Account.objects.get(id=5)
            reply = Reply.objects.get(id = reply_id)

            newReply = Reply1()
            newReply.account = account
            newReply.reply = reply
            newReply.reply_t = reply_t
            newReply.save()

            code = newReply.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)

















class Reply2View(APIView):

    def get(self, request, reply_id):

        reply = Reply2.objects.filter( reply1_id = reply_id)

        reply_bucket = []

        for r in reply:

            account = Account.objects.get(id = r.account_id)
            firstname = account.firstname
            lastname = account.lastname
            dp = account.display_pic

            reply_id = r.id
            reply = r.reply
            date = r.date

            reply_count = Reply3.objects.filter(reply2_id = reply_id).count()

            upvote = Reply2Vote.objects.filter(reply2_id = r.id, upvote=True).count()
            

            downvote = Reply2Vote.objects.filter(reply2_id = r.id, downvote=True).count()
            votes = upvote - downvote

            reply_register = {
                'reply_id' : reply_id,
                'reply' : reply,
                'reply_count' : reply_count,
                'firstname' : firstname,
                'lastname' : lastname,
                'votes' : votes,
                'dp' : dp,
                'date' : date,
            }

            reply_bucket.append(reply_register)

        serializer = ReplySerializer(reply_bucket, many=True)
        
        return Response(serializer.data)



    
    def post(self, request, reply_id):
        
        
        reply = request.POST.get("reply","")
       
      
        if True:
            account = Account.objects.get(id=5)
            reply1 = Reply1.objects.get(id = reply_id)

            newReply = Reply2()
            newReply.account = account
            newReply.reply1 = reply1
            newReply.reply = reply
            newReply.save()

            code = newReply.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)






















class Reply3View(APIView):

    def get(self, request, reply_id):

        reply_ = Reply3.objects.filter( reply2_id = reply_id)

        reply_bucket = []

        for r in reply_:

            account = Account.objects.get(id = r.account_id)
            firstname = account.firstname
            lastname = account.lastname
            dp = account.display_pic

            reply_id = r.id
            reply = r.reply
            date = r.date

            reply_count = Reply4.objects.filter(reply3_id = reply_id).count()
           
            upvote = Reply3Vote.objects.filter(reply3_id = r.id, upvote=True).count()
            downvote = Reply3Vote.objects.filter(reply3_id = r.id, downvote=True).count()
            votes = upvote - downvote

            reply_register = {
                'reply_id' : reply_id,
                'reply' : reply,
                'reply_count' : reply_count,
                'firstname' : firstname,
                'lastname' : lastname,
                'votes' : votes,
                'dp' : dp,
                'date' : date,
            }

            reply_bucket.append(reply_register)

        serializer = ReplySerializer(reply_bucket, many=True)
        
        return Response(serializer.data)



    
    def post(self, request, reply_id):
        
        
        reply = request.POST.get("reply","")
       
      
        if True:
            account = Account.objects.get(id=5)
            reply2 = Reply2.objects.get(id = reply_id)

            newReply = Reply3()
            newReply.account = account
            newReply.reply2 = reply2
            newReply.reply = reply
            newReply.save()

            code = newReply.id

            success = {
                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)
            return Response(serializer.data)






















class Reply4View(APIView):

    def get(self, request, reply_id):

        reply = Reply4.objects.filter( reply3_id = reply_id)

        reply_bucket = []

        for r in reply:

            account = Account.objects.get(id = r.account_id)
            firstname = account.firstname
            lastname = account.lastname
            dp = account.display_pic

            reply_id = r.id
            reply = r.reply
            date = r.date

            reply_count = 11

            upvote = Reply4Vote.objects.filter(reply4_id = r.id, upvote=True).count()
            downvote = Reply4Vote.objects.filter(reply4_id = r.id, downvote=True).count()
            votes = upvote - downvote

            reply_register = {
                'reply_id' : reply_id,
                'reply' : reply,
                'reply_count' : reply_count,
                'firstname' : firstname,
                'lastname' : lastname,
                'votes' : votes,
                'dp' : dp,
                'date' : date,
            }

            reply_bucket.append(reply_register)

        serializer = ReplySerializer(reply_bucket, many=True)
        
        return Response(serializer.data)



    
    def post(self, request, reply_id):
        
        
        reply = request.POST.get("reply","")
       
      
        if True:
            account = Account.objects.get(id=5)
            reply3 = Reply3.objects.get(id = reply_id)

            newReply = Reply4()
            newReply.account = account
            newReply.reply3 = reply3
            newReply.reply = reply
            newReply.save()

            code = newReply.id

            success = {

                'code' : code
                }

            serializer = SuccessCodeSerializer(success, many = False)

            return Response(serializer.data)

        else:

            error_message = 'yikes! something went wrong'
            err = {
                'error_message' : error_message
            }
            serializer = ErrorCheckSerializer( err, many=False)

            return Response(serializer.data)


















class VoteComment(APIView):

    def get(self, request, toggle, comment_id):

        upvote = CommentVote.objects.filter(comment_id = comment_id, upvote=True).count()
        downvote = CommentVote.objects.filter(comment_id = comment_id, downvote=True).count()
        votes = upvote - downvote

        try:
            #account = get_account(request)
            account = Account.objects.get(id = 3)
            try: 
                commentvote = CommentVote.objects.get(comment_id = comment_id, account_id = account.id)
            except:
                comment = Comment.objects.get(id = comment_id)
                vote = CommentVote()
                vote.comment = comment
                vote.account = account
                if toggle == '1':
                    vote.upvote = True
                else:
                    vote.downvote = True
                vote.save()
               
                
                
            upvote = CommentVote.objects.filter(comment_id = comment_id, upvote=True).count()
            downvote = CommentVote.objects.filter(comment_id = comment_id, downvote=True).count()
            votes = upvote - downvote
        
        except: 
            pass

        
        return Response(votes)
        
        
       
        

    
    def post(self, request, toggle, comment_id):
        pass

























class VoteReply(APIView):

    def get(self, request, toggle, reply_id):

        upvote = ReplyVote.objects.filter(reply_id = reply_id, upvote=True).count()
        downvote = ReplyVote.objects.filter(reply_id = reply_id, downvote=True).count()
        votes = upvote - downvote

        try:
            #account = get_account(request)
            account = Account.objects.get(id = 3)
            try: 
                replyvote = ReplyVote.objects.get(reply_id = reply_id, account_id = account.id)
            except:
                reply = Reply.objects.get(id = reply_id)
                vote = ReplyVote()
                vote.reply = reply
                vote.account = account
                if toggle == '1':
                    vote.upvote = True
                else:
                    vote.downvote = True
                vote.save()
               
                
                
            upvote = ReplyVote.objects.filter(reply_id = reply_id, upvote=True).count()
            downvote = ReplyVote.objects.filter(reply_id = reply_id, downvote=True).count()
            votes = upvote - downvote
        
        except: 
            pass

        
        return Response(votes)
        
        
       
        

    
    def post(self, request, toggle, reply_id):
        pass


























class VoteReply1(APIView):

    def get(self, request, toggle, reply_id):

        upvote = Reply1Vote.objects.filter(reply1_id = reply_id, upvote=True).count()
        downvote = Reply1Vote.objects.filter(reply1_id = reply_id, downvote=True).count()
        votes = upvote - downvote

        try:
            #account = get_account(request)
            account = Account.objects.get(id = 3)
            try: 
                replyvote = Reply1Vote.objects.get(reply1_id = reply_id, account_id = account.id)
            except:
                reply = Reply1.objects.get(id = reply_id)
                vote = Reply1Vote()
                vote.reply1 = reply
                vote.account = account
                if toggle == '1':
                    vote.upvote = True
                else:
                    vote.downvote = True
                vote.save()
               
                
                
            upvote = Reply1Vote.objects.filter(reply1_id = reply_id, upvote=True).count()
            downvote = Reply1Vote.objects.filter(reply1_id = reply_id, downvote=True).count()
            votes = upvote - downvote
        
        except: 
            pass

        
        return Response(votes)
        
        
       
        

    
    def post(self, request, toggle, reply_id):
        pass




























class VoteReply2(APIView):

    def get(self, request, toggle, reply_id):

        upvote = Reply2Vote.objects.filter(reply2_id = reply_id, upvote=True).count()
        downvote = Reply2Vote.objects.filter(reply2_id = reply_id, downvote=True).count()
        votes = upvote - downvote

        try:
            #account = get_account(request)
            account = Account.objects.get(id = 3)
            try: 
                replyvote = Reply2Vote.objects.get(reply2_id = reply_id, account_id = account.id)
            except:
                reply = Reply2.objects.get(id = reply_id)
                vote = Reply2Vote()
                vote.reply2 = reply
                vote.account = account
                if toggle == '1':
                    vote.upvote = True
                else:
                    vote.downvote = True
                vote.save()
               
                
                
            upvote = Reply2Vote.objects.filter(reply2_id = reply_id, upvote=True).count()
            downvote = Reply2Vote.objects.filter(reply2_id = reply_id, downvote=True).count()
            votes = upvote - downvote
        
        except: 
            pass

        
        return Response(votes)
        
        
       
        

    
    def post(self, request, toggle, reply_id):
        pass






























class VoteReply3(APIView):

    def get(self, request, toggle, reply_id):

        upvote = Reply3Vote.objects.filter(reply3_id = reply_id, upvote=True).count()
        downvote = Reply3Vote.objects.filter(reply3_id = reply_id, downvote=True).count()
        votes = upvote - downvote

        try:
            #account = get_account(request)
            account = Account.objects.get(id = 3)
            try: 
                replyvote = Reply3Vote.objects.get(reply3_id = reply_id, account_id = account.id)
            except:
                reply = Reply3.objects.get(id = reply_id)
                vote = Reply3Vote()
                vote.reply3 = reply
                vote.account = account
                if toggle == '1':
                    vote.upvote = True
                else:
                    vote.downvote = True
                vote.save()
               
                
                
            upvote = Reply3Vote.objects.filter(reply3_id = reply_id, upvote=True).count()
            downvote = Reply3Vote.objects.filter(reply3_id = reply_id, downvote=True).count()
            votes = upvote - downvote
        
        except: 
            pass

        
        return Response(votes)
        
        
       
        

    
    def post(self, request, toggle, reply_id):
        pass






























class VoteReply4(APIView):

    def get(self, request, toggle, reply_id):

        upvote = Reply4Vote.objects.filter(reply4_id = reply_id, upvote=True).count()
        downvote = Reply4Vote.objects.filter(reply4_id = reply_id, downvote=True).count()
        votes = upvote - downvote

        try:
            #account = get_account(request)
            account = Account.objects.get(id = 3)
            try: 
                replyvote = Reply4Vote.objects.get(reply4_id = reply_id, account_id = account.id)
            except:
                reply = Reply4.objects.get(id = reply_id)
                vote = Reply4Vote()
                vote.reply4 = reply
                vote.account = account
                if toggle == '1':
                    vote.upvote = True
                else:
                    vote.downvote = True
                vote.save()
               
                
                
            upvote = Reply4Vote.objects.filter(reply4_id = reply_id, upvote=True).count()
            downvote = Reply4Vote.objects.filter(reply4_id = reply_id, downvote=True).count()
            votes = upvote - downvote
        
        except: 
            pass

        
        return Response(votes)





















class GetChannel(APIView):

    def get(self,request):
        
        
        try:
            account = Account.objects.get(id = 5)
            account_id = account.id

            channel = Channel.objects.get(account_id = account_id)
            channel_name = "Add new post[" + channel.channel + "]"

        except:
            
            channel_name = "Wrong turn, try again"


        return Response(str(channel_name))
    

    
    def post(self, request):
        pass

        










def logout(request):

    def get(self, request):
        pass

    
    def post(self, request):
        pass
















                





