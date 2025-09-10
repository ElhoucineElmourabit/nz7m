from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    
    # store Supabase URL
    request_photo = models.URLField(max_length=500, null=True, blank=True)
    
    # Track if the order is finished
    order_finished = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.phone_number})"