
def show_all():
    file = open('sample.txt', 'r', encoding='UTF=8')
    data = file.readlines()
    print(data)
    file.close()
    #print(data[0])
    for i in data:
        print(i)