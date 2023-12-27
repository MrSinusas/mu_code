
water_stored = 0
water_limit = 1000
while True:
    water_input = int(input("How much water do you pour in? "))
    water_stored = water_input + water_stored
    if water_stored > water_limit:
        water_output = water_stored
        print(str(water_output) + " ml of water was output from the box.")
        water_stored = 0
    else:
        print("Nothing happened.")

