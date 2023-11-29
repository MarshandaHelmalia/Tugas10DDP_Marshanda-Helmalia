listbuah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikasi(listbuah):
    list_buahbaru = []
    for buah in listbuah:
        list_buahbaru.append(buah)
        list_buahbaru.append(buah)
    return list_buahbaru

hasil_duplikasi = duplikasi(listbuah)
print(hasil_duplikasi)