a = 8
b = 6
c = 3.5
d = 2
e = 1
f = 24-a-b-c-d-e
my_dict = {}
AS = {"sleeping":a, "classes":b, "studying":c, "TV":d, "music":e, "other":f}
s = input("the time of activity your want to know:")
if s in AS:
    print("the time is",AS[s],"hours.")
else:
    print("wrong")
