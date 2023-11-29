def konsonan(kalimat):
    vokal = 'aiueoAIUEO'
    hasil = ""

    for huruf in kalimat:
        if huruf not in vokal:
            hasil += huruf
    return hasil

print("Huruf konsonan dari kata Nurul Fikri adalah", konsonan('Nurul Fikri'))