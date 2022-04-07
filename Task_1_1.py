"""1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях:
<d> дн <h> час <m> мин <s> сек."""

minute = 60
hour = 3600
day = 86400
week = 604800
month = 2629743
year = 31556926

duration = int(input('Для перевода укажите количество секунд: '))

if duration < minute:
    print('{} сек.'.format(duration));
elif minute <= duration and hour > duration:
    my_minute = duration // minute
    my_second = duration % minute
    print('{} мин. {} сек.'.format(my_minute, my_second));
elif duration >= hour and duration <= day:
    my_hour = duration // hour
    duration = duration % hour
    my_minute = duration // minute
    my_second = duration % minute
    print('{} час. {} мин. {} сек.'.format(my_hour, my_minute, my_second));
elif duration >= day and duration <week:
    my_day = duration // day
    duration = duration % day
    my_hour = duration // hour
    duration = duration % hour
    my_minute = duration // minute
    my_second = duration % minute
    print('{} дн. {} час. {} мин. {} сек.'.format(my_day, my_hour, my_minute, my_second));
elif duration >= week and duration < month:
    my_week = duration // week
    duration = duration % week
    my_day = duration // day
    duration = duration % day
    my_hour = duration // hour
    duration = duration % hour
    my_minute = duration // minute
    my_second = duration % minute
    print('{} нед. {} дн. {} час. {} мин. {} сек.'.format(my_week, my_day, my_hour, my_minute, my_second));
elif duration >= month and duration < year:
    my_month = duration // month
    duration = duration % month
    my_week = duration // week
    duration = duration % week
    my_day = duration // day
    duration = duration % day
    my_hour = duration // hour
    duration = duration % hour
    my_minute = duration // minute
    my_second = duration % minute
    print('{} мес. {} не.{} дн.{} час. {} мин. {} сек.'.format(my_month, my_week, my_day, my_hour, my_minute, my_second));
elif duration >= year:
    my_year = duration // year
    duration = duration % year
    my_month = duration // month
    duration = duration % month
    my_week = duration // week
    duration = duration % week
    my_day = duration // day
    duration = duration % day
    my_hour = duration // hour
    duration = duration % hour
    my_minute = duration // minute
    my_second = duration % minute
    print('{} год {} мес. {} нед. {} дн. {} час. {} мин. {} сек.'.format(my_year, my_month, my_week, my_day, my_hour, my_minute, my_second));



