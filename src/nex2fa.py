#!/usr/bin/env python3
from Bio import SeqIO
import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2],'w')

records = SeqIO.parse(f1, "nexus")
count = SeqIO.write(records, f2, "fasta")
print("Converted %i records" % count)
