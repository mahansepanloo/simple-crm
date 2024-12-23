from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):  
    name = models.CharField(max_length=255, unique=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="brand_created_by",
        null=True, blank=True
    )

    def __str__(self):  
        return self.name  


class BrandSetting(models.Model):  
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brandsetting_brand')  
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="brandsetting_created_by",
        null=True, blank=True
    )

    def __str__(self):  
        return self.title 
    

class Color(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="color_created_by",
        null=True, blank=True
    )

    def __str__(self):
        return self.name
    


class Employer(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='employer_brand')
    marketing_employer = models.CharField(max_length=255, null=True, blank=True)
    factory_employer = models.CharField(max_length=255, null=True, blank=True)
    imei = models.CharField(max_length=255, unique=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="employer_created_by",
        null=True, blank=True
    )

    def __str__(self):
        return self.name 
    

class Guarantee(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="guarantee_created_by",
        null=True, blank=True
    )

    def __str__(self):
        return self.title
      

class Swaptype(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="swaptype_created_by",
        null=True, blank=True
    )

    def __str__(self):
        return self.title


class SevenConfig(models.Model):
    server_ip = models.GenericIPAddressField(verbose_name='Server IP')
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.server_ip


class RefundType(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="refundtype_created_by", null=True, blank=True

    )
    
    def __str__(self):
        return self.title
    
    
class PaymentType(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="paymenttype_created_by", null=True, blank=True

    )
    
    def __str__(self):
        return self.title
    
    
class PaymentSource(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="paymentsource_created_by", null=True, blank=True
    )

    def __str__(self):
        return self.title
