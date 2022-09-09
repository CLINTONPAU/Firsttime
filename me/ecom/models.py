from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    brand=models.CharField(max_length=500)
    model=models.CharField(max_length=500)
    network_technology=models.CharField(max_length=500)
    t2G_bands=models.CharField(max_length=500)
    t3G_bands=models.CharField(max_length=500)
    t4G_bands=models.CharField(max_length=500)
    network_speed=models.CharField(max_length=500)
    GPRS=models.CharField(max_length=500)
    EDGE=models.CharField(max_length=500)
    announced=models.CharField(max_length=500)
    status=models.CharField(max_length=500)
    dimentions=models.CharField(max_length=500)
    weight_g=models.CharField(max_length=500)
    weight_oz=models.CharField(max_length=500)
    SIM=models.CharField(max_length=500)
    display_type=models.CharField(max_length=500)
    display_resolution=models.CharField(max_length=500)
    display_size=models.CharField(max_length=500)
    OS=models.CharField(max_length=500)
    CPU=models.CharField(max_length=500)
    Chipset=models.CharField(max_length=500)
    GPU=models.CharField(max_length=500)
    memory_card=models.CharField(max_length=500)
    internal_memory=models.CharField(max_length=500)
    RAM=models.CharField(max_length=500)
    primary_camera=models.CharField(max_length=500)
    secondary_camera=models.CharField(max_length=500)
    loud_speaker=models.CharField(max_length=500)
    audio_jack=models.CharField(max_length=500)
    WLAN=models.CharField(max_length=500)
    bluetooth=models.CharField(max_length=500)
    GPS=models.CharField(max_length=500)
    NFC=models.CharField(max_length=500)
    radio=models.CharField(max_length=500)
    USB=models.CharField(max_length=500)
    sensors=models.CharField(max_length=500)
    battery=models.CharField(max_length=500)
    colors=models.CharField(max_length=500)
    approx_price=models.IntegerField(default=None)
    img_url=models.CharField(max_length=500)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    def __str__(self):
        return self.brand


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=500)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
