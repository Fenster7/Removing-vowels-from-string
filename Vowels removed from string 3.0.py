
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

def remove_vowel(random_string):
    new_string = ''.join([x for x in random_string if x.lower() not in vowels])
    print(new_string, len(random_string) - len(new_string), 'vowels where removed!')

random_string = input("Please enter one word or string of characters:")

remove_vowel(random_string)





