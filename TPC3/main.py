if __name__ == '__main__':
    try:
        with open('processos.txt', 'r') as ficheiro:
            texto = ficheiro.read()

        frequencias = {
            'ano': {},
            'nome': {},
            'apelido': {},
            'relacao familiar': {}
        }

        frase = "Doc.danificado"

        for linha in texto.split("\n"):
            i = 0
            if frase in linha:
                j = 3
            for elem in linha.split("::"):
                if i == 1:
                    ano = elem.split("-")
                    if frequencias['ano'].get(ano[0]) is not None:
                        frequencias['ano'][ano[0]] += 1
                    else:
                        frequencias['ano'][ano[0]] = 1
                elif i > 1:
                    elem2 = elem.split(",")
                    elem3 = elem2[0].split(" ")

                    if frequencias['nome'].get(elem3[0]) is not None:
                            frequencias['nome'][elem3[0]] += 1
                    else:
                        frequencias['nome'][elem3[0]] = 1

                    if frequencias['apelido'].get(elem3[-1]) is not None:
                        frequencias['apelido'][elem3[-1]] += 1
                    else:
                        frequencias['apelido'][elem3[-1]] = 1

                    if len(elem2) > 1 and elem2[1] is not None:
                        parente = elem2[1].split(".")
                        if frequencias['relacao familiar'].get(parente[0]) is not None:
                            frequencias['relacao familiar'][parente[0]] += 1
                        else:
                            frequencias['relacao familiar'][parente[0]] = 11
                i += 1
        print("Distribuição por Ano: \n")
        print(frequencias['ano'])
        print("\n")
        print("Distribuição por Nome Próprio: \n")
        print(frequencias['nome'])
        print("\n")
        print("Distribuição por apelido: \n")
        print(frequencias['apelido'])
        print("\n")
        print("Distribuição por Parentesco: \n")
        print(frequencias['relacao familiar'])

    except Exception as e:
        print(e)




