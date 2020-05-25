def hero(bullets, dragons):
    if bullets >= dragons*2:
        return True
    else:
        return False
        
#Test.assert_equals(hero(10, 5), True)
#Test.assert_equals(hero(7, 4), False)
#Test.assert_equals(hero(4, 5), False)
#Test.assert_equals(hero(100, 40), True)
#Test.assert_equals(hero(1500, 751), False)
#Test.assert_equals(hero(0, 1), False)        
