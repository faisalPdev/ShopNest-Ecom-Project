from django.db import models
from shortuuid.django_fields  import ShortUUIDField
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import  slugify
from django.dispatch import receiver
 
# Create your models here.
class Category(models.Model):
    cid=ShortUUIDField(unique=True,length=10,max_length=30,prefix="cat",alphabet="abcdefgh12345")
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to= 'images/Category.jpg')   
    
    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))

    def __str__(self):
        return self.title



class Product(models.Model):
    pid=ShortUUIDField(unique=True,length=10,max_length=30,prefix="prod",alphabet="abcdefgh12345")  

    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)  
    title=models.CharField(max_length=255)  
    price=models.PositiveIntegerField(default=0,null=True)
    featured_image=models.CharField(max_length=255)
    discount=models.PositiveIntegerField(default=0,null=True)
    brand=models.CharField(max_length=64)
    available=models.PositiveIntegerField(default=0,null=True)
    description=RichTextField(null=True,blank=True)

    sku=ShortUUIDField(unique=True,length=10,max_length=30,prefix="sku",alphabet="123456789")
    tags=models.CharField(max_length=255,null=True,blank=True)
    slug=models.CharField(max_length=255,null=True,blank=True)

    top_deal_the_day=models.BooleanField(default=False)
    top_featured_product=models.BooleanField(default=False)
    hot_trending_product=models.BooleanField(default=False)
    on_sale_product=models.BooleanField(default=False)

    date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(null=True,blank=True)

    class Meta: 
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.featured_image))
    
    def _str_(self):
        return self.title
    

@receiver(pre_save,sender=Product)
def generate_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        base_slug=slugify(instance.title)
        unique_slug=base_slug
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug=f"{base_slug}-{instance.id}"
        instance.slug=unique_slug



    

class Additional_Information(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True,blank=True)
    spec=models.CharField(max_length=100,null=True,blank=True)
    class Meta: 
        verbose_name_plural = "Additional informations"

class Short_Description(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    description=models.CharField(max_length=100,null=True,blank=True)
    class Meta: 
        verbose_name_plural = "Short Descriptions"

class Additional_Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.CharField(max_length=255)
    class Meta: 
        verbose_name_plural = "Product Images"




