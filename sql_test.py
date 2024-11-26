import psycopg2
from prettytable import PrettyTable

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="company_db",
        user="example_user",
        password="example_password"
    )

def execute_queries():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT last_name, first_name, middle_name FROM Workers
        WHERE is_foreman = TRUE
        ORDER BY last_name;
        """
    )
    table = PrettyTable(["Прізвище", "Ім'я", "По батькові"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("Робітники, які є бригадирами:\n", table)

    cursor.execute(
        """
        SELECT repair_type, AVG(days_required) AS avg_duration FROM Repairs
        GROUP BY repair_type;
        """
    )
    table = PrettyTable(["Тип ремонту", "Середня тривалість (днів)"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("\nСередня тривалість ремонту за типом ремонту:\n", table)

    selected_depot = input("Введіть депо (Фастів, Козятин, П’ятихатки): ")
    cursor.execute(
        """
        SELECT reg_number, locomotive_type, year_of_manufacture FROM Locomotives
        WHERE depot = %s;
        """, (selected_depot,)
    )
    table = PrettyTable(["Реєстраційний номер", "Тип локомотива", "Рік випуску"])
    for row in cursor.fetchall():
        table.add_row(row)
    print(f"\nЛокомотиви у депо {selected_depot}:\n", table)

    cursor.execute(
        """
        SELECT reg_number, SUM(days_required * cost_per_day) AS total_repair_cost
        FROM Repairs
        GROUP BY reg_number;
        """
    )
    table = PrettyTable(["Реєстраційний номер", "Загальна вартість ремонту"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("\nЗагальна вартість ремонту кожного локомотива:\n", table)

    cursor.execute(
        """
        SELECT brigade_number, COUNT(worker_id) AS worker_count
        FROM Workers
        GROUP BY brigade_number;
        """
    )
    table = PrettyTable(["Номер бригади", "Кількість працівників"])
    for row in cursor.fetchall():
        table.add_row(row)
    print("\nКількість працівників у кожній бригаді:\n", table)

    selected_brigade = int(input("Введіть номер бригади для перегляду ремонтів: "))
    cursor.execute(
        """
        SELECT repair_code, reg_number, repair_type, days_required
        FROM Repairs
        WHERE brigade_number = %s;
        """, (selected_brigade,)
    )
    table = PrettyTable(["Код ремонту", "Реєстраційний номер", "Тип ремонту", "Тривалість (днів)"])
    for row in cursor.fetchall():
        table.add_row(row)
    print(f"\nРемонти, проведені бригадою {selected_brigade}:\n", table)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    execute_queries()
