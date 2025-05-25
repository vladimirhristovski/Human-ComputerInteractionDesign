from datetime import datetime

from django.contrib import admin
from .models import Estate, Agent, Characteristic, AgentsEstates, EstatesCharacteristics


class AgentsEstatesInline(admin.TabularInline):
    model = AgentsEstates
    extra = 0


class EstatesCharacteristicsInline(admin.TabularInline):
    model = EstatesCharacteristics
    extra = 0


class EstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'area')
    exclude = ('characteristic',)
    inlines = [AgentsEstatesInline, EstatesCharacteristicsInline]

    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            AgentsEstates.objects.create(agent=Agent.objects.filter(user=request.user).first(), estate=obj)

    def has_delete_permission(self, request, obj=None):
        return not EstatesCharacteristics.objects.filter(estate=obj).exists()

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return obj and AgentsEstates.objects.filter(estate=obj, agent__user=request.user).exists()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Estate.objects.filter(date=datetime.now().date())
        return Estate.objects.all()


class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

    def has_add_permission(self, request):
        return request.user.is_superuser


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('characteristic', 'price')

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Estate, EstateAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
