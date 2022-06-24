import json

def readNumbers():
    with open("data.json", "r") as json_data:
        data = json.load(json_data)
        total = sum(data.values())
        for d in data:
            percentage = str( round( (data[d] / total * 100), 1)) + "%" + f" ({data[d]})"
            data[d] = percentage 
        data_with_percentage = json.dumps(data, indent = 4)
        print(data_with_percentage)
        json_data.close()
        confirm = input("Vuoi salvare i dati? 1-Si | 2-No ")
        if int(confirm) == 1:
            with open("saved_data.txt", "w") as saved_data:
                saved_data.write(data_with_percentage)
                saved_data.close()


def insertNumbers():

    numbers = ""

    giocata = input("Inserisci giocata: ")

    serie = giocata.split()

    if(len(serie) != 6):
        print("I numeri devono essere 6")
        return

    if len(serie) > len(set(serie)):
        print("I numeri devono essere tutti diversi")
        return



    with open("data.json") as json_data:
        data = json.load(json_data)
        numbers = data
        json_data.close()


    for s in serie:
        s = str(s)
        if s not in numbers:
            numbers[s] = 1
        else:
            numbers[s] +=1


    with open("data.json", "w") as json_data:
        jsonString = json.dumps(numbers, indent=4)
        json_data.write(jsonString)
        json_data.close()

def resetData():
    confirm = input("Sei sicuro di voler eliminare i dati? 1-Si | 2-No ")
    if(int(confirm) == 1):
        with open("data.json", "w") as json_data:
            data = {}
            jsonString = json.dumps(data)
            json_data.write(jsonString)
            json_data.close()