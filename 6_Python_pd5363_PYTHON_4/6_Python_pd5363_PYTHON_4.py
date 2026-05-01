gen1 = 'PDCD1'
dna_target = 'ATCGACGATGG'
seq_length = 0.4 # Długość w kb
print('Type of gen1: ', type(gen1), 'Type of dna_target: ', type(dna_target), 'Type of seq_length: ', type(seq_length))
print('Gen: ', gen1)
print('DNA target: ', dna_target)
print('Sequence length: ', seq_length, 'kb')
# Obliczanie procentu targetu w sekwencji
print('% Target/Sequence: ', (len(dna_target) / (seq_length * 1000)) * 100, '%')

