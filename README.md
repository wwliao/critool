# CRI Tool
Calculate composite RIP index (CRI) score and generate box plots

## Requirements
Python 2.7 and R

## License
MIT

## Repeat sequences (FASTA format)
- [Neurospora_crassa.unmasked.fasta.seqs.txt.gz](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/Neurospora_crassa.unmasked.fasta.seqs.txt.gz)
- [Saccharomyces_cerevisiae.EF4.66.dna.toplevel.fa.seqs.txt.gz](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/Saccharomyces_cerevisiae.EF4.66.dna.toplevel.fa.seqs.txt.gz)
- [Tuber_melanosporum_v1.0_unmasked.fa.seqs.txt.gz](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/Tuber_melanosporum_v1.0_unmasked.fa.seqs.txt.gz)
- [aspergillus_nidulans_fgsc_a4_1_contigs.fasta.seqs.txt.gz](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/aspergillus_nidulans_fgsc_a4_1_contigs.fasta.seqs.txt.gz)
- [uncinocarpus_reesii_2_supercontigs.fasta.seqs.txt.gz](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/uncinocarpus_reesii_2_supercontigs.fasta.seqs.txt.gz)

## Calculate CRI score for each repeat
See other procedures in Methods for the CRI formula.

Example:

    $ python CRI_fasta.py -f Tuber_melanosporum_v1.0_unmasked.fa.seqs.txt
    
Output files:

- [CRI_CA_Tuber_melanosporum_v1_repeats.txt (CA->TA)](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CA_Tuber_melanosporum_v1_repeats.txt)
- [CRI_CG_Tuber_melanosporum_v1_repeats.txt (CG->TG)](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CG_Tuber_melanosporum_v1_repeats.txt)

All outputs:

- [CRI_CA_Neurospora_crassa_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CA_Neurospora_crassa_repeats.txt)
- [CRI_CA_aspergillus_nidulans_fgsc_a4_1_contigs_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CA_aspergillus_nidulans_fgsc_a4_1_contigs_repeats.txt)
- [CRI_CA_Saccharomyces_cerevisiae_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CA_Saccharomyces_cerevisiae_repeats.txt)
- [CRI_CA_Tuber_melanosporum_v1_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CA_Tuber_melanosporum_v1_repeats.txt)
- [CRI_CA_uncinocarpus_reesii_2_supercontigs_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CA_uncinocarpus_reesii_2_supercontigs_repeats.txt)
- [CRI_CG_aspergillus_nidulans_fgsc_a4_1_contigs_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CG_aspergillus_nidulans_fgsc_a4_1_contigs_repeats.txt)
- [CRI_CG_Saccharomyces_cerevisiae_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CG_Saccharomyces_cerevisiae_repeats.txt)
- [CRI_CG_Tuber_melanosporum_v1_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CG_Tuber_melanosporum_v1_repeats.txt)
- [CRI_CG_uncinocarpus_reesii_2_supercontigs_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CG_uncinocarpus_reesii_2_supercontigs_repeats.txt)
- [CRI_CG_Neurospora_crassa_repeats.txt](http://paoyang.ipmb.sinica.edu.tw/~paoyang/truffle/CRI_tool/CRI_CG_Neurospora_crassa_repeats.txt)

## Generate box plots
Run R program:

    Boxplot-CRI-Tuber-vs-other4.R
    
Output files:

![](https://raw.githubusercontent.com/wwliao/critool/develop/test/Box-CRI-repeats-CA-Tuber-vs-other4.png)
![](https://raw.githubusercontent.com/wwliao/critool/develop/test/Box-CRI-repeats-CG-Tuber-vs-other4.png)
