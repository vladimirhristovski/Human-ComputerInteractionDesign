from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver
from .models import *


@receiver(pre_save, sender=Estate)
def handle_sold(sender, instance, **kwargs):
    estate_old = Estate.objects.filter(pk=instance.pk).first()
    if estate_old:
        if estate_old.sold == False and instance.sold == True:
            agents_estates = AgentEstate.objects.filter(estate=estate_old).all()
            for agent_estate in agents_estates:
                agent = Agent.objects.filter(pk=agent_estate.agent.pk).first()
                agent.sales += 1
                agent.save()


@receiver(post_save, sender=EstateCharacteristic)
def handle_price(sender, instance, **kwargs):
    estate = EstateCharacteristic.objects.filter(pk=instance.pk).first().estate
    characteristics = EstateCharacteristic.objects.filter(estate=estate).all()
    estate.price = 0
    estate.characteristics = ''
    for characteristic in characteristics:
        estate.price += characteristic.characteristic.value
        estate.characteristics += characteristic.characteristic.name + ', '
    estate.save()
