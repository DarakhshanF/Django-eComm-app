from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            help_text='Enter the category name')
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='A unique slug for the category (no spaces or special characters)')
    description = models.TextField(blank=True,
                                   help_text='Optional description of the category')
    is_active = models.BooleanField(default=True,
                                    help_text='Uncheck to deactivate the category')
    created_at = models.DateTimeField(auto_now_add=True,
                                      help_text='The date and time this category is created')
    updated_at = models.DateTimeField(auto_now=True,
                                      help_text='The date and time this category is updated')
    image = models.ImageField(upload_to='category_images', blank=True,
                              null=True,
                              help_text='Optional image for the category')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children',
                               blank=True, null=True,
                               help_text='Select a parent category, if applicable')

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name
