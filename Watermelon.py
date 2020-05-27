def divide(weight):
    flag = False
    for i in range(weight):             
        if i%2 == 0 and (weight-i)%2 == 0 and i != 0:
            flag = True
    return flag
        
#test.assert_equals(divide(4), True)
#test.assert_equals(divide(2), False)
#test.assert_equals(divide(5), False)
#test.assert_equals(divide(100), True)
#test.assert_equals(divide(67), False)
#test.assert_equals(divide(90), True)
#test.assert_equals(divide(10), True)
#test.assert_equals(divide(99), False)
#test.assert_equals(divide(32), True)        
