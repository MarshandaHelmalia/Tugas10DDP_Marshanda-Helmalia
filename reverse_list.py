fruits = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def balikan(fruits):
    hasil = []

    for i in  range(len(fruits)-1, -1, -1):
        hasil.append(fruits[i])
    return hasil

output = balikan(fruits)
print(output)