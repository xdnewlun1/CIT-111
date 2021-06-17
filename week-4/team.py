import math

def cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height

def cylinder_surface_area(radius, height):
    return 2*math.pi*radius*(radius+height)

lines = ""
with open("week-4/data.txt") as data:
    lines = data.readlines()
#Name, Radius, Height
for line in lines:
    line = line.split(",")
    line[1] = float(line[1])
    line[2] = float(line[2])
    volume = cylinder_volume(line[1], line[2])
    surf_area = cylinder_surface_area(line[1], line[2])
    stor_efic = volume/surf_area
    print(f"{line[0]} - {stor_efic:.1f}")