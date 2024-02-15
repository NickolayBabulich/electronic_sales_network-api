from django.db import models


class Supplier(models.Model):
    type_for_choice = [
        ('factory', 'Завод'),
        ('retail_network', 'Розничная сеть'),
        ('individual_entrepreneur', 'Индивидуальный предприниматель')
    ]
    type = models.CharField(max_length=50, choices=type_for_choice, verbose_name='Тип')
    name = models.CharField(max_length=100, verbose_name='Название поставщика')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    building_number = models.CharField(max_length=10, verbose_name='Номер здания')

    def __str__(self):
        return f'{self.get_type_display()} - {self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=150, verbose_name='Модель')
    date_of_product = models.DateField(verbose_name='Дата выхода')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик',
                                 related_name='product_supplier')

    def __str__(self):
        return f'{self.name} - {self.supplier}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CommercialNetwork(models.Model):
    type_for_choice = [
        ('factory', 'Завод'),
        ('retail_network', 'Розничная сеть'),
        ('individual_entrepreneur', 'Индивидуальный предприниматель')
    ]
    type = models.CharField(max_length=50, choices=type_for_choice, verbose_name='Тип')
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    building_number = models.CharField(max_length=10, verbose_name='Номер здания')
    products = models.ManyToManyField(Product, related_name='networks', verbose_name='Продукт')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='networks_supplier',
                                 verbose_name='Поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2,
                                           verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.get_type_display()} - {self.name}'

    class Meta:
        verbose_name = 'Сеть продаж'
        verbose_name_plural = 'Сети продаж'
