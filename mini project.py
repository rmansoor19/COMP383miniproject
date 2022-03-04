import os
from Bio import SeqIO
# importing the os module and BioPython

os.mkdir("/Users/rmansoor/Downloads/results")
#creating a directory under downlaods called "results" to store all my results
results = "/Users/rmansoor/Downloads/results"

outfile = open("/Users/rmansoor/Downloads/results/miniproject.log", "w")
#creating a log file within my new results folder to store commands, contigs, and basepairs.

# number 1: Fetching the file
os.system("/Users/rmansoor/Downloads/sratoolkit.2.11.2-mac64/bin/prefetch SRR8185310" + " -O " + results)
#download the SRA file (in SRA format), using prefetch command
reads = "/Users/rmansoor/Downloads/results/SRR8185310/SRR8185310.sra"
os.system("/Users/rmansoor/Downloads/sratoolkit.2.11.2-mac64/bin/fasterq-dump " + reads + " -O " +results)
#translate the SRA format file to fastq format, using fasterq-dump.
datafastq = "/Users/rmansoor/Downloads/results/SRR8185310.fastq"


# If you run into any errors when runnign SRAtoolkit than involve: vdb-config -i
# please use the following link adn run the commands in your terminal to complete quick tool configuration
# https://github.com/ncbi/sra-tools/wiki/03.-Quick-Toolkit-Configuration



# number 2: Using Spades
spades = "/Users/rmansoor/Downloads/SPAdes-3.15.4-Darwin/bin/spades.py -k 55,77,99,127 -t 2 --only-assembler -s " + datafastq + " -o " +results
# This command will look inside the bin folder inside the SPAdes folder and complete the assembly
os.system(spades)
outfile.write("SPAdes Command: " + spades + " \n" + "\n")
#writing the SPAdes command to the miniproject.log file



#number 3:
seqs=[] # creating an empty lsit
data = SeqIO.parse('/Users/rmansoor/Downloads/results/contigs.fasta','fasta')
#Under the results folder, a file named "contigs.fasta" was created with the assembled contigs file. 
# we are reading this file in fasta format
for record in data:
    #for each record in the contigs.fasta file
    if len(record.seq) > 1000:
        #if the len of the record is greater than 1000 base pairs:
        seqs.append(record)
        #add the records to the list called seqs

longseqs = ("There are " + str(len(seqs)) + " contigs > 1000 in the assembly.")
#print the correct command that explains the number of contigs greater than 1000 in the assembly.
outfile.write(longseqs + " \n" + " \n")
#write the command to the log file 
SeqIO.write(seqs, "/Users/rmansoor/Downloads/results/long_seqs.fasta", "fasta")
#create a new file called "Long_seqs.fasta" in fasta format that will store all contigs greater than 1000
count = 0
#intitlaize count as zero






#number 4:
data2 = SeqIO.parse('/Users/rmansoor/Downloads/results/long_seqs.fasta','fasta')
# read the newly created file in fasta format with all contigs greater than 1000 base pairs
for record in data2:
    #for each record in the long_seqs.fasta file
    count = count + len(record)
    #add the length of each record to count
bp = ('There are ' + str(count) + ' bp in the assembly.')
#print the correct command that explains the total number of bp in all of the contigs > 1000 bp in length
outfile.write(bp + " \n" + " \n")
#write the command to the log file 
outfile.close()
#close the file