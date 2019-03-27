string1 = input("Enter the first string:")
type(string1)
string2 = input("Enter the second string:")
type(string2)
if ''.join(sorted(string1)) == ''.join(sorted(string2)) :
    print("Entered strings are anagrams of each other")
else:
    print("Entered strings are not anagrams of each other")
