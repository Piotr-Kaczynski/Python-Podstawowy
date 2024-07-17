import math
degree = 360
radiany = 360*(math.pi)/180
print(radiany)
print(math.radians(360))

#2
small_r = 0.22
big_r = 0.27
family_r = 0.38

small_price = 11.5
big_price = 15.6
family_price = 22

small = math.pi*small_r**2
big = math.pi*big_r**2
family = math.pi*family_r**2
print(small, big, family)

small_sqMeter = small_price/small
big_sqMeter = big_price/big
family_sqMeter = family_price/family

print(small_sqMeter, big_sqMeter, family_sqMeter)

print(dir(math))