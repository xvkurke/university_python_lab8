from django.contrib import admin
from .models import Locomotive, Brigade, Repair


@admin.register(Locomotive)
class LocomotiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_number', 'depot', 'locomotive_type', 'year_of_manufacture')
    search_fields = ('reg_number', 'depot', 'locomotive_type')
    list_filter = ('locomotive_type', 'depot', 'year_of_manufacture')
    ordering = ('reg_number',)


@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'brigade_number', 'phone')
    search_fields = ('brigade_number', 'phone')
    ordering = ('brigade_number',)


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('id', 'repair_code', 'reg_number', 'repair_type', 'start_date', 'days_required', 'cost_per_day', 'brigade_number')
    search_fields = ('repair_code', 'repair_type', 'reg_number__reg_number')
    list_filter = ('repair_type', 'start_date', 'brigade_number')
    ordering = ('start_date',)
