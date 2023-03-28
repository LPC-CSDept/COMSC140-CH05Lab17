
def makeLambda(value):
    ##################################################
    # Make your code
    # retrun lambda function
    # add value to the all elements
    ##################################################


def main():
    numbers = [10, 20, 30]

    add20 = makeLambda(20)
    numbers = add20(numbers)
    print(numbers)

    add50 = makeLambda(50)
    numbers = add50(numbers)
    print(numbers)


    numbers2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    numbers2 = add20(numbers2)
    print(numbers2)

if __name__ == '__main__':
    main()