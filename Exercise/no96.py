'''The Digital Thermostat (Void Functions)
Definition: A system that triggers a physical action (simulated) without returning a value.Task: Create a void function (a function with no return statement) called
toggle_ac(temp). If temp > 25, it should print "Compressor ON". If not, it should print
"Compressor OFF"
'''

def toggle_ac(temp):    
    if temp > 25:
        print("Compressor ON")
    else:
        print("Compressor OFF")     
        
# User input
temperature = float(input("Enter the current temperature: "))   
# Call function
toggle_ac(temperature)
