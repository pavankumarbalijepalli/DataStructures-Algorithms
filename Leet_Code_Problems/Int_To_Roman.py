# Question: https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
      
        # Mapping usual int numbers to roman numbers
        _map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        
        # creating a list of keys from dict
        keys = list(_map.keys())
        
        # Output Stack
        out = []
        
        # Multiplication value for integer
        mult = 1
        
        # Going from back to front on keys - 1000 to 1
        for i in range(len(keys)-1, -1, -1):
            # If the num value exists
            if num>0:
              
                # Get the last digit from the number 
                # and set number to remaining digits
                temp = num%10
                num = num//10
                
                # P.S: If you're confused even after reading the comments, uncomment the below code.
#                 print(temp, "*", mult)
                
                # Condition for cases like 9 and 4
                if (temp+1 in keys) and (temp>1):
                  
                    # Add mapped value of mult on left and add mapped value of mult*(temp+1) on right
                    # If temp=9, and mult=10, i.e, 90. We add _map[mult] = 10:'X' on left, and _map[mult*(temp+1)] = _map[10*(10)] = 100:'C'
                    # We get XC which is 90 in roman.
                    out.append(_map[mult]+_map[mult*(temp+1)])
                # Conditions like 5,6,7,8
                elif (temp>=5 and temp<9):
                    
                    # Add mapped value of mult*5 on left and add mapped value of mult, temp-5 times.
                    # If temp=7 and mult=1, i.e, 7. We add _map[mult*5]= 5:'V' on left, and _map[mult]*(temp-5) = 1:'I' *(7-5) = 'II'
                    # We get VII which is 7 in roman.
                    out.append(_map[mult*5]+(temp-5)*_map[mult])
                
                # For all other conditions
                else:
                    
                    # Add mapped value of mult, temp times.
                    # If temp = 3 and mult=100, i.e 300. We add _map[mult] = 100:'C' * temp = 'C'*3
                    # We get CCC which is 300 in roman.
                    out.append(temp*_map[mult])
                
                # After every digit removed, we multiply mult with 10 so that next value is treated properly
                mult *= 10
                
        # Since we are appending to a stack, they will be in reverse order. So we reverse the stack and join the values.
        return ''.join(out[::-1])
