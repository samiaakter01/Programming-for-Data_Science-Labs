x = int()

if x < 0:
    print("Rejected")
    
elif x < 20:
    print("Low") 
    
elif x <= 35 and x >= 20:
    print() 
    
    
    
values = [12, 0, 25, 18, 0, 30, 15]          

valid_values =[]
total = 0
for value in values:
    if value == 0:
       continue
    valid_values.append(value)
    
 number_of_valid_observation: int = len(valid_values)
    
 total = total +  value 
  average = (total/number_of_observation)