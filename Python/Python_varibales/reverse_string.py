
value = input("Enter any String : ")
value_2 = reversed(value)
print("The reversed value is :" , ''.join(value_2))
print("The reversed value is :" ,value[: : -1])

length_value = len(value)
print("The length of the string is:" , length_value)

text = ""
for i in value:
    text = i + text
print("The reversed value is :" , text)

