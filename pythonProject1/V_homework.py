#1 შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
class Vehicle:
    passenger_car= 35 #ვგულისხმობ მოდელებს, დაშვებაა
    truck = 30
    commercial=15
    Public_transport=20
#2 დაამატე ერთი სტატიკური მეთოდი
    @staticmethod
    def acceleration():
        print("აჩქარება დამოკიდებულია ტრანსპორტის მახასიათებელზე")
#3 დაამატე ორი კლასის მეთოდი
#აქ რაც მაინტერესებ ერთად დამატება შეიძლებააა?
    @classmethod
    def your_vehiceltyp(cls):
        print(f"My vehicle is one of {cls.passenger_car}")

    @classmethod
    def your_vehiceltyp1(cls):
        print(f"My vehicle is one of {cls.truck}")

Vehicle.acceleration()
Vehicle.your_vehiceltyp()
Vehicle.your_vehiceltyp1()

#4_5 init magic მეთოდით უნდა დავამატოთ 3 ობიექტი
#ეს თავიდან იმიტომ შევქმენი რომ ზემოთ ძალიან ამებნა და გააზრება რომ შემძლებოდა
class Transport:
  def __init__(self, weels, color, model):
      self.weels=weels
      self.color=color
      self.model=model
transport1=Transport(4,"red", "Honda") #მიჭირს გააზრება როდესაც ობიექტებს ვამატებ შემდეგ ისინი ხომ უნდა დავინახო და დავბეჭდო მაგრამ ვერ ვაკეთებ, კიდევ მინდა განვსაზღვრო სადმე სხვაგან? მაგალითად, რამდენი ბორბალი აქვს, რა ფერია და ა.შ
transport2=Transport(6,"blue", "CV")   #რადგან ტრანსპორტში განვსაზღვრე ვფიქრობ, რომ განსაზღვრულია და სხვა არაფერი სჭირდება
transport1.weels


def __repr__(self):
    return f"Transport"
