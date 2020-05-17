def array_plus_array(arr1,arr2):
    sum = int(0)
    for i in range(len(arr1)):
        sum = sum + arr1[i] + arr2[i]
    return sum
    
#Test.it("Basic test")
#Test.assert_equals(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
#Test.assert_equals(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
#Test.assert_equals(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
#Test.assert_equals(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)    
