##text = input("Enter any word to encrypt : ")
##cipher = ''
##shifting = int(input("Select shifting number between 1 - 25 : "))
##if shifting not in range(1,26):
##    print("Wrong shifting number ")
##else:
##    for ch in text:
##        if ch.isdigit():
##            cipher += ch
##
##        elif ch.isupper():
##            code = ord(ch) + shifting
##            if code > ord("Z"):
##                sub_ord = code - ord("Z") + ord("A") - 1
##                cipher += chr(sub_ord)
##            else:
##                cipher += chr(code)
##        elif ch.islower():
##            code = ord(ch) + shifting
##            if code > ord("z"):
##                sub_ord = code - ord("z") + ord("a") - 1
##                cipher += chr(sub_ord)
##            else:
##                cipher += chr(code)
##        else:
##            cipher += ch
##print(cipher)


# input text to encrypt
text = input("Enter message: ")

# enter valid shift value (repeat until it succeeds)
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter cipher's shift (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Bad shift value!")

cipher = ''

for char in text:
    # is it a letter?
    if char.isalpha():
        # shift its code
        code = ord(char) + shift
        # find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # make correction
        code -= first
        code %= 26
        # append encoded character to message
        cipher += chr(first + code)
    else:
        # append original character to message
        cipher += char

print(cipher)
