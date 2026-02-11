
import sys
print("Hello from arg.py!"  )
for index, arg in enumerate(sys.argv):
    print(f"Argument {index}: {arg}")   
    
print("\n total arguments: ", len(sys.argv))