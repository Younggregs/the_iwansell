from rest_framework import serializers
from .models import Account, Category, SubCategory, Campus, Sponsored, Product, EShop, RateReview, Trending, Media, Blog, ForgotPassword

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class AddAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['firstname','lastname','phone','campus','password']


class SignInSerializer(serializers.Serializer):

        username = serializers.CharField()
        password = serializers.IntegerField()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'icon']

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'image']


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class CampusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campus
        fields = ['id', 'campus_code']


class ResultListSerializer(serializers.Serializer):

    product_id =  serializers.IntegerField()
    product_name = serializers.CharField()
    product_image = serializers.CharField()
    starting_price = serializers.CharField()


class TrendSerializer(serializers.ModelSerializer):

   class Meta:
        model = Trending
        fields = ['id', 'product_image']



class EShopStoreSerializer(serializers.ModelSerializer):

   class Meta:
       model = Product
       fields = ['id','product_name', 'product_image', 'starting_price']


class SponsoredSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsored
        fields = ['product_image']


class ProductSerializer(serializers.Serializer):
    
    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    product_description = serializers.CharField()
    product_image = serializers.CharField()
    starting_price = serializers.CharField()
    profile_id = serializers.IntegerField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    phone = serializers.CharField()
    display_pic = serializers.CharField()



class EShopCategorySerializer(serializers.Serializer):
    
    category_name = serializers.CharField()


class ProductSnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_image', 'starting_price']




class ProductImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = ['image']


class ProductVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = ['video']

    
class MessageSerializer(serializers.Serializer):

    msg = serializers.CharField()
    from_or_to = serializers.BooleanField()


class HaggleClientSerializer(serializers.Serializer):

    name = serializers.CharField()
    client_id = serializers.IntegerField()
    haggle_id = serializers.IntegerField()


class EShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = EShop
        fields = '__all__'


    
class AboutEShopSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    boss = serializers.CharField()
    phone = serializers.CharField()




class EShopExistSerializer(serializers.Serializer):

    eshop_exist = serializers.BooleanField()



class ClientRRSerializer(serializers.Serializer):

    client_name = serializers.CharField()
    client_image = serializers.CharField()
    rating = serializers.IntegerField()
    review = serializers.CharField()



class EShopRRSerializer(serializers.Serializer):

    client_name = serializers.CharField()
    client_image = serializers.CharField()
    rating = serializers.IntegerField()
    review = serializers.CharField()


class FavoriteListClient(serializers.Serializer):

    profile_id = serializers.IntegerField()
    display_pic = serializers.CharField()
    name = serializers.CharField()




class FavoriteListEShop(serializers.Serializer):

    eshop_name = serializers.CharField()
    eshop_id = serializers.IntegerField()
    catchboard = serializers.CharField()


class FavoriteListProduct(serializers.Serializer):

    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    product_image = serializers.CharField()



class ForgotPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForgotPassword 
        fields = '__all__'

    
class ErrorCheckSerializer(serializers.Serializer):

    error_message = serializers.CharField()


class SuccessCodeSerializer(serializers.Serializer):

    code = serializers.IntegerField()


