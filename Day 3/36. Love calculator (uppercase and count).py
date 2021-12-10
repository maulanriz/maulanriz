yourname = input("Whats your name? ")
theirname = input("Whats their name? ")

name1 = yourname.lower()
name2 = theirname.lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e2 = name1.count("e") + name2.count("e")

total1 = t + r + u + e
total2 = l + o + v + e2

totalint = int(str(total1) + str(total2))

if totalint < 10 or totalint > 90:
    print(f"Your score is {totalint}, you go together like coke and mentos")
elif 40 <= totalint <= 50:
    print(f"Your score is {totalint}, you are alright together")
else:
    print(f"Your total score is {totalint}")
