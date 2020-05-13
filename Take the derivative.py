def derive(coefficient, exponent): 
    return str(coefficient*exponent)+"x^"+str(exponent-1)
    
#@test.describe('Example Tests')
#def example_tests():
#    test.assert_equals(derive(7,8), "56x^7")
#    test.assert_equals(derive(5,9), "45x^8")    
