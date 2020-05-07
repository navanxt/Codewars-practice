def get_sum(a,b):
    if a==b:
      return a
    else:
      sum = int(0)
      if a<b:
        for i in range(a,b+1):
          sum+=i
      elif b<a:
        for i in range(b,a+1):
          sum+=i
      return sum

#Test.assert_equals(get_sum(0,1),1)
#Test.assert_equals(get_sum(0,-1),-1)
