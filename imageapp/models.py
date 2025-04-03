from django.db import models

class Image(models.Model):
    original_image = models.ImageField(upload_to='originals/')
    processed_image = models.ImageField(upload_to='processed/', blank=True, null=True)
    filter_applied = models.CharField(max_length=50, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
