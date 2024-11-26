import random
from faker import Faker
from django.core.management.base import BaseCommand
from myapp.models import Locomotive, Brigade, Repair  # Замініть 'app' на назву вашого додатка

fake = Faker("uk_UA")

class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **kwargs):
        # Генерація даних для Locomotive
        locomotive_types = ["вантажний", "пасажирський"]
        depots = ["Фастів", "Козятин", "П'ятихатки"]

        for _ in range(9):  # 9 локомотивів
            Locomotive.objects.create(
                reg_number=f"LOCO-{random.randint(1000, 9999)}",
                depot=random.choice(depots),
                locomotive_type=random.choice(locomotive_types),
                year_of_manufacture=random.randint(1980, 2023)
            )

        # Генерація даних для Brigade
        for i in range(1, 4):  # 3 бригади
            Brigade.objects.create(
                brigade_number=i,
                phone=f"+38067{random.randint(1000000, 9999999)}"
            )

        # Генерація даних для Repair
        locomotives = Locomotive.objects.all()
        brigades = Brigade.objects.all()

        for _ in range(11):  # 11 ремонтів
            Repair.objects.create(
                repair_code=f"REP-{random.randint(1000, 9999)}",
                reg_number=random.choice(locomotives),
                repair_type=random.choice(["поточний", "технічне обслуговування", "позаплановий"]),
                start_date=fake.date_this_year(),
                days_required=random.randint(1, 30),
                cost_per_day=random.uniform(500, 1500),
                brigade_number=random.choice(brigades)
            )

        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
