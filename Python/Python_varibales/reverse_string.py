
value = input("Enter any String : First way  : ")
value_2 = reversed(value)
print("The reversed value is :" , ''.join(value_2))
print("The reversed value is :" ,value[: : -1])

# Check the length of the string
length_value = len(value)
print("The length of the string is:" , length_value)

# Another way to reverse a string
text = ""
for i in value:
    text = i + text
print("The reversed value is :" , text)




def reverse_string(String):
    text = ""
    for i in String:
        text = i + text
    return text
Reverse_value = input("Enter any String : Second way ")
Value_r = reverse_string(Reverse_value)
print("The reversed value is :" , Value_r)