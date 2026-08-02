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