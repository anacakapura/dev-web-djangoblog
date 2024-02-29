from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Artikel(models.Model):
    title       = models.CharField(max_length=255)
    body        = models.TextField()
    
    LIST_KATEGORI = (
        ('Nature','Nature'),
        ('Teknologi','Teknologi'),
        ('Politik','Politik'),
        ('-','-')
    )
    kategori = models.CharField(
        max_length=255,
        default='-',
        choices=LIST_KATEGORI
    )
    published   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(blank=True,editable=False)

    # Mengisi slug dengan slugify sebelum di simpan
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        url_slug ={'slug':self.slug}    
        return reverse('artikel:artikel_detail', kwargs=url_slug)

    # Mengetahui query yang sedang di proses
    def __str__(self):
        return "{}. {}.".format(self.id, self.title)