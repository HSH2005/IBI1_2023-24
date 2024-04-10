a =int(input("the year person was born is: "))
date = a + 18
class actor:
    def __init__(self, name, age):
        self.name=name
        self.age= age
the_actor = actor("Roger Moore",1973)
the_actor2 = actor("Timothy Dalton",1987)
the_actor3 = actor("Pierce Brosnan",1995)
the_actor4 =actor("Daniel Craig",2006)
if date > the_actor4.age:
    print(the_actor4.name)
elif date > the_actor3.age:
    print(the_actor3.name)
elif date > the_actor2.age:
    print(the_actor2.name)
else:
    print(the_actor.name)