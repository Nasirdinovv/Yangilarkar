from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User





class User_profile(models.Model):
    class Status(models.TextChoices):
        ADMIN = 'A', 'Admin'
        USER = 'U', 'User'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField   (choices=Status.choices, default=Status.USER)
    



class News(models.Model):
    title = models.CharField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="author_news")
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category_news")
    time = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="news_images", blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

class Author(models.Model):
    full_name = models.CharField(max_length=36)
    image = models.ImageField(upload_to="author_images", blank=True, null=True)

class Category(models.Model):
    title = models.CharField()

class Likes(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE, related_name="user_likes")

    class Meta:    
        constraints = [

            models.UniqueConstraint(
                fields=['news', 'user'], 
                name='unique_likes'
            ),
        ]