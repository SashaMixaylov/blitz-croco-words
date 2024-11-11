# Задача 2024.11.06.01
#
# Попробуйте написать даты, когда проходила каждая игра, учитывая что игры проходили по воскресеньям.

from datetime import datetime, timedelta

def allday(year: int) -> list[str]:
    sunday: list[str] = list()
    current_data = datetime.now()
    for i in range(year):
        if current_data.weekday() == 6:
            sunday.append(current_data.strftime(" %Y %d %m"))
        current_data += timedelta(days=1)
    return sunday


def main():
    sunday: list[str] = allday(2024)
    print(f"Даты игр: {sunday}")


if __name__ == '__main__':
    main()