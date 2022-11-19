from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)

