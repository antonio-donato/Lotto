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








#####################

# def most_likely_ambo(history):
#   total_combinations = 90
#   combination_counts = {}
  
#   # Contare quante volte ogni combinazione di ambi è uscita nello storico per ogni Ruota
#   for draw in history:
#     for i in range(len(draw)):
#       for j in range(i+1, len(draw)):
#         combination = [draw[i], draw[j]]
#         combination.sort()
#         if tuple(combination) in combination_counts:
#           combination_counts[tuple(combination)] += 1
#         else:
#           combination_counts[tuple(combination)] = 1
  
#   # Trovare la combinazione di ambi più probabile
#   most_likely_combination = max(combination_counts, key=combination_counts.get)
#   return most_likely_combination

def archivio_lotto(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()

    records = [line.strip() for line in lines]

    nuova_lista = []
    for record in records:
        parti = record.split()
        nuova_lista.append([int(parti[2]), int(parti[3]), int(parti[4]), int(parti[5]), int(parti[6])])
    return nuova_lista

history = archivio_lotto("ArchivioLotto.italia.txt")
likely_ambo = most_likely_ambo(history)
print("L'ambo più probabile è:", likely_ambo)
