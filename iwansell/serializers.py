from rest_framework import serializers
from .models import Account, AlternatePhone, Category, SubCategory, Campus, Sponsored, Product, EShop, RateReview, Trending, Media, Blog, PaymentMethod, ForgotPassword, Listing, Thread, Comment, Reply





class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'






class AddAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['firstname','lastname','phone','campus','password']






class AlternatePhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlternatePhone
        fields = '__all__'







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
        fields = ['id', 'product_image', 'product_name', 'starting_price']















class EShopStoreSerializer(serializers.ModelSerializer):

   class Meta:
       model = Product
       fields = ['id','product_name', 'product_image', 'starting_price']













class SponsoredSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsored
        fields = ['product_image']

    











class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = '__all__'














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













class ListingSerializer(serializers.Serializer):
     
    product_name = serializers.CharField()
    product_description = serializers.CharField()
    product_image = serializers.CharField()
    budget = serializers.CharField()
    phone = serializers.CharField()












class ListingProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = '__all__'
















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
    dp = serializers.CharField()
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









class TransactionSerializer(serializers.Serializer):

    transaction_id = serializers.IntegerField()
    seller = serializers.CharField()
    token = serializers.CharField()
    product_name = serializers.CharField()
    product_image = serializers.CharField()
    agreed_price = serializers.CharField()
    payment_method = serializers.CharField()
    quantity = serializers.IntegerField()












class BuyerSerializer(serializers.Serializer):

    transaction_id = serializers.IntegerField()
    buyer = serializers.CharField()














class ReceiptSerializer(serializers.Serializer):

    transaction_id = serializers.IntegerField()
    seller = serializers.CharField()
    buyer = serializers.CharField()
    token = serializers.CharField()
    product_name = serializers.CharField()
    product_image = serializers.CharField()
    price = serializers.CharField()
    payment_method = serializers.CharField()
    quantity = serializers.IntegerField()
    campus_code = serializers.CharField()
    date = serializers.CharField()
















class BusinessSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    product_name = serializers.CharField()
    frequency = serializers.IntegerField()













class ProductValuationSerializer(serializers.Serializer):

    searched_frequency = serializers.IntegerField()
    notFound_frequency = serializers.IntegerField()
    forSell_frequency = serializers.IntegerField()
    sold_frequency = serializers.IntegerField()
















class ThreadSerializer(serializers.Serializer):

    firstname = serializers.CharField()
    lastname = serializers.CharField()
    title = serializers.CharField()
    thread_id = serializers.IntegerField()
    thread = serializers.CharField()
    media = serializers.CharField()
    logo = serializers.CharField()
    votes = serializers.IntegerField()
    comment_count = serializers.IntegerField()
    channel_id = serializers.IntegerField()
    channel = serializers.CharField()
    following = serializers.CharField()
    date = serializers.CharField()















class CommentSerializer(serializers.Serializer):

    firstname = serializers.CharField()
    lastname = serializers.CharField()
    dp = serializers.CharField()
    comment_id = serializers.IntegerField()
    comment = serializers.CharField()
    comment_count = serializers.IntegerField()
    votes = serializers.IntegerField()
    date = serializers.CharField()

















class ReplySerializer(serializers.Serializer):

    firstname = serializers.CharField()
    lastname = serializers.CharField()
    dp = serializers.CharField()
    reply_id = serializers.IntegerField()
    reply = serializers.CharField()
    reply_count = serializers.IntegerField()
    votes = serializers.IntegerField()
    date = serializers.CharField()
