
#!/admin/desktop/python

# gc count

dna=input("enter your dna sequence pls :")
no_c =dna.count('c')
no_g =dna.count('g')
dna_length = len(dna)
dna_percent = (no_c + no_g) * 100.0 / dna_length
print("the gc percent of given DNA sequence is %5.3f %%” % dna_percent")

