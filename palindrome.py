f = open("English.txt", "r")
string=f.readline()
while string:
    string = string.lower()
    string = string.strip()
    if(string == string[::-1]):
          print(string)
    string = f.readline()
print("they are a palindrome")
f.close()
