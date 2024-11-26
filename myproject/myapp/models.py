from django.db import models

class Locomotive(models.Model):
    reg_number = models.CharField(max_length=50, unique=True, verbose_name="Реєстраційний номер")
    depot = models.CharField(max_length=100, verbose_name="Депо")
    locomotive_type = models.CharField(max_length=50, verbose_name="Тип локомотива")
    year_of_manufacture = models.PositiveIntegerField(verbose_name="Рік виготовлення")

    class Meta:
        db_table = 'locomotives'  # Назва таблиці

    def __str__(self):
        return self.reg_number


class Brigade(models.Model):
    brigade_number = models.PositiveIntegerField(unique=True, verbose_name="Номер бригади")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    class Meta:
        db_table = 'brigades'  # Назва таблиці

    def __str__(self):
        return f"Бригада {self.brigade_number}"


class Repair(models.Model):
    repair_code = models.CharField(max_length=50, unique=True, verbose_name="Код ремонту")
    reg_number = models.ForeignKey(
        Locomotive,
        on_delete=models.CASCADE,
        verbose_name="Реєстраційний номер локомотива"
    )
    repair_type = models.CharField(max_length=100, verbose_name="Тип ремонту")
    start_date = models.DateField(verbose_name="Дата початку")
    days_required = models.PositiveIntegerField(verbose_name="Кількість днів")
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вартість за день")
    brigade_number = models.ForeignKey(
        Brigade,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Номер бригади"
    )

    class Meta:
        db_table = 'repairs'  # Назва таблиці

    def __str__(self):
        return self.repair_code
