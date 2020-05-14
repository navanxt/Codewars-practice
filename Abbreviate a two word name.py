def abbrevName(name):
    abv = ""
    x,y = name.upper().split(' ')
    f = x[0]
    l = y[0]
    return f+'.'+l
    
#Test.assert_equals(abbrevName("Sam Harris"), "S.H");
#Test.assert_equals(abbrevName("Patrick Feenan"), "P.F");
#Test.assert_equals(abbrevName("Evan Cole"), "E.C");
#Test.assert_equals(abbrevName("P Favuzzi"), "P.F");
#Test.assert_equals(abbrevName("David Mendieta"), "D.M");    
