from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# quando um user é criado é mandado um sinal, 
# onde o receiver(neste caso o create_profile) recebe e toma em conta todas os argumentos
# e se o utilizador foi criado, é criado um perfil para este utilizador 
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


# quando um user é criado é mandado um sinal, 
# onde o receiver(neste caso o save_profile) recebe e toma em conta todas os argumentos
# e quando o utilizador muda o conteudo do perfil e guarda, o perfil é guardado 
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()