# Reverse Value of String in Python

def reverseValue(string):
 text = ""
 for i in string:
   text = i + text
 return text

Value_Revesed = input("Enter Any value : ")
if reverseValue(Value_Revesed):
   print(f"The reversed value of {Value_Revesed} is {reverseValue(Value_Revesed)}")
else:
   print("The value is not palindrome")


# Palindrome

def PalindromeValue(string):
 if string == string[: : -1]:
  return True
 else:
   return False

ActualValue = input("Enter Any value : ")
if PalindromeValue(ActualValue):
   print(f"The Palindrome value of {ActualValue} is {PalindromeValue(ActualValue)}")
else:
   print("The value is not palindrome")




# Fibonacci Series

def Fibonacci(n):
  a, b = 0, 1
  series = []
  for i in range(n):
   series.append(a)
   a, b = b, a + b
  return series

ActualValue = int(input("Enter Any value : "))
if ActualValue <= 0:
   print(f"Please enter the Correct values {ActualValue}")
else:
   Result = Fibonacci(ActualValue)
   print("The Fibonacci value of:", ActualValue, "is:", Result)


# Remove Duplicates from a List

def Duplicates():
   my_list = [1,2,3,4,5,6,1,5,6,3,2]
   duplicate = []
   for item in my_list:
      if my_list.count(item) > 1 and item not in duplicate:
        duplicate.append(item)
   return duplicate

DuplicateValue = Duplicates()
if DuplicateValue:
  print("Duplicae Value found: ", DuplicateValue )
else:
  print("No Duplicae Value found: ", DuplicateValue )

# vowels

# count vowels in a string
def vowels(alphabet):
  count = 0
  vowels = "aeiouAEIOU"
  for i in alphabet:
      if i in vowels:
         count = count + 1
  return count
   
Couunt_vowles = input("Enter any alphabet: ")
if vowels(Couunt_vowles):
   print("The values are vowels :", vowels(Couunt_vowles))
else:
   print("The values are not vowels :", vowels(Couunt_vowles))