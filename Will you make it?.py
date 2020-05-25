def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        return True
    else:
        return False
        
#test.assert_equals(zero_fuel(50, 25, 2), True)
#test.assert_equals(zero_fuel(100, 50, 1), False)        
