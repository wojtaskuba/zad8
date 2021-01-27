with open('plik.txt', '+w') as f:
    f.write('LoremIpsum')
    f.seek(0)
    for line in f:
        print(line)