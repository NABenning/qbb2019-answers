head -n 400000 ~/qbb2019-answers/rawdata/SRR072893.fastq > ~/qbb2019-answers/day2-lunch/SRR072893.10k.fastq

fastqc SRR072893.10k.fastq 

hisat2 -p 4 -x ~/qbb2019-answers/genomes/BDGP6 -U ~/qbb2019-answers/day2-lunch/SRR072893.10k.fastq > ~/qbb2019-answers/day2-lunch/SRR072893.10k.sam 

samtools sort -@ 4 SRR072893.10k.sam -o SRR072893.10k.bam

samtools index -b -@ 4 SRR072893.10k.bam SRR072893.10k.bam.bai

stringtie SRR072893.10k.bam -o SRR072893.10k.gtf -p 4 -G ~/qbb2019-answers/day1-morning/BDGP6.Ensembl.81.gtf -B -e