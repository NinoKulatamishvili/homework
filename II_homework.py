#1_ვიქტორინა

a=input("Question : ")
b=input("Answer: ")
c="რომის"
if b == c :
    print("სწორია")
else:
    print("არა! სწორი პასუხია რომის!")

##2_ონლაინ მაღაზია

choice_1="ლეპტოპები"
choice_2="პერსონალური კომპიუტერები"
choice_3="მობილურები"
choice=input("Make your choice: ")
our_budget=int(input("your budget is: ")) #რატომ მჭირდება მთელი რიცხვის მითითბება ისე არაფრით არ იმუშავა?

if choice==choice_1:
    print("choice_1")
if our_budget<1600:
    print("თქვენ არ გყოფნით ბიუჯეტი!")
elif our_budget==2000:
    print("hp")
elif our_budget<=1800:
    print("asus", "lenovo")
if choice==choice_2:    #აქ ის ვერ გავაკეთე რომ ერთ if რომ მორჩება იმის შედეგი არ დამიბეჭდოს და არჩეულ choice გაყვეს მხოლოდ
    print("choice_2")
if our_budget<2000:
    print("თქვენ არ გყოფნით ბიუჯეტი!")
elif our_budget>=3000:
    print("apple")
elif our_budget>=2100:
    print("asus", "lenovo")
if choice==choice_3:
    print("choice_2")
if our_budget<100:
    print("თქვენ არ გყოფნით ბიუჯეტი!")
elif our_budget>=600 :
    print("samsung")
elif our_budget>=3100:
    print("apple")

# თამაში "ქალაქობანა"

a=input("enter the Latin letters, A-Z : ")

human1=0
human2=0
human1_answer_cuntry=input("cuntry of human1: ")
human1_answer_city=input("sity of human1 : ")
human2_answer_cuntry=input("cuntry of human2 : ")
human2_answer_city=input("sity of human2 : ")

if  human1_answer_cuntry[0]!="a" or human1_answer_city[0]!="a": #აქ პირველი ასო როგრო შეადაროს მოვძებნე, მაგრამ ბოლომდე ვერ გავედი ნორმალურად
     print("human1, you lost")
else:
    print("human2, you win")
if  human2_answer_cuntry[0]!="a" or human2_answer_city[0]!="a":
     print("human2, you lost")
else:
    print("human2, you win")








