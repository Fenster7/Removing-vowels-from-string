random_string = input("Please enter one word or string of characters:")
print(random_string)

q = len(random_string)


random_string = random_string.replace("a", "")
random_string = random_string.replace("e", "")
random_string = random_string.replace("i", "")
random_string = random_string.replace("o", "")
random_string = random_string.replace("u", "")
random_string = random_string.replace("y", "")
random_string = random_string.replace("A", "")
random_string = random_string.replace("E", "")
random_string = random_string.replace("I", "")
random_string = random_string.replace("O", "")
random_string = random_string.replace("U", "")
random_string = random_string.replace("Y", "")

x = len(random_string)
z = q - x

print(random_string, "was", q, "characters long.", z, "vowels were removed!")
