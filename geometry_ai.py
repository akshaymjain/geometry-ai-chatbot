import math 
#defining our precise global constant for Pi at the very top
PI=math.pi
print("---GEOMETRY AI CHATBOT INITILIAZED---")
print("I can understand natural language requests for sphere's circumference,area,total surface area and volume.")
print("--------------------------------------")
#we use .lower() so the uppercase letters don't confuse the program
command=input("AI:Hey! I am your Geometry AI.What do you want to calculate today?").lower()
if "volume" in command:
    print("\nAI:Understood! let's calculate the volume of your sphere.")
    r=float(input("Enter the radius of the sphere: "))
    if r<=0:
        print("AI Error: The radius cannot be negetive or zero!")
    else:
        v=(4/3)*PI*(r**3)
        print("AI Result: the volume of the sphere is: ",v)
elif "circumference" in command:
    print("\nAI:Understood! let's calculate the circumference of your sphere.")
    r=float(input("enter the radius of sphere: "))
    if r<=0:
        print("AI Error: the radius caannot be negetive or zero")
    else:
        c=2*PI*r
        print("AI Result: the circumference of the sphere is: ",c)
elif "area" in command:
    print("\nAI:Understood! let's calculate the area of your sphere.")
    r=float(input("Enter the radius of the sphere: "))
    if r<=0:
        print("AI Error: the radius cannot negetive or zero.")
    else:
        a=PI*r**2
        print('AI Result: the area of the sphere is: ',a)
elif "total surface area" in command:
    print("\nAI:Undrestood! let's calculate the  total surface area of your sphere.")
    r=float(input("Enter the radius of the sphere: "))
    if r<=0:
        print("AI Error: The radius cannot be negetive or zero.")
    else:
        total_surface_area=4*PI*r**2
        print("AI Result: the total surface area of the sphere is: ",total_surface_area)
else:
    print("\nAI Error: I'm sorry,I am only trained to understand 'volume','circumference','area' and'total surface area' requests right now. ")
print('\n--------------------------------')
input("press Enter button to exit the code")