#program yo count the number of notes
a = int(input("enter the amount:"))
c2000 = a // 2000
a %= 2000
c500 = a // 500
a %= 500
c200 = a // 200
a %= 200
c100 = a // 100
print("2000 notes:", c2000)
print("500 notes:", c500)
print("200 notes:", c200)
print("100 notes:", c100)
