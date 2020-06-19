



#roman_num: Roman numeral string
#returns integer or invalid string

def roman_to_numbers(roman_num):
    d = {'I' : 1, 'V' : 5, 'X': 10, 'L': 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    final = 0
    for i in range(len(roman_num)):
        #checking for exponents rule
        if i > 0 and roman_num[i] == 'C' and (roman_num[i-1] == 'V' or roman_num[i-1] == 'I'):
            return 'invalid'
        if i > 0 and roman_num[i] == 'D' and (roman_num[i-1] == 'V' or roman_num[i-1] == 'I'):
            return 'invalid'
        if i > 0 and roman_num[i] == 'M' and (roman_num[i-1] == 'V' or roman_num[i-1] == 'I' or roman_num[i-1] == 'X' or roman_num[i-1] == 'L'):
            return 'invalid'
        
        if i > 0 and d.get(roman_num[i-1]) < d.get(roman_num[i]):
            #subtract difference if previous character is smaller
            final = final + d.get(roman_num[i]) - (d.get(roman_num[i-1])*2)
        else:
            final = final + d.get(roman_num[i])
    return final
        
    



#number: integer to convert
#returns roman numeral string

def numbers_to_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] 
    sym = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    final = ''
    for i in reversed(range(len(num))):
        #determines if divisible and get remainder
        num_repeats = number//num[i]
        remainder = number%num[i]
        
        for j in range(num_repeats):
            final = final + sym[i]
        number = remainder #reset number to be remainder
    return final





#testing code
print (roman_to_numbers('ID'))
print (numbers_to_roman(8976))


    
        
         

        





    
           
