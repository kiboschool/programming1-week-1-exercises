width = float(input("how wide is the room? "))
height = float(input("how tall is the room? "))
number_of_people = int(input("how many people in the room? "))

print(round(width * height *  0.1 + number_of_people * 0.06, 2))
