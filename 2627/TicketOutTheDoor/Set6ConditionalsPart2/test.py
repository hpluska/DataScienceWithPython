age = 25
has_driver_license = True

if age >= 18:
    print("You are old enough to drive.")
    if has_driver_license:
        print("You also have a driver's license, so you can legally drive.")
    else:
        print("You are old enough, but you need a driver's license to legally drive.")
else:
    print("You are not old enough to drive.")