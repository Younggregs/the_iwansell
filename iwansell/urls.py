from django.conf.urls import url
from rest_framework.authtoken import views as drf_views

from . import views
app_name = 'iwansell'

urlpatterns = [
    #auth/
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),

    #iwansell/
    url(r'^$',views.index, name = 'index'),

    #iwansell/accounts
    url(r'^accounts/$',views.AddAccount.as_view(), name = 'add-account'),

    #iwansell/signin
    url(r'^signin/$',views.SignIn.as_view(), name = 'sign-in'),

    #iwansell/600
    url(r'^accounts/(?P<account_id>[0-9]+)/$',views.AccountDetail.as_view(), name = 'account-detail'),

    #iwansell/reset_dp
    url(r'^reset_dp/$',views.ResetDP.as_view(), name = 'reset-dp'),

    #iwansell/signin
    url(r'^update_password/$',views.UpdatePassword.as_view(), name = 'update-password'),

    #iwansell/signin
    url(r'^reset_phone/$',views.ResetPhone.as_view(), name = 'reset-phone'),

    #iwansell/isloggedin
    url(r'^isloggedin/$',views.IsLoggedIn.as_view(), name = 'is-logged-in'),

    #iwansell/ismyaccount/profile_id
    url(r'^is_myprofile/(?P<profile_id>[0-9]+)/$',views.IsMyProfile.as_view(), name = 'is-my-profile'),

     #iwansell/ismyaccount/profile_id
    url(r'^myaccount_id/$',views.MyAccountID.as_view(), name = 'my-account-id'),

    #iwansell/ismyeshop/eshop_id
    url(r'^ismyeshop/(?P<eshop_id>[0-9]+)/$',views.IsMyEShop.as_view(), name = 'is-my-eshop'),

    #iwansell/ismyeshop/eshop_id
    url(r'^my_eshopid/$',views.MyEShopID.as_view(), name = 'my-eshop-id'),

    #iwansell/category
    url(r'^category/$',views.CategoryView.as_view(), name = 'category'),

    #iwansell/subcategory
    url(r'^subcategory/(?P<category_id>[0-9]+)/$',views.SubCategoryView.as_view(), name = 'category'),

    #iwansell/campus
    url(r'^campus/$',views.CampusView.as_view(), name = 'campus'),

    #iwansell/update_dp
    url(r'^update_dp/$',views.UpdateDP.as_view(), name = 'update-dp'),

    #iwansell/update_password
    url(r'^update_password/$',views.UpdatePassword.as_view(), name = 'update-password'),

    #iwansell/newproduct
    url(r'^newproduct/(?P<account_id>[0-9]+)/$',views.NewProductView.as_view(), name = 'new-product'),

    #iwansell/product_list
    url(r'^product_list/$',views.ProductList.as_view(), name = 'product-list'),

    #iwansell/product_list
    url(r'^eshop_product_list/$',views.EShopProductList.as_view(), name = 'eshop-product-list'),

    #iwansell/product_images
    url(r'^product_images/(?P<product_id>[0-9]+)/$',views.ProductImages.as_view(), name = 'product-images'),

    #iwansell/product_video
    url(r'^product_video/(?P<product_id>[0-9]+)/$',views.ProductVideo.as_view(), name = 'product-video'),

    #iwansell/search/category_id/search_phrase
    url(r'^search/(?P<campus_id>[0-9]+)/(?P<category_id>[0-9]+)/(?P<search_phrase>\w+)/$',views.Search.as_view(), name = 'search'),

    #iwansell/trending
    url(r'^trending/(?P<campus_id>[0-9]+)/(?P<category>\w+)/$',views.TrendingView.as_view(), name = 'trending'),

    #iwansell/sponsored
    url(r'^sponsored/(?P<campus_id>[0-9]+)/$',views.SponsoredView.as_view(), name = 'sponsored'),

    #iwansell/product
    url(r'^product/(?P<product_id>[0-9]+)/$',views.ProductView.as_view(), name = 'product'),

    #iwansell/haggleclients
    url(r'^haggleclients/$',views.HaggleClients.as_view(), name = 'haggle-clients'),

    #iwansell/haggleclients
    url(r'^new_hagglers/(?P<client_id>[0-9]+)/$',views.NewHagglers.as_view(), name = 'new-hagglers'),

    #iwansell/messenger
    url(r'^messenger/(?P<client_id>[0-9]+)/$',views.MessengerView.as_view(), name = 'messenger'),

    #iwansell/messenger
    url(r'^unread_messages/$',views.UnreadMessages.as_view(), name = 'unread-messages'),

    #iwansell/send_message
    url(r'^send_message/(?P<client_id>[0-9]+)/$',views.SendMessage.as_view(), name = 'send-message'),

    #iwansell/new_eshop
    url(r'^new_eshop/$',views.NewEShop.as_view(), name = 'new-eshop'),

    #iwansell/have_eshop
    url(r'^have_eshop/$',views.HaveEShop.as_view(), name = 'have-eshop'),

    #iwansell/eshop
    url(r'^eshop/(?P<eshop_id>[0-9]+)/$',views.EShopView.as_view(), name = 'eshop'),

    #iwansell/eshop
    url(r'^eshop_subcategory/(?P<eshop_id>[0-9]+)/$',views.EShopSubCategory.as_view(), name = 'eshop-subcategory'),

    #iwansell/eshop
    url(r'^eshop_store/(?P<eshop_id>[0-9]+)/(?P<subcategory_id>[0-9]+)/$',views.EShopStore.as_view(), name = 'eshop-store'),

    #iwansell/eshop
    url(r'^eshop_search/(?P<eshop_id>[0-9]+)/(?P<search_phrase>\w+)/$',views.EShopSearch.as_view(), name = 'eshop-search'),

    #iwansell/eshop
    url(r'^edit_eshop/$',views.EditEShop.as_view(), name = 'edit-eshop'),

    #iwansell/eshop_exist
    url(r'^eshop_exist/$',views.EShopExist.as_view(), name = 'eshop-exist'),

    #iwansell/new_eshop_product
    url(r'^new_eshop_product/(?P<account_id>[0-9]+)/$',views.NewEShopProduct.as_view(), name = 'new-eshop-product'),

    #iwansell/rate_review/status_code/id
    url(r'^rate_review/(?P<status_code>[0-9]+)/(?P<id>[0-9]+)/$',views.RRView.as_view(), name = 'rr-view'),

    #iwansell/rate_review/status_code/id
    url(r'^rate_review_form/(?P<status_code>[0-9]+)/(?P<id>[0-9]+)/$',views.RRViewForm.as_view(), name = 'rr-view-form'),

    #iwansell/soldproduct
    url(r'^sold_product/(?P<product_id>[0-9]+)/$',views.SoldProduct.as_view(), name = 'sold-product'),

    #iwansell/removeproduct
    url(r'^remove_product/(?P<product_id>[0-9]+)/$',views.RemovedProduct.as_view(), name = 'remove-product'),

    #iwansell/favorite/status_code/id
    url(r'^favorite/(?P<status_code>[0-9]+)/(?P<id>[0-9]+)/$',views.FavoriteView.as_view(), name = 'favorite'),

    #iwansell/favorite_list/status_code/id
    url(r'^favorite_list/(?P<status_code>[0-9]+)/(?P<profile_id>[0-9]+)/$',views.FavoriteList.as_view(), name = 'favorite-list'),

    #iwansell/get_account
    url(r'^get_account/$',views.GetAccount.as_view(), name = 'get-account'),

    #iwansell/get_campus
    url(r'^get_campus/$',views.GetCampus.as_view(), name = 'get-campus'),

    #iwansell/forgot_password
    url(r'^forgot_password/$',views.ForgotPasswordView.as_view(), name = 'forgot-password'),

    #iwansell/forgot_password
    url(r'^reset_password/(?P<reset_code>[0-9]+)/$',views.ResetPassword.as_view(), name = 'reset-password'),

    #iwansell/logout
    url(r'^logout/$', views.logout, name='logout'),
]
