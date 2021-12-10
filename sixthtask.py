def chocolateFeast(money,price, wrap):
    if money== 1 or money == 0 or money < wrap:
        return 0
    else:
        return money//wrap + chocolateFeast(money//wrap + money%wrap, price, wrap)

def main(money,price,wrap):
    result = money//price + chocolateFeast(money//price, price, wrap)
    return(result)

# Test
assert main(10,3,2)==5    
assert main(20,2,2)==19
assert main(16,2,2)==15
print("OK")



