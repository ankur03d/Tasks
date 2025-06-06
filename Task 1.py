print("\n--- STR to INT, FLOAT, COMPLEX ---")

# ----- User-defined -----
str_val = "10"
print("User-defined str to int:", int(str_val))          
print("User-defined str to float:", float(str_val))       
print("User-defined str to complex:", complex(str_val))   

# ----- User input -----
str_input = input("Enter a string number (e.g., '20'): ")
print("User input str to int:", int(str_input))           
print("User input str to float:", float(str_input))        
print("User input str to complex:", complex(str_input))    


print("\n--- FLOAT to INT, COMPLEX, STR ---")

# ----- User-defined -----
float_val = 10.5
print("User-defined float to int:", int(float_val))           
print("User-defined float to complex:", complex(float_val))    
print("User-defined float to str:", str(float_val))            

# ----- User input -----
float_input = float(input("Enter a float number (e.g., 25.75): "))
print("User input float to int:", int(float_input))           
print("User input float to complex:", complex(float_input))   
print("User input float to str:", str(float_input))            


print("\n--- INT to FLOAT, COMPLEX, STR ---")

# ----- User-defined -----
int_val = 7
print("User-defined int to float:", float(int_val))           
print("User-defined int to complex:", complex(int_val))        
print("User-defined int to str:", str(int_val))                

# ----- User input -----
int_input = int(input("Enter an integer number (e.g., 15): "))
print("User input int to float:", float(int_input))            
print("User input int to complex:", complex(int_input))       
print("User input int to str:", str(int_input))                


print("\n--- COMPLEX to INT, FLOAT, STR ---")

# ----- User-defined -----
comp_val = complex(5, 3)
print("User-defined complex to str:", str(comp_val))               
print("User-defined complex to int (real part):", int(comp_val.real))    
print("User-defined complex to float (real part):", float(comp_val.real)) 
 
# ----- User input -----
real = float(input("Enter real part of complex number: "))
imag = float(input("Enter imaginary part of complex number: "))
comp_input = complex(real, imag)
print("User input complex to str:", str(comp_input))              
print("User input complex to int (real part):", int(comp_input.real))     
print("User input complex to float (real part):", float(comp_input.real)) 
