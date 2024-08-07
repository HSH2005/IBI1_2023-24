import re
input_file= open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
output_file = open("mito_genes.fa",'w')
def duplication(inputfile,outputfile):
    with open(inputfile,'r') as fasta_file:
        with open(outputfile,'w') as output_fasta:
            sequence=[]
            genename=None
            for line in fasta_file:
                if line.startswith('>'):
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

duplication(input_file,output_file)