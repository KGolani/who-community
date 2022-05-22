from django.db import models

class Feed(models.Model):
    title      = models.CharField(max_length=30)
    detail     = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user       = models.ForeignKey('users',on_delete=models.CASCADE)

    class Meta:
        db_table = 'feeds'

class FeedImages(models.Model):
    image_url = models.CharField(max_length=200)
    feed      = models.ForeignKey('feeds',on_delete=models.CASCADE)

    class Meta:
        db_table = 'feed_images'
# Create your models here.
