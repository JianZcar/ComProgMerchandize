import pickle


def ask_y_n(x):
    while True:
        i = input(x + ' y/n : ')
        if i == 'y':
            return True
        elif i == 'n':
            return False
        else:
            print('Invalid Input')


def delete_item(x, y):
    print(list(x)[y], ' : ', list(x.values())[y])
    if ask_y_n('Delete'):
        x.pop(str(list(x)[y]))


def aer(x):
    item = input('Enter the Item name: ').strip()
    prompt = 'Enter ' + item + ' price: '
    price = int(input(prompt))
    print('\n')
    x.update({item: price})
    for key, value in x.items():
        print(key, ' : ', value)


def edit():
    dairy = {}
    wet_goods = {}

    filex = open("DictFileDairy.pkl", "rb")
    x = pickle.load(filex)

    filex = open("DictFileWetGoods.pkl", "rb")
    y = pickle.load(filex)

    dairy.update(x)
    wet_goods.update(y)

    print('\n')

    while True:
        a = 1

        print("Dairy: ")
        for key, value in dairy.items():
            print(str(a) + '.', key, ' : ', value)
            a += 1

        print('\n')

        print("Wet Goods: ")
        for key, value in wet_goods.items():
            print(str(a) + '.', key, ' : ', value)
            a += 1

        print('\n')
        operation = int(input('Add/Edit/Replace:1 Remove:2  |  '))

        if operation == 1:
            while True:
                print('\n')
                print('Enter (q) to exit')
                category = input('Dairy:1 Wet Goods:2  |  ')

                if category == 'q':
                    break

                category = int(category)
                if category == 1:
                    aer(dairy)

                elif category == 2:
                    aer(wet_goods)

        elif operation == 2:
            while True:
                print('\n')
                print('Enter (q) to exit')
                select = input("Select an Item : ")

                if select == 'q':
                    break

                select = int(select)
                select -= 1

                if (select + 1) <= len(dairy):
                    delete_item(dairy, select)
                else:
                    select2 = select
                    select2 -= len(dairy)
                    delete_item(wet_goods, select2)

        print('\n')
        if not ask_y_n('Continue'):
            break

    a = 1

    print("Dairy: ")
    for key, value in dairy.items():
        print(str(a) + '.', key, ' : ', value)
        a += 1

    print('\n')

    print("Wet Goods: ")
    for key, value in wet_goods.items():
        print(str(a) + '.', key, ' : ', value)
        a += 1

    if ask_y_n('Save'):
        filex = open("DictFileDairy.pkl", "wb")
        pickle.dump(dairy, filex)
        filex.close()

        filex = open("DictFileWetGoods.pkl", "wb")
        pickle.dump(wet_goods, filex)
        filex.close()
