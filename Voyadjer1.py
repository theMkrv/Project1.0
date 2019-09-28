import math
date = int(input("Введите количество дней: "))
range_from_sun = 16637000000
speed_miles_per_hour = 38241 * 24
total_range = range_from_sun + speed_miles_per_hour * date
range_km = total_range * 1.609
a_e = range_km / 150000000
radiowave_speed = 299792458 / 1000 * 3600
delay = range_km / radiowave_speed
print(a_e,"А.Е.")
print(range_km,"Км")
print(total_range,"Миль")
print("Задержка в часах: ", delay)
