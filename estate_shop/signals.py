from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Estate, EstatesCharacteristics, Characteristic, AgentsEstates


@receiver(pre_save, sender=Estate)
def handle_sold(sender, instance, **kwargs):
    old_instance = sender.objects.filter(id=instance.id).first()
    if old_instance:
        if old_instance.sold != instance.sold:
            agents_real_estate = AgentsEstates.objects.filter(estate=old_instance).all()
            for agent_real_estate in agents_real_estate:
                agent = agent_real_estate.agent
                agent.sales += 1
                agent.save()


@receiver([post_save, post_delete], sender=EstatesCharacteristics)
def handle_saving_house(sender, instance, **kwargs):
    all_characteristics = sender.objects.filter(estate=instance.estate).all()
    if all_characteristics:
        real_estate = all_characteristics[0].estate
        real_estate.characteristic = ", ".join(char.characteristic.characteristic for char in all_characteristics)
        real_estate.save()
