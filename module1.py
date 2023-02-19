import pickle


def quan():
    quantity = int(input("How Much : "))
    return quantity


def buying(w, x, y):

    print(list(x)[y], ' : ', list(x.values())[y])
    z = quan()
    w.update({str(list(x)[y]): [int(list(x.values())[y]), z]})


def cust_buy():
    order = {}

    # reading
    file = open("DictFileDairy.pkl", "rb")
    dairy = pickle.load(file)

    file = open("DictFileWetGoods.pkl", "rb")
    wet_goods = pickle.load(file)

    print("Dairy: ")
    a = 1
    for key, value in dairy.items():
        print(str(a) + '.', key, ' : ', value)
        a += 1

    print('\n')

    print("Wet Goods: ")
    for key, value in wet_goods.items():
        print(str(a) + '.', key, ' : ', value)
        a += 1

    print('\n')

    while True:
        print("Enter (q) to exit")
        buy = input("Select an Item : ")
        if buy == "q":
            break

        buy = int(buy)
        buy -= 1

        if (buy + 1) <= len(dairy):
            buying(order, dairy, buy)
        else:
            buy2 = buy
            buy2 -= len(dairy)
            buying(order, wet_goods, buy2)

        print('\n')
    print('\n')

    total = 0

    print('Item', ' : ', 'Price', ',', 'Quantity')

    for key, value in order.items():
        print(key, ' : ', value)
        total += value[0] * value[1]

    print('Total :', total)
