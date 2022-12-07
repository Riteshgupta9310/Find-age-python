# Take input of age from 3 people
#determine the oldest and youngest

person1 = int(input("age of first person"))
person2 = int(input("age of second person"))
person3 = int(input("age of third person"))

if person1 > person2 and person1 > person3:
    print("oldest is",person1)
     
elif person2 > person3 and person2 > person1:
    print("oldest is",person2)     

elif person3 > person1 and person3 > person2:
    print("oldest is",person3)