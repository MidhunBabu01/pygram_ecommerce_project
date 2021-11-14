from django.db import models

# Create your models here.

class AdminProducts(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return str(self.name)

    slug = models.SlugField(max_length = 200)
    
    choices = (
        ('Men-T-Shirts','Men-T-Shirts'),
        ('Shirts','Shirts'),
        ('Men-Jeans','Men-Jeans'),
        ('Women-Jeans','Women-Jeans'),
        ('Men-Watches','Men-Watches'),
        ('Women-Watches','Women-Watches'),
        ('Saree','Saree'),
        ('Churidhar', 'Churidhar'),
        ('Top','Top'),
        ('boys', 'boys'),
        ('girls','girls'),
    )
    subcategory = models.CharField(choices=choices, default='1', max_length=50)
    img1 = models.ImageField(upload_to="pictures")
    img2 = models.ImageField(upload_to="pictures")
    img3 = models.ImageField(upload_to="pictures")
    desc = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    # available = models.BooleanField(default=True)




