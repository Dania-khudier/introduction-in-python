# Task 1
# برنامج لفحص الملف اذا فردي أو زوجي



#  input : نستخدمها لجعل المستخدم هو الذي يكتب القيمة 

number = int(input("Enter an intgerg number: "))

# نستخدم الشرط لمعرفة إذا كان الرقم زوجي أم فردي
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# اذا الرقم الذي يدخله المستخدم يقبل القسمة على 2 بدون باقي
# اذا هو زوجي اما اذا كان هناك بافي فهو فردي