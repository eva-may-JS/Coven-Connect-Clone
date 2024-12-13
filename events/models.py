from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

PERMITTED = ((0, "Yes"), (1, "No"))
STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = ((0, "---"), (1, "Witchcraft for begginers"), (2, "Spells & Rituals"), (3, "Witch-Crafts"), (4, "Music & Dance"), (5, "Foods & Elixirs"), (6, "Markets & Trading"), (7, "Healing & Wellness"), (8, "Dark Arts & Shadow Work"), (9, "Tarot & Divination"), (10, "Other"))

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts")
    category = models.IntegerField(choices=CATEGORY, default=0)
    event_image = CloudinaryField('image', default='placeholder')
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.TextField()
    familiar = models.IntegerField(choices=PERMITTED, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | created by {self.author}"


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.content} by {self.author}"