


#create a function to find perform the calculation of base and exponent
def calculate_exponent(base, exp):
    exp_answer = base ** exp

    if exp < 0: # the exponent should not be a non-negative integer
        return False 
    else: 
        print("base =", base)
        print("exponent =" , exp)
        print(base , "raises to the power of" , exp , "is :" , exp_answer)
    
#call the function with the given base and exponent
calculate_exponent(2, 5)
calculate_exponent(5, 4)





