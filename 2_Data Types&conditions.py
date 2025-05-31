 

# Data Types(أنواع البيانات): منهاpythonيوجد أنواع عديدة للبيانات في لغة 
""""
1- int (رقم صحيح): for example : studant age,phone number

2- string (نص): for ex : studant name 

3- float (للأرقام الكسرية أو العشرية) : for ex : average

4- Boolean (True or False للقيم التي تحتل قيمتين فقط ) : for ex : student age is sutable or no 

"""
# Condition(الشروط) : 
""""
وهو يعني أن ينفذ البرنامج أو يتخذ قرار معين إذا تحقق شرط معين 
نستخدم عدة جمل لكتابة الجمل الشرطية في python:  
1- if  جملة الشرط
أي إذا تحقق شرطها سوف يطبع الجملة المطلوبة

"""
#for example :
x = 5
if x > 1 :
 print ("True")
 
 """
 2- جملة else
 else اطبع الشرط  if  تستخدم إذا لم يتحقق الشرط اي وجود اكثر من شرط بمعنى آخر اذا لم يتحقق الشرط 
 """
 # for example :
 x = 2

if x > 5:
    print("True")
else:
   
 print("False")

"""
elif وهي اختصار ل else ifجملة 
وتستخدم في حال كان لدينا أكثر من احتمال أو خيار
"""
# for example
x = 5

if x > 5:
    print("أكبر من 5")
elif x == 5:
    print("يساوي 5")
else:
    print("أصغر من 5")

