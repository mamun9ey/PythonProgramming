#write a program to input any alphabet and check whether is vowel or consonant.

c = input()

# checking for vowels
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
    print(c, "is a vowel")  # condition true input is vowel
else:
    print(c, "is a consonant")  # condition true input is consonant