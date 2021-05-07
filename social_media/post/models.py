from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
        Base Model as an Abstract Model
    """
    id = models.AutoField(primary_key=True, )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    """
        Post Model
    """
    INTERACTIONS = (
        ('liked', 'Liked'),
        ('disliked', 'Disliked')
    )
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user', null=True)
    tags = models.CharField(max_length=100, blank=True)
    weight = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=INTERACTIONS, null=True)
    likes = models.ManyToManyField

    class Meta:
        ordering = ['-weight', ]


class Like(BaseModel):
    """
        Like Models
    """
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)


class DisLike(BaseModel):
    """
        DisLike Models
    """
    user = models.ForeignKey(User, related_name='dislikes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='dislikes', on_delete=models.CASCADE)

