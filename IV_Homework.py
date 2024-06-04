#დავალება 1
consumer_info= []
while len(consumer_info)<3:

    name= input("Name Lastname age: ")
    a = []
    a.append(name)
    consumer_info.append(a)

print(consumer_info[1])

#დავალება 2
a=[["Name: Andy Brody Age: 45"], ["Name: Tom Hanks Age: 55"], ["Name: Morgan Freeman Age: 70"]]
actors=input("Enter actors name: ")
for actors in a :
  if actors[0]=="Andy":
   print(a[0])

#დავალება 3 _ შექმენია სია, რომელიც მიიღებს სიას და დააბრუნებს სიას უნიკალური ელემენტაებით
def myfunction():
    a=[]
    while True:
        answer=input("Enter number or enough: ")
        if answer=="enough":
            break
        else:
            a.append(answer)
    a = tuple(set(a))
    return a

result = myfunction()
print(result)

#4 დავალება ორი set უნდა გაეერთიანოს და გადააქციოს Tuple-ად

def function() :
    a={"vashli", "msxali", "marwyvi"}
    b={"pomidori", "niori"}
    a.union("b")
    a=tuple(set(a))
    return a
result = function()
print(result)

#დავალება 5_შეამოწმე ლექსიკონის ცარიელობა
a={}
if len(a)==0:
    print("ცარიელი სიმრაველა")
else:
    print("ლექსიკონი არ არის ცარიელი")

#დავალება 6 _ლექციაზე ნანახის მიხედვით არ მინდოდა გაკეთება, თუმცა ვერ დავასრულე და ვიფიქრებ კიდე
def dectionary():
    input_str=int("Enter string: ")
    print(len(input_str))

    result = dectionary()
    print(result)

