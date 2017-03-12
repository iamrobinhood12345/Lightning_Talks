import sys


def transcribe_to_rna():
	strand = sys.argv[1]
	print(strand.replace("T", "U"))


transcribe_to_rna()