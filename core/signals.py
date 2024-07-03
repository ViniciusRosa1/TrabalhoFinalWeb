from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Paciente

@receiver(post_save, sender=Paciente)
def create_user_for_paciente(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create(
            username=instance.email,
            email=instance.email,
            first_name=instance.nome
        )
        user.set_password(instance.senha)  # Defina uma senha padrão ou gere uma senha aleatória
        user.save()
        instance.user = user
        instance.save()