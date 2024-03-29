from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')


#Apresenta o username do utilizador mais o template do profile
	def __str__(self):
		return f'{self.user.username} Profile'

#guarda as fotos e define o maximo do altura e largura das imagens
	def save(self, *args, **kwargs): 
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)