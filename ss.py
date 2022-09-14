def isPalindrome(s):

    # Replacing the white-space in string

    s1 = s.replace(' ', '')

    # converting string to lowercase

    s1 = s1.lower()

    # Reversing the string

    s2 = s1[::-1];

    # Evaluating the result

    return True if s1 == s2 else False

   
# Driver program to test sentencePalindrome()

s = input("enter the sentences")

if (isPalindrome(s)):

    print ("Sentence is palindrome.")

else:

    print ("Sentence is not palindrome.")
 
