threshold = 1000
genome = 0
genome_no_N = 0
D={}
D2={}
for line in open('m_knwr_snps_consensus.fa'):
    print(line.strip())
    if line[0]==">":
        contig = line.strip().split()[0].strip(">")
        D[contig]=0
        D2[contig]=0
        continue
    seq = line.strip()
    D[contig] += len(seq)
    Ns = seq.count("N")
    seq_no_N = len(seq)-Ns
    D2[contig] += seq_no_N
    #if len(D)>threshold:
    #    break
for tig in D:
    genome += D[tig]

for t in D2:
    genome_no_N += D2[t]

print("genome", genome)
print("genome_no_N", genome_no_N)
