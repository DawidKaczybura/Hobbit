name = "jak kowalski"
print(name.title())
# Jak Kowalski

name = "Jan Kowalski"
print(name.upper())
# JAN KOWALSKI
print(name.lower())
# jan kowalski

first_name = "michael"
last_name = "hueniger"
full_name = first_name + " " + last_name
print("Witaj, " + full_name.title() + "!")
# Witaj, Michael Hueniger!
message = "Witaj, " + full_name.title() + "!"
print(message)
# Witaj, Michael Hueniger!

print("Python")
# Python
print("\tPython")
#         Python

print("Języki:\nPyton\nC\nJavaScript")
# Języki:
# Pyton
# C
# JavaScript

print("Języki:\n\tPyton\n\tC\n\tJavaScript")
# Języki:
#         Pyton
#         C
#         JavaScript

favorite_language = 'python '
print(favorite_language)
# 'python '
print(favorite_language.rstrip())
# 'python'
favorite_language = favorite_language.rstrip()
print(favorite_language)
# 'python'

favorite_language = ' python '
print(favorite_language.rstrip())
# ' python'
print(favorite_language.lstrip())
# 'python '
print(favorite_language.strip())
# 'python'