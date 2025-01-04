from django.db import models
from django.contrib.auth import get_user_model
from blogs.models import Blog

User = get_user_model()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'comments'
        db_table = 'comment'  # No schema reference here

# This is a comment to force detection

