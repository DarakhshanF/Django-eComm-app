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

class Tag(models.Model):
    name = models.CharField(max_length=255,
                            help_text='Enter the Tag name')
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='A unique slug for the Tag (no spaces or special characters)')
    created_at = models.DateTimeField(auto_now_add=True,
                                      help_text='The date and time this tag is created')
    updated_at = models.DateTimeField(auto_now=True,
                                      help_text='The date and time this tag is updated')
    
    class Meta:
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255,
                            help_text='Enter the product name')
    description = models.TextField(blank=True,
                                   help_text='Provide a detailed description of the product')
    price = models.DecimalField(max_digits=8,
                                decimal_places=2, help_text='Enter the product price')
    created_at = models.DateTimeField(auto_now_add=True,
                                      help_text='The date and time this category is created')
    updated_at = models.DateTimeField(auto_now=True,
                                      help_text='The date and time this category is updated')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 help_text='Select the product category')
    tags = models.ManyToManyField(Tag, related_name='products', blank=True,
                                  help_text='Select the relevant tags for this product')
    available = models.BooleanField(default=True,
                                    help_text='Uncheck if the product is currently unavailable')
    sku = models.CharField(max_length=50, unique=True,
                           help_text='Enter the unique Stock-Keeping Unit (SKU) for the product')
    brand = models.CharField(max_length=100, blank=True,
                             help_text='Enter the brand name of the product')
    image = models.ImageField(upload_to='product_images', blank=True, null=True,
                              help_text='Upload an image for the product')
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,
                                 help_text='Enter the product weight in kilograms (optional)')
    dimensions = models.CharField(max_length=100, blank=True,
                                  help_text='Enter the product dimensions (e.g., 10x20x30 cm)')
    stock_quantity = models.PositiveIntegerField(default=0,
                                                 help_text='Enter the current stock quantity of the product')
    featured = models.BooleanField(default=False,
                                   help_text='Check to mark this product as featured')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'
        ordering = ['-created_at']

class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE,
                             help_text='User submitting the review')
    content = models.TextField(help_text='Provide your thoughts about the product here')
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE,
                                help_text='Select the product for reviewing')
    created_at = models.DateField(auto_now_add=True,
                                  help_text='The date and time this review is created')
    updated_at = models.DateField(auto_now=True,
                                  help_text='The date and time this review is updated')

    class Meta:
        verbose_name_plural = 'reviews'
        ordering = ['author']
    
    def __str__(self):
        return f"{self.author.email}'s thoughts on {self.product.name}"
