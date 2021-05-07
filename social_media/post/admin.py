from django.contrib import admin
from post.models import Post, Like, DisLike

"""
    Registered Models
"""
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(DisLike)