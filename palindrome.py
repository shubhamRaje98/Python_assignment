s = input("Enter String: ")
rev = list(s)

for i in range(0, int(len(rev) / 2)):
    temp = rev[i]
    rev[i] = rev[len(rev) - 1 - i]
    rev[len(rev) - 1 - i] = temp
reverse = "".join(rev)
if(s == reverse):
    print("Palindrome")
else:
    print("Not a Palindrome")