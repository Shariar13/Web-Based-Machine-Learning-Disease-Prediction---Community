from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin





urlpatterns = [
    path('',views.home,name="home"),
    path('status',views.status,name="status"),
    path('pattern',views.pattern,name="pattern"),
    path('inbox',views.inbox.as_view(),name="inbox"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    path('alzheimer_test',views.alzheimer_test,name="alzheimer_test"),
    path('result',views.result.as_view(),name="result"),
    path('find_doctor',views.find_doctor.as_view(),name="find_doctor"),
    path('community',views.community.as_view(),name="community"),
    path('buddy',views.buddy.as_view(),name="buddy"),
    path('buddy_profile/<int:pk>',views.buddy_profile.as_view(),name="buddy_profile"),
    path('user_chat/<int:pk>',views.user_chat.as_view(),name="user_chat"),
    path('chat_form',views.chat_form,name="chat_form"),
    path('comment_form',views.comment_form,name="comment_form"),
    path('status_form',views.status_form,name="status_form"),
    path('profile',views.profile.as_view(),name="profile"),
    path('edit_profile_picture/<int:pk>',views.edit_profile_picture.as_view(),name="edit_profile_picture"),
    path('change_profile_picture',views.change_profile_picture.as_view(),name="change_profile_picture"),
    path('profile_picture_form',views.profile_picture_form,name="profile_picture_form"),


    
    
]