import sys


def count_nucleotides():
	A = sys.argv[1].count('A')
	C = sys.argv[1].count('C')
	G = sys.argv[1].count('G')
	T = sys.argv[1].count('T')
	print(str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T))


count_nucleotides()