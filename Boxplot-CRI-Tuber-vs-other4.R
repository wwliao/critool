require(graphics)
require(plotrix)

file1=paste("CRI_CA_Tuber_melanosporum_v1_repeats.txt",sep="")
file2=paste("CRI_CA_Neurospora_crassa_repeats.txt",sep="")
file3=paste("CRI_CA_uncinocarpus_reesii_2_supercontigs_repeats.txt",sep="")

file4=paste("CRI_CA_aspergillus_nidulans_fgsc_a4_1_contigs_repeats.txt",sep="")


file5=paste("CRI_CA_Saccharomyces_cerevisiae_repeats.txt",sep="")

dat<-read.table(file1)
chr1=dat$V1
dat<-read.table(file2)
chr2=dat$V1
dat<-read.table(file3)
chr3=dat$V1
dat<-read.table(file4)
chr4=dat$V1
dat<-read.table(file5)
chr5=dat$V1



#--------------------------------

mat=cbind(ts(chr1),ts(chr2),ts(chr3),ts(chr4),ts(chr5))
mat=data.frame(mat)
colnames(mat)<-c("T. melanosporum","N. crassa","U. reesii","A. nidulans","S. cerevisiae")

outfile=paste("Box-CRI-repeats-CA-Tuber-vs-other4.png",sep = "",collapse='')

bitmap(outfile,type="png16m",width=4.3,height=2, res=450)

boxplot(mat,outline=FALSE,range=1.5,notch=TRUE,varwidth=FALSE,main="Composite RIP index (CA->TA)",ylab="Composite RIP index",col=c("yellowgreen","dodgerblue","dodgerblue","gray","gray"),ylim=c(-5,5),cex.main=1.2,cex.lab=1,cex.axis=1.2)

abline(h=0,lty=3,col="red")
abline(v=1.5,lty=1,col="gray4")
abline(v=8.5,lty=1,col="gray4")

dev.off()
