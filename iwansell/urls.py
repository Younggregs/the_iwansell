from django.conf.urls import url
from rest_framework.authtoken import views as drf_views

from . import views
app_name = 'iwansell'

urlpatterns = [
    #auth/
    url(r'^auth/$', drf_views.obtain_auth_token, name='auth'),

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

    #iwansell/eshop_category/eshop_id
    url(r'^eshop_category/(?P<eshop_id>[0-9]+)/$',views.EShopCategoryView.as_view(), name = 'eshop-category-view'),

    #iwansell/my_eshopid/
    url(r'^my_eshopid/$',views.MyEShopID.as_view(), name = 'my-eshop-id'),

    #iwansell/eshop_list/campus_id
    url(r'^eshop_list/(?P<campus_id>[0-9]+)/$',views.EShopList.as_view(), name = 'eshop_list'),

    #iwansell/campus_code
    url(r'^campus_code/(?P<campus_id>[0-9]+)/$',views.CampusCode.as_view(), name = 'campus_code'),

    #iwansell/eshop_list_category
    url(r'^eshop_list_category/(?P<campus_id>[0-9]+)/(?P<category_id>[0-9]+)/$',views.EShopListCategory.as_view(), name = 'eshop_list_category'),

    #iwansell/eshop_subcategory/eshop_id
    url(r'^eshop_subcategory/(?P<eshop_id>[0-9]+)/$',views.EShopSubCategory.as_view(), name = 'eshop-subcategory'),

    #iwansell/about_eshop/eshop_id
    url(r'^about_eshop/(?P<eshop_id>[0-9]+)/$',views.AboutEShop.as_view(), name = 'about_eshop'),

    #iwansell/category
    url(r'^category/$',views.CategoryView.as_view(), name = 'category'),

    #iwansell/category_product
    url(r'^category_product/(?P<campus_id>[0-9]+)/(?P<category_id>[0-9]+)/(?P<show_more>[0-9]+)/$',views.CategoryProduct.as_view(), name = 'categoryproduct'),

    #iwansell/subcategory
    url(r'^subcategory/(?P<category_id>[0-9]+)/$',views.SubCategoryView.as_view(), name = 'subcategory'),

    #iwansell/subcategory_main
    url(r'^subcategory_main/$',views.SubCategoryMain.as_view(), name = 'subcategory_main'),

    #iwansell/subcategory_product
    url(r'^subcategory_product/(?P<campus_id>[0-9]+)/(?P<subcategory_id>[0-9]+)/$',views.SubCategoryProduct.as_view(), name = 'subcategory_product'),

    #iwansell/sub_category_icons
    url(r'^sub_category_icons/$',views.SubCategoryIcon.as_view(), name = 'subcategoryicons'),

    #iwansell/campus
    url(r'^campus/$',views.CampusView.as_view(), name = 'campus'),

    #iwansell/campus
    url(r'^campus_search/$',views.CampusSearch.as_view(), name = 'campus_search'),

    #iwansell/update_dp
    url(r'^update_dp/$',views.UpdateDP.as_view(), name = 'update-dp'),

    #iwansell/update_password
    url(r'^update_password/$',views.UpdatePassword.as_view(), name = 'update-password'),

    #iwansell/newproduct
    url(r'^newproduct/(?P<account_id>[0-9]+)/$',views.NewProductView.as_view(), name = 'new-product'),

    #iwansell/new_listing
    url(r'^new_listing/(?P<account_id>[0-9]+)/$',views.NewListingView.as_view(), name = 'new-listing'),

    #iwansell/listings
    url(r'^listings/(?P<campus_id>[0-9]+)/$',views.ListingView.as_view(), name = 'listing'),

    #iwansell/listing_category
    url(r'^listing_category/(?P<campus_id>[0-9]+)/(?P<category_id>[0-9]+)/$',views.ListingCategory.as_view(), name = 'listing_category'),

    #iwansell/listing_product
    url(r'^listing_product/$',views.ListingProduct.as_view(), name = 'listing_product'),

    #iwansell/remove_listing
    url(r'^remove_listing/(?P<product_id>[0-9]+)/(?P<status>[0-9]+)/$',views.RemoveListing.as_view(), name = 'remove_listing'),

    #iwansell/media_upload
    url(r'^media_upload/(?P<product_id>[0-9]+)/$',views.MediaUpload.as_view(), name = 'media-upload'),

    #iwansell/product_list
    url(r'^product_list/$',views.ProductList.as_view(), name = 'product-list'),

    #iwansell/payment_name
    url(r'^product_name/(?P<product_id>[0-9]+)/$',views.ProductName.as_view(), name = 'product-name'),

    #iwansell/payment_method
    url(r'^payment_method/$',views.PaymentMethodView.as_view(), name = 'payment_method'),

    #iwansell/initiate_transaction
    url(r'^initiate_transaction/$',views.InitiateTransaction.as_view(), name = 'initiate_transaction'),

    #iwansell/confirm_buyer
    url(r'^confirm_buyer/$',views.ConfirmBuyer.as_view(), name = 'confirm_buyer'),

    #iwansell/confirm_transaction_seller
    url(r'^confirm_transaction_seller/$',views.ConfirmTransactionSeller.as_view(), name = 'confirm-transaction-seller'),

    #iwansell/receipt
    url(r'^receipt/(?P<transaction_id>[0-9]+)/$',views.Receipt.as_view(), name = 'receipt'),

    #iwansell/join_transaction
    url(r'^join_transaction/$',views.JoinTransaction.as_view(), name = 'join-transaction'),

    #iwansell/confirm_transaction_buyer
    url(r'^confirm_transaction_buyer/(?P<transaction_id>[0-9]+)/$',views.ConfirmTransactionBuyer.as_view(), name = 'confirm-transaction-buyer'),

    #iwansell/transaction_status
    url(r'^transaction_status/$',views.TransactionStatus.as_view(), name = 'transaction-status'),

    #iwansell/eshop_product_list
    url(r'^eshop_product_list/$',views.EShopProductList.as_view(), name = 'eshop-product-list'),

    #iwansell/product_images
    url(r'^product_images/(?P<product_id>[0-9]+)/$',views.ProductImages.as_view(), name = 'product-images'),

    #iwansell/product_video
    url(r'^product_video/(?P<product_id>[0-9]+)/$',views.ProductVideo.as_view(), name = 'product-video'),

    #iwansell/search/category_id/search_phrase
    url(r'^search/(?P<campus_id>[0-9]+)/(?P<category_id>[0-9]+)/$',views.Search.as_view(), name = 'search'),

    #iwansell/trending
    url(r'^trending/(?P<campus_id>[0-9]+)/(?P<trending_url>\w+)/$',views.TrendingView.as_view(), name = 'trending'),

    #iwansell/sponsored
    url(r'^sponsored/(?P<campus_id>[0-9]+)/$',views.SponsoredView.as_view(), name = 'sponsored'),

    #iwansell/product
    url(r'^product/(?P<product_id>[0-9]+)/$',views.ProductView.as_view(), name = 'product'),

    #iwansell/haggleclients
    url(r'^haggleclients/$',views.HaggleClients.as_view(), name = 'haggle-clients'),

    #iwansell/haggleclients
    url(r'^new_hagglers/(?P<client_id>[0-9]+)/$',views.NewHaggler.as_view(), name = 'new-haggler'),

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

    #iwansell/rating/eshop_id
    url(r'^rating/(?P<eshop_id>[0-9]+)/$',views.Rating.as_view(), name = 'rating'),

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

    #iwansell/blog_post
    url(r'^blog_post/(?P<blog_id>[0-9]+)/$',views.BlogPost.as_view(), name = 'category-blog'),

    #iwansell/category_blog 
    url(r'^category_blog/(?P<category_id>[0-9]+)/$',views.CategoryBlog.as_view(), name = 'category-blog'),

    #iwansell/blog_top
    url(r'^blog_top/$',views.BlogTop.as_view(), name = 'blog-top'),

    #iwansell/recent_blog_post
    url(r'^recent_blog_post/$',views.RecentBlogPost.as_view(), name = 'recent-blog-post'),

    #iwansell/blog_snippet
    url(r'^blog_snippet/$',views.BlogSnippet.as_view(), name = 'blog-snippet'),

    #iwansell/top_sold
    url(r'^top_sold/$',views.TopSoldView.as_view(), name = 'top-sold-view'),

    #iwansell/top_search_product
    url(r'^top_search_product/$',views.TopSearchedView.as_view(), name = 'top-searched-view'),

    #iwansell/top_not_found
    url(r'^top_not_found/$',views.TopNotFoundView.as_view(), name = 'top-not-found-view'),

    #iwansell/top_for_sell
    url(r'^top_for_sell/$',views.TopForSellView.as_view(), name = 'top-for-sell-view'),

    #iwansell/least_sold
    url(r'^least_sold/$',views.LeastSoldView.as_view(), name = 'least-sold-view'),

    #iwansell/least_for_sell
    url(r'^least_for_sell/$',views.LeastForSellView.as_view(), name = 'least-for-sell-view'),

    #iwansell/product_valuation
    url(r'^product_valuation/$',views.ProductValuation.as_view(), name = 'product-valuation'),

    #iwansell/alternate_phone
    url(r'^alternate_phone/$',views.AlternatePhoneView.as_view(), name = 'alternate-phone'),

    #iwansell/alternate_phone_seller
    url(r'^alternate_phone_seller/(?P<account_id>[0-9]+)/$',views.AlternatePhoneSellerView.as_view(), name = 'alternate-phone-seller'),

    #iwansell/get_phone
    url(r'^get_phone/$',views.GetPhone.as_view(), name = 'get-phone'),

    #iwansell/channel
    url(r'^channel/(?P<campus_id>[0-9]+)/$',views.ChannelView.as_view(), name = 'channel'),

    #iwansell/get_channel
    url(r'^get_channel/$',views.GetChannel.as_view(), name = 'getchannel'),

    #iwansell/thread
    url(r'^thread/(?P<thread_id>[0-9]+)/$',views.ThreadView.as_view(), name = 'thread'),

    #iwansell/comment/1
    url(r'^comment/(?P<thread_id>[0-9]+)/$',views.CommentView.as_view(), name = 'comment-view'),

    #iwansell/reply/1
    url(r'^reply/(?P<comment_id>[0-9]+)/$',views.ReplyView.as_view(), name = 'reply-view'),

    #iwansell/reply_1/1
    url(r'^reply_1/(?P<reply_id>[0-9]+)/$',views.Reply1View.as_view(), name = 'reply-1-view'),

    #iwansell/reply_2/1
    url(r'^reply_2/(?P<reply_id>[0-9]+)/$',views.Reply2View.as_view(), name = 'reply-3-view'),

    #iwansell/reply_3/1
    url(r'^reply_3/(?P<reply_id>[0-9]+)/$',views.Reply3View.as_view(), name = 'reply-3-view'),

    #iwansell/reply_4/1
    url(r'^reply_4/(?P<reply_id>[0-9]+)/$',views.Reply4View.as_view(), name = 'reply-4-view'),

    #iwansell/follow
    url(r'^follow/(?P<channel_id>[0-9]+)/$',views.FollowView.as_view(), name = 'follow'),

    #iwansell/vote
    url(r'^vote/(?P<toggle>[0-9]+)/(?P<thread_id>[0-9]+)/$',views.VoteView.as_view(), name = 'vote-view'),

    #iwansell/vote_comment
    url(r'^vote_comment/(?P<toggle>[0-9]+)/(?P<comment_id>[0-9]+)/$',views.VoteComment.as_view(), name = 'vote-comment'),

    #iwansell/vote_reply
    url(r'^vote_reply/(?P<toggle>[0-9]+)/(?P<reply_id>[0-9]+)/$',views.VoteReply.as_view(), name = 'vote-reply'),

    #iwansell/vote_reply
    url(r'^vote_reply_1/(?P<toggle>[0-9]+)/(?P<reply_id>[0-9]+)/$',views.VoteReply1.as_view(), name = 'vote-reply-1'),

    #iwansell/vote_reply
    url(r'^vote_reply_2/(?P<toggle>[0-9]+)/(?P<reply_id>[0-9]+)/$',views.VoteReply2.as_view(), name = 'vote-reply-2'),

    #iwansell/vote_reply
    url(r'^vote_reply_3/(?P<toggle>[0-9]+)/(?P<reply_id>[0-9]+)/$',views.VoteReply3.as_view(), name = 'vote-reply-3'),

    #iwansell/vote_reply
    url(r'^vote_reply_4/(?P<toggle>[0-9]+)/(?P<reply_id>[0-9]+)/$',views.VoteReply4.as_view(), name = 'vote-reply-4'),

    #iwansell/forgot_password
    url(r'^forgot_password/$',views.ForgotPasswordView.as_view(), name = 'forgot-password'),

    #iwansell/forgot_password
    url(r'^reset_password/(?P<reset_code>\w+)/$',views.ResetPassword.as_view(), name = 'reset-password'),

    #iwansell/logout
    url(r'^logout/$', views.logout, name='logout'),

]
