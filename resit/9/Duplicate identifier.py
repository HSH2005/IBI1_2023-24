gene_names = ['DLX5', 'DLX6', 'NBAS', 'BRCA2', 'BRCA2', 'NBAS']
unique = []
deunique = []
for i in gene_names:
    if i not in unique:
        unique.append(i)
    elif i not in deunique:
        deunique.append(i)
for i in deunique:
    unique.remove(i)
print('unique:',unique,'deunique:',deunique)