import sys




def main():
    lines = []
    show = 0
    count = 1
    r = 0
    i = 0
    print("Insira o texto")
    lines = input()
    while i < len(lines):
        if lines[i] == '=':
            show = 1
            i += 1
        elif lines[i].lower() == 'o' and lines[i+1].lower() == 'n':
            count = 1
            i += 2
        elif lines[i].lower() == 'o' and lines[i+1].lower() == 'f' and lines[i+2].lower() == 'f':
            count = 0
            i += 3
        elif lines[i].isdigit():
            if count == 1:
                r += int(lines[i])
                i += 1
            else:
                i += 1

    if show == 1:
        print("Resultado: " + str(r))







if __name__ == '__main__':
    main()


