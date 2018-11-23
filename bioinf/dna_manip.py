#/usr/bin/env python
def comp_str(seq):
    #prompt = input('Enter valid single strand SEQ:').strip()
    dnaseq= seq.upper()
    comp_seq=''
    for n in dnaseq:
        valid =["A","C","G","T"]
        if n is "A":
            comp_seq += "T"
        elif n is "C":
            comp_seq += "G"
        elif n is "G":
            comp_seq += "C"
        elif n is "T":
            comp_seq += "A"
        elif n not in valid:
            print("Invalid Character in Seq {}".format(dnaseq))
            comp_str()
            break
    return comp_seq

def inv_str(seq):
    i = -1
    inv_seq=''
    while i >= (-len(seq)):
        inv_seq += seq[i]
        i -= 1
    return inv_seq

if __name__ == "__main__":
    comp_seq = comp_str('TACGA')
    print('Reverse strand  sequence is',comp_seq)
    inv_seq = inv_str('AGCAT')
    print('Inverse strand  sequence is',inv_seq)
