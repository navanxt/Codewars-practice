def modified_sum(a, n):
    sum = int(0)
    powersum = int(0)
    for i in a:
        sum += i
        powersum += pow(i,n)
    result = int(powersum-sum)
    return result
    
#Test.assert_equals(modified_sum([1, 2, 3], 3), 30)
#Test.assert_equals(modified_sum([1, 2], 5), 30)    
