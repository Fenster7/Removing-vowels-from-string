# My workflow for figuring out how to remove vowels from a string.

# The below code includes my failures till finally reaching success.
# After getting the successful code, I went back to improve it a little by adding
# a little code to check how many characters/vowels were removed and displays it.
# Also added check to change user's input to lower case. Could have just added upper case
# to the vowels' tuple.
# My thoughts & failed code has been commented out to show my thought process and improvement.


random_string = input("Please enter one word or string of characters:")
print(random_string)
low_random_string = random_string.lower()
print(low_random_string)
q = len(random_string)
#print(q)

# new_string = random_string.replace("a", "")
# new_string = random_string.replace("e", "")
# new_string = random_string.replace("i", "")
# new_string = random_string.replace("o", "")
# new_string = random_string.replace("u", "")
# new_string = random_string.replace("y", "")

l_string = list(low_random_string)
#print(l_string)

i = len(l_string)
# Add code to show the orginial length of the user's string.
print(random_string,"is",i, "characters long")

#for c in len(l_string):
#   if l_string[c] == a or e or i or o or u or y:
#       del(l_string[c])

#while i < (len(l_string) + 1):
#    print(l_string(i))

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

#for b in l_string:
#    if b in vowels:
#        new_string = random_string.replace(b, "")
#print(new_string)

for i in l_string:
    if i in vowels:
        low_random_string = low_random_string.replace(i, "")
x = len(low_random_string)
# Comparing number of characters from original(q) string and new string(x) to
# find how how many characters(vowels) where removed.
z = q - x
# printing out the original string without vowels and how many vowels were removed.
# This changes the original string to lower case. I can do better.
print(low_random_string, "has had", z, "vowels removed!")



        
