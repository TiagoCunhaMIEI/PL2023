import matplotlib.pyplot as plt

def lercsv():
    file = open("myheart.csv")
    dic = dict()
    i = 0
    for line in file:
        if i != 0:
            dic[i] = line.split(",")
        i += 1
    return dic


def distri_sexo(file):
    print("Distribuição por sexo:")
    male = 0
    female = 0
    for key in file.keys():
        if file[key][5] == "1\n":
            if file[key][1] == "M":
                male += 1
            else:
                female += 1
    print(str(male) + " doentes masculinos")
    print(str(female) + " doentes femeninas")

def get_oldest(file):
    oldest = 0
    for key in file.keys():
        if oldest < int(file[key][0]):
            oldest = int(file[key][0])
    return oldest

def age_aux(file,i):
    total = 0
    totalI = 0
    for key in file.keys():
        if i <= int(file[key][0]) < i + 4:
            if file[key][5] == "1\n":
                totalI += 1
            total+=1
    print("[" + str(i) + "," + str(i + 4) + "]: " + str(total) + " registados, " + str(totalI) + " doentes")



def distri_age(file):
    print("Distribuição por escalões etários:")
    oldest = get_oldest(file)
    i=30
    while i < oldest:
        age_aux(file,i)
        i+=5

def get_high_col(file):
    high = 0
    for key in file.keys():
        if high < int(file[key][3]):
            high = int(file[key][3])
    return high

def col_aux(file,i):
    totalR = 0
    totalI = 0
    for key in file.keys():
        if i <= int(file[key][3]) < i + 10:
            if file[key][5]=="1\n":
                totalI += 1
            totalR += 1
    print("[" + str(i) + "," + str(i + 10) + "]: " + str(totalR) + " registados, " + str(totalI) + " Doentes")


def distri_col(file):
    print("Distribuição por colesterol:")
    highest_col = get_high_col(file)
    i = 80;
    while i < highest_col:
        col_aux(file,i)
        i += 10

def tabela_sexo(file):
    labels = ["Masculino", "Femenino"]
    list = [0,0]

    for key in file.keys():
        if file[key][5] == "1\n":
            if file[key][1] == "M":
                list[0] += 1
            else:
                list[1] += 1

    plt.bar(labels, list, width=0.5)

    plt.xlabel("Sexo")
    plt.ylabel("Nº de Doentes")
    plt.title("Distribuição da doença por sexo")

    plt.show()

def tabela_idade(file):
    escaloes = list()
    escaloesDoente = list()
    oldest = get_oldest(file)
    i = 30
    c = 0
    while i < oldest:
        totalI = 0
        escaloes.append("[" + str(i) + "," + str(i + 4) + "]")
        escaloesDoente.append(0)
        for key in file.keys():
            if i <= int(file[key][0]) < i + 4:
                if file[key][5] == "1\n":
                    totalI += 1
        escaloesDoente[c] = totalI
        c += 1
        i += 5

    plt.bar(escaloes, escaloesDoente, width=0.5)
    plt.xlabel("Escalão Etário")
    plt.ylabel("Nº de Doentes")
    plt.title("Distribuição da doença por escalões etários.")
    plt.show()

def tabela_col(file):
    escaloesCol = list()
    escaloesColDoente = list()
    highest_col = get_high_col(file)
    i = 80
    c = 0
    while i < highest_col:
        totalI = 0
        escaloesCol.append("[" + str(i) + "," + str(i + 10) + "]")
        escaloesColDoente.append(0)
        for key in file.keys():
            if i <= int(file[key][3]) < i + 10:
                if file[key][5] == "1\n":
                    totalI += 1
        escaloesColDoente[c] = totalI
        c += 1
        i += 10

    plt.bar(escaloesCol,escaloesColDoente,width=0.5)
    plt.xlabel("Escalão colestrol")
    plt.ylabel("Nº de doentes")
    plt.title("Distribuição da doença por escalões de colestrol.")
    plt.show()






def main():
    f = lercsv()
    while 1:
        menu = {
            "1": " -Distribuição da doença pelo sexo",
            "2": " -Distribuição da doença pela idade",
            "3": " -Distribuição da doença pelo colesterol",
            "4": " -Tabela referente á Distribuição da doença pelo sexo",
            "5": " -Tabela referente á Distribuição da doença pela idade",
            "6": " -Tabela referente á Distribuição da doença pelo colesterol",
            "7": " -Sair"
        }
        for op in menu:
            print(op + menu.get(op))

        op = input("Escolha uma das opções acima: ")
        print("\n")

        if op == "1":
            distri_sexo(f)
            print("\n")
        if op == "2":
            distri_age(f)
            print("\n")
        if op == "3":
            distri_col(f)
            print("\n")
        if op == "4":
            tabela_sexo(f)
            continue
        if op == "5":
            tabela_idade(f)
            continue
        if op == "6":
            tabela_col(f)
            continue
        if op == "7":
            break

    print()



main()
