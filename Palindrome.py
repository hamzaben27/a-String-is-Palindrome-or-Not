
# palindrome ou non verification


def isPalindrome(str):

    # on devise le mot en deux et on verifier 
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


# main function
s = input("donner la chaine a verifier : ")
pal = isPalindrome(s)

if (pal):
    print("ce mot est palindrome")
else:
    print("ce mot n'est pas palindrome")
