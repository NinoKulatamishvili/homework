#შექმენი ქვეყნის აბსტრაქტული კლასი
from abc import ABC, abstractmethod
class Cuntry(ABC):
    @abstractmethod
    def population(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def labour_force(self):
        pass
class Georgia(Cuntry):
    def population(self):
        print("population in 3.7 mln")

    def area(self):
        print("area is 69 th. sq km")
    def labour_force(self):
        print("labour force is 1.5 mln people")
cuntry=Georgia() #აქ რა კითხვაც მაქვს ანუ მე თუ არ გავნსაზღვრავდი ამ აბსტრაქტულ კლასში "ელემენტებს" დამატებით შემეძლო თუ არა Georgia განსაზღვირს დროს დამემატებინა და როგორ?
cuntry.population()
cuntry.area()
cuntry.labour_force()
