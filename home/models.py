from django.db import models
from django.contrib.auth.models import User

class post (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    status = models.TextField (null=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    date = models.DateTimeField (auto_now_add=True,null = True)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return None

class user_comment (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    post_id = models.IntegerField ()
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField (auto_now_add=True,null = True)
    comment_count = models.IntegerField (null = True, default=1)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class edit_profile (models.Model):
    username = models.CharField(max_length=99)
    name = models.CharField (max_length=99, null=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    date = models.DateTimeField (auto_now_add=True,null = True)

    def __str__(self):
        if len(self.username)>50:
            return self.username[:50]+"..."
        return self.username

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return None

class chat (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    chat_user_name = models.CharField (max_length=99)
    chat_name = models.CharField (max_length=99)
    message = models.TextField (null=True)
    date = models.DateTimeField (auto_now_add=True)
    only_date = models.DateField (auto_now_add=True)
    friend_count = models.IntegerField (null = True, default=1)

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class doctor (models.Model):
    username = models.CharField (max_length=99)
    name = models.CharField (max_length=99)
    phone = models.CharField (max_length=99)
    email = models.CharField (max_length=99)
    location = models.CharField (max_length=99)
    photo = models.ImageField (null = True)
    information = models.TextField ()

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name
