from django.contrib import admin
from App_Posts.models import Post, Likes
# Register your models here.

admin.site.register(Post)
admin.site.register(Likes)