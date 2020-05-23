def is_even(n): 
    if type(n) == int:
        if n%2 == 0:
            return True
        else:
            return False
    else:
        return False
        
#@test.describe('Fixed Tests')
#def fixed_tests():

#    @test.it('Basic Test Cases')
#    def basic_tests():
#        test.assert_equals(is_even(0), True)
#        test.assert_equals(is_even(0.5), False)
#        test.assert_equals(is_even(1), False)
#        test.assert_equals(is_even(2), True)
#        test.assert_equals(is_even(-4), True)
#        test.assert_equals(is_even(15), False)
#        test.assert_equals(is_even(20), True)
#        test.assert_equals(is_even(220), True)
#        test.assert_equals(is_even(222222221), False)
#        test.assert_equals(is_even(500000000), True)        
