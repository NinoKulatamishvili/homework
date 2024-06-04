# ინფორმაციის გასამმაგება
x=input("Enter text: ")  #რადგან პირობაში ეწერა რომ მომხმარებლისგან უნდა "მიეღო" ჩავთვალე რომ ასე უნდა შეეყვანა
def tripled(word):
    print("tripled:", x+x+x)
tripled("word")

#2_Weight on the moon
def moon_weight(y):
   return y/6
print(moon_weight (66))

#კალკულატორი _ რაც ლექციაზე მაინტერესებს კი ვხდები რომ return უნქცია აბრუნებს მაგრამ პრინტ ხომ მაინც გვჭირდება რომ დამიბეჭდოს და შეცდომით ვიცი?

def culculator():
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))   #სიმბოლოების შეყვანის if როგორ დამეწერა ვერ გავიხსენე და საკითხავი მაქვს
   operetion = input("Enter operation: ")

   if num2 == 0 and operetion == "/":
      print("მნიშვნელი არ შეიძლება ნულის ტოლი იყოს!")
   elif operetion == "/":
      print(num1 / num2)
   if operetion == "+":
      print(num1 + num2)
   elif operetion == "-":
      print(num1 - num2)
   elif operetion == "*":
      print(num1 * num2)
   elif operetion == "**":
      print(num1 ** num2)
culculator()