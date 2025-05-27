from datetime import datetime

from django.contrib import admin
from .models import *


class AgentEstateInline(admin.TabularInline):
    model = AgentEstate
    extra = 0


class EstateCharacteristicInline(admin.TabularInline):
    model = EstateCharacteristic
    extra = 0


class EstateAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'description']

    inlines = [AgentEstateInline, EstateCharacteristicInline]

    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        super(EstateAdmin, self).save_model(request, obj, form, change)
        if not change:
            AgentEstate.objects.create(agent=Agent.objects.get(user=request.user), estate=obj)

    def has_delete_permission(self, request, obj=None):
        return not EstateCharacteristic.objects.filter(estate=obj).exists()

    def has_change_permission(self, request, obj=None):
        return AgentEstate.objects.filter(agent=Agent.objects.filter(user=request.user).first(), estate=obj).exists()

    def has_view_permission(self, request, obj=None):
        return True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Estate.objects.filter(date=datetime.now().date()).all()
        return Estate.objects.all()


class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']

    def has_add_permission(self, request):
        return request.user.is_superuser


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['name']

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Estate, EstateAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
