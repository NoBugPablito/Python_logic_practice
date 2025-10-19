temp = 32
print(" F°     C°")
while temp < 73:
    celsius = int((temp - 32) * 5 / 9)
    print(f"{temp}°F   {celsius}°C")
    temp += 1
