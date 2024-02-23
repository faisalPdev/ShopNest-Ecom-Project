from django.db import models

# Create your models here.
# ------------------slider----------------------

class Slider(models.Model):
    DEAL_TYPE=[
        ('Hot Deal','Hot Deal'),
        ('New Arrivals','New Arrivals'),
        ('Best Sellers','Best Sellers'),
        ('New Deal','New Deal'),
    ]

    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to= 'images/slider.jpg')
    discount=models.PositiveIntegerField(default=0,null=True)
    deal=models.CharField(choices=DEAL_TYPE,max_length=255)

    def __str__(self):
        return self.title[:50]

class Banner(models.Model):
    DEAL_TYPE=[
        ('Hot Deal','Hot Deal'),
        ('New Arrivals','New Arrivals'),
        ('Best Sellers','Best Sellers'),
        ('New Deal','New Deal'),
    ]

    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to= 'images/Banner.jpg')
    discount=models.PositiveIntegerField(default=0,null=True)
    deal=models.CharField(choices=DEAL_TYPE,max_length=255)

    def __str__(self):
        return self.title[:50]

class Subbanner_1(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to= 'images/SubBanner_1.jpg')
    free_shipping_from=models.PositiveIntegerField(default=0,null=True)

    def __str__(self):
        return self.title[:50]
