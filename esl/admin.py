from django.contrib import admin, messages
from esl.models import Supplier, Product, CommercialNetwork


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Supplier._meta.fields]
    list_display_links = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_display_links = ['name']


@admin.register(CommercialNetwork)
class CommercialNetworkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CommercialNetwork._meta.fields]
    list_display_links = ('name',)
    list_filter = ['city']
    actions = ['clear_debt_to_supplier', 'delete_selected']

    @admin.action(description='Очистить задолженность:')
    def clear_debt_to_supplier(self, request, queryset):
        if_debt = False
        for object in queryset:
            if object.debt_to_supplier > 0:
                object.debt_to_supplier = 0
                if_debt = True
                object.save()

        if if_debt:
            messages.success(request, f'Задолженность погашена')
        else:
            messages.warning(request, f'Задолженность уже была погашена')
