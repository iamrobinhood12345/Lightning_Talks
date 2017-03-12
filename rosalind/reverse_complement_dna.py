import sys


def reverse_complement_dna():
	strand = (sys.argv[1])[::-1]
	new_strand_list = []
	complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	for i in strand:
		new_strand_list.append(complement[i])
	print(''.join(new_strand_list))


reverse_complement_dna()