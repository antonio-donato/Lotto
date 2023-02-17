def most_likely_ambo(history):
  total_numbers = 90
  number_counts = [0] * total_numbers
  
  # Contare quante volte ogni numero è uscito nello storico per ogni Ruota
  for draw in history:
    for number in draw:
        if 1 <= number <= total_numbers:
            number_counts[number - 1] += 1  
  # Trovare i due numeri meno presenti
  least_likely_numbers = sorted(range(total_numbers), key=lambda x: number_counts[x])[:2]
  return least_likely_numbers

# history = [[13, 24, 35, 46, 57], [68, 79, 80, 91, 2], [3, 14, 25, 36, 47]]
# likely_ambo = most_likely_ambo(history)
# print("L'ambo più probabile è composto dai numeri:", likely_ambo)


def archivio_lotto(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()

    records = [line.strip() for line in lines]

    nuova_lista = {}
    for record in records:
        estr_data, ruota, n1, n2, n3, n4, n5 = record.split()
        draw = [int(n1), int(n2), int(n3), int(n4), int(n5)]
        if ruota not in nuova_lista:
           nuova_lista[ruota] = []
        nuova_lista[ruota].append(draw)

        # nuova_lista.append([int(parti[2]), int(parti[3]), int(parti[4]), int(parti[5]), int(parti[6])])
    return nuova_lista

history = archivio_lotto("ArchivioLotto.italia.txt")
for ruota, hist in history.items():
    likely_ambo = most_likely_ambo(hist)
    print("L'ambo più probabile sulla ruota di {} è: {}".format(ruota, likely_ambo))
