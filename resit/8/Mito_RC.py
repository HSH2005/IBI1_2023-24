import re
c = input('the file name is:')
input_file= open(c,'r')
output_file = open("mito_genes.fa",'w')
def hsh(seq):
    com =''
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
    return(com1)
def duplication(inputfile,outputfile):
    with open(inputfile,'r') as fasta_file:
        with open(outputfile,'w') as output_fasta:
            sequence=[]
            sequence1 = []
            genename=None
            for line in fasta_file:
                if line.startswith('>'):
                    sequence.append(hsh(sequence1))
                    sequence1 = []
                    if sequence and genename:
                        output_fasta.write(''.join(sequence)+'\n')
                        sequence=[]
                    if 'protein_coding' in line:
                        genename_match=re.search(r'>(\S+)',line)
                        if genename_match:
                            genename=genename_match.group(1)
                            output_fasta.write(f'>{genename}\n')
                    else:
                        genename=None
                elif genename:
                    sequence.append(line.strip())
                    sequence1.append(line.strip())
               
                

                     

duplication(input_file,output_file)