seq ='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
com = ''
for i in seq:
    if i == 'A':
        com += 'T'
    if i == 'T':
        com += 'A'
    if i == 'G':
        com += 'C'
    if i == 'C':
        com += 'G'
com1 = ''.join(reversed(com))
print(com1)