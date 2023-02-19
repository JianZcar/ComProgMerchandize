import pickle
import module1
import module2
# Made by Jian Esteban


def initialize(x, y):
    try:
        filex = open("DictFileDairy.pkl", "rb")
        x = pickle.load(filex)

        filey = open("DictFileWetGoods.pkl", "rb")
        y = pickle.load(filey)

    except FileNotFoundError:
        filex = open("DictFileDairy.pkl", "wb")
        pickle.dump(x, filex)
        filex.close()

        filey = open("DictFileWetGoods.pkl", "wb")
        pickle.dump(y, filey)
        filex.close()

    except EOFError:
        filex = open("DictFileDairy.pkl", "wb")
        pickle.dump(x, filex)
        filex.close()

        filey = open("DictFileWetGoods.pkl", "wb")
        pickle.dump(y, filey)
        filex.close()


filename = "lists.csv"
Dairy = {'Fresh Milk': 150, 'NAN Gold(1kg)': 1590, 'Promil Gold(1kg)': 1480}
WetGoods = {'Ground Beef': 450, 'Chicken Wings': 280, 'Pork Knuckles': 350}

module = int(input('Merchandise:0 Customer:1  |  '))

initialize(Dairy, WetGoods)

# reading
file = open("DictFileDairy.pkl", "rb")
dairy = pickle.load(file)

file2 = open("DictFileWetGoods.pkl", "rb")
wetGoods = pickle.load(file2)


if module == 0:
    module2.edit()

elif module == 1:
    module1.cust_buy()
