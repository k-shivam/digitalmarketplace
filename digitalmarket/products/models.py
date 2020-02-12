from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=6.99, null=True, blank=True)

    def __str__(self):
        return self.title


def products_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug='some-slug'


pre_save.connect(products_signal, sender=Product)



def products_post_save_signal(sender, instance, *args, **kwargs):
    if instance.slug != slugify(instance.title):
        instance.slug=slugify(instance.title)
        instance.save()


post_save.connect(products_post_save_signal, sender=Product)