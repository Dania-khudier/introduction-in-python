# program to check if a number is prime

# العدد الأولي هو العدد الذي لا يقبل القسمة الا على 1 أو على نفسه


# المستخدم هو الذي يدخل رقم صحيح 
number = int(input("Enter a positive integer: "))

# فحص اذا كان العدد أكبر من 1 للتأكد بأنه أولي
if number > 1:
# للبحث اذا كان العدد يقبل القسمة على أعداد أخرى غير 1 و نفسه
    for i in range(2, number):
        if number % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")
else:
    print("The number is not prime.")
