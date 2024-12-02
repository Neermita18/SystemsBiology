from Bio.Seq import Seq
import Bio.Seq as s
import Bio
data= Seq("AGGGAGTTCTCTAGA")
print(data)
print(dir(Bio.Seq))
print(s.CodonTable)

## DNA methods

dna= s.Seq("attcgcgcgtatatc")
print(dna.transcribe())
print(dna.translate())
print(dna.reverse_complement())
print(dna.reverse_complement_rna())
print(dna.find("tt"))
print(dna.back_transcribe())
print(dna.count("cgc"))
print(dna.count_overlap("cgc"))
spacer=s.Seq(' ')
spr=spacer.join("actg")
print(spr)
print(dna.replace('a', 'm'))
dna2=Bio.Seq.MutableSeq('a-tt--g-c-t-ac-tg')
print(dna2.ungap('-'))