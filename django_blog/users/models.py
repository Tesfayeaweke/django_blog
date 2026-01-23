from django.db import models
from django.contrib.auth.models import User
from PIL import Image #pillow

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to= 'profile_pics')
    def __str__(self):
        return f"{self.user}'s profile"
    
    # Override save method to resize image size
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (150,150)
            # The resizing by keeping the aspect ratio.
            img.thumbnail(output_size)
            # It gets saved in the original location.
            img.save(self.image.path)
