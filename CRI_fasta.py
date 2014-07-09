import fileinput, bz2, os, subprocess, random, gzip, time, shelve, string
from fileinput import FileInput
from subprocess import Popen
import operator
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--infile", type="string", dest="infilename",help="Input your read file name (FORMAT: sequences, illumina fastq, qseq,fasta)", metavar="FILE")
(options, args) = parser.parse_args()
                  
full_fasta_file=options.infilename

ll=full_fasta_file.split(".")
sample=ll[0]

#------------------------------------------------


def reverse_compl_seq(strseq):
	strseq=strseq.upper()
	rc_strseq=strseq.translate(string.maketrans("ATCG", "TAGC"))[::-1]
	return rc_strseq;

def RIP_product_CA(seq):
	rcseq=reverse_compl_seq(seq)
	n1=seq.count("TA")+rcseq.count("TA")
	n2=seq.count("AT")+rcseq.count("AT")
	if n2>0:
		r="%1.5f"%(float(n1)/n2)
	else:
		r="NA"
	return r;

def RIP_product_CC(seq):
	rcseq=reverse_compl_seq(seq)
	n1=seq.count("TC")+rcseq.count("TC")
	n2=seq.count("CT")+rcseq.count("CT")
	if n2>0:
		r="%1.5f"%(float(n1)/n2)
	else:
		r="NA"
	return r;

def RIP_product_CG(seq):
	rcseq=reverse_compl_seq(seq)
	n1=seq.count("TG")+rcseq.count("TG")
	n2=seq.count("GT")+rcseq.count("GT")
	if n2>0:
		r="%1.5f"%(float(n1)/n2)
	else:
		r="NA"
	return r;

def RIP_substrate_CA(seq):
	rcseq=reverse_compl_seq(seq)
	n1=seq.count("CA")+rcseq.count("CA")
	n2=seq.count("TG")+rcseq.count("TG")
	n3=seq.count("AC")+rcseq.count("AC")
	n4=seq.count("GT")+rcseq.count("GT")
	if (n3+n4) >0:
		r="%1.5f"%(float(n1+n2)/(n3+n4))
	else:
		r="NA"
	return r;

def RIP_substrate_CG(seq):
	rcseq=reverse_compl_seq(seq)
	n1=seq.count("CG")+rcseq.count("CG")
	n2=seq.count("CG")+rcseq.count("CG")
	n3=seq.count("GC")+rcseq.count("GC")
	n4=seq.count("GC")+rcseq.count("GC")
	if (n3+n4) >0:
		r="%1.5f"%(float(n1+n2)/(n3+n4))
	else:
		r="NA"
	return r;

def RIP_substrate_CT(seq):
	rcseq=reverse_compl_seq(seq)
	n1=seq.count("CT")+rcseq.count("CT")
	n2=seq.count("AG")+rcseq.count("AG")
	n3=seq.count("TC")+rcseq.count("TC")
	n4=seq.count("GA")+rcseq.count("GA")
	if (n3+n4) >0:
		r="%1.5f"%(float(n1+n2)/(n3+n4))
	else:
		r="NA"
	return r;
	
#------------------------------------------------

seq_dic={}
seq=""
header=""
g=""
for line in fileinput.input(full_fasta_file):
	l=line.split()
	if line[0]!=">":
		g=g+line[:-1]
	elif line[0]==">":
		if header=="":
			header=l[0][1:]
		else:
			g=g.upper()
			seq_dic[header]=g
			#print header,len(g);
			header=l[0][1:]
			g=""
			
fileinput.close()
g=g.upper()
seq_dic[header]=g

#---------------------------------------------------

outfile1='CRI_CA_'+sample+'_repeats.txt'
outfile2='CRI_CG_'+sample+'_repeats.txt'

outf1=open(outfile1,'w')
outf2=open(outfile2,'w')


mark=1
for id in seq_dic.keys():
		seq=seq_dic[id].upper()
		#--------------------------------------
		r1=RIP_product_CA(seq)
		#r2=RIP_product_CC(seq)
		r3=RIP_product_CG(seq)
		r4=RIP_substrate_CA(seq)
		r5=RIP_substrate_CG(seq)
		#r6=RIP_substrate_CT(seq)
		#--------------------------------------
		if r1 !="NA" and r4 !="NA":
			CRI_CA="%1.3f"%(float(r1)-float(r4))
			outf1.write("%s"%(CRI_CA)+"\n")
		#--------------------------------------
		if r3 !="NA" and r5 !="NA":
			CRI_CG="%1.3f"%(float(r3)-float(r5))
			outf2.write("%s"%(CRI_CG)+"\n")
outf1.close()			
outf2.close()			
			
			
			
		