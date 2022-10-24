import random

##################################################
# Make your lambda function here
# greater =
# filter50 =
##################################################


print(greater(10, 20))
print(greater(20, 10))
print(greater(100, 20))

numbers = [random.randint(0, 100) for i in range(10)]
print('original list', numbers)
print('filter 50', filter50(numbers))
