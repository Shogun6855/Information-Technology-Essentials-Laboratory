def is_vowel(s):
    if s in ['A','a','E','e','I','i','O','o','U','u']:
        return True
    else:
        return False
def main():
    vowel = 0
    string = input("Enter a string: ")
    for i in string.split():
        for j in i:
            if(is_vowel(j)):
                vowel+=1
    print("No of vowels in the string: ", vowel)
main()
            
