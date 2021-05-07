from post import views
from django.urls import path


app_name = 'post'


# URLS for Posts
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list_view'),
    path('liked', views.LikeList.as_view(), name='liked_post'),
    path('disliked', views.DisLikeList.as_view(), name='disliked_post'),
    path('like', views.LikePost.as_view(), name='like_post'),
    path('dislike', views.DisLikePost.as_view(), name='dislike_post')
]