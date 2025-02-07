#A program to check a year whether is leap year or not
year=int(input("Enter the year: "))
if year % 100==0 and year % 400 ==0:
    print(year,"is a leap year")
elif year % 4 == 0 and year % 100!=0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


#A program to check whether a letter is a consonant or a vowel
letter = input("Enter the alphabet : ")

if letter in ("a","e","i","o","u"):
    print(letter,"is a vowel")
else:
    print(letter,"is a consonant")