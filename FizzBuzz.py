# FizzBuzz
# "Fizz" اطبع الأرقام من 1 إلى 100اذا كان العدد يقبل القسمة على 3 اطبع
# "Buzz" اذا يقبل القسمة على 5 اطبع 
# "FizzBuzz"واذا يقبل على كليهما اطبع 

for i in range(1, 101):
  if i % 3 == 0:
   print ("Fizz")  
  elif i % 5 == 0:
   print("Buzz")
  elif i % 3 == 0 and i % 5 == 0:
   print("FizzBuzz")
  else :
   print ("erorr")


