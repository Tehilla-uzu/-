from django.db import models
import string
import random

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = ''.join(
                random.choices(string.ascii_letters + string.digits, k=6)
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_code
