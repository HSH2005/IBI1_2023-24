xfile = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
a=xfile.read()
seq1 = "GTGTGT"
seq2 = "GTCTGT"
import re
cseq1=len(re.findall(seq1, a))
cseq2=len(re.findall(seq2, a))
count = cseq1 + cseq2
print(count)