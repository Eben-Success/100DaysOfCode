
# This program test the compatibility between two people.

prompt1 = input("What is your name?: \n")

prompt2 = input("What is their name?: \n")

prompt1 = prompt1.lower()
prompt2 = prompt2.lower()

t1 = prompt1.count("t")
r1 = prompt1.count("r")
u1 = prompt1.count("u")
e1 = prompt1.count("e")

t2 = prompt2.count("t")
r2 = prompt2.count("r")
u2 = prompt2.count("u")
e2 = prompt2.count("e")

l1 = prompt1.count("l")
o1 = prompt1.count("o")
v1 = prompt1.count("v")
le1 = prompt1.count("e")


l2 = prompt2.count("l")
o2 = prompt2.count("o")
v2 = prompt2.count("v")
le2 = prompt2.count("e")

print("\nLetters in \"TRUE\" ")
print("T occurs {0} times".format(t1+t2))
print("R occurs {0} times".format(r1+r2))
print("U occurs {0} times".format(u1+u2))
print("E occurs {0} times".format(e1+e2))
print("Total count in \"TRUE\' is: {}".format())

print("\nLetters in \"LOVE\" ")
print("L occurs {0} times".format(l1+l2))
print("O occurs {0} times".format(o1+o2))
print("V occurs {0} times".format(v1+v2))
print("E occurs {} times".format(le1+le2))