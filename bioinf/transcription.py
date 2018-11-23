#!/usr/bin/python
__authour__="Abdulvahab"
from dna_manip import comp_str,inv_str
# Checking for CFTR susseptibility of a paitient
# Enter seq as argument with 5' or 3' at the begining of string
def user_input():
    seq = 'none'
    while (seq[0] != '3' or '5') and (seq[1] != "\'"):
        seq = input("Enter valid gene Sequence to test with orientation 3' or 5' in start :  ").upper()
    return seq

def transcription(seq):
    orientation = seq[0]
    template = input("IS it template Strand(y/n)?: ").lower()
    if (orientation == "3") and (template == ('y' or 'yes')):
        template3 = seq[3:]
        nontemplate5 = comp_str(template3)
    elif (orientation == "5") and (template == ('y' or 'yes')):
        template5 = seq[3:]
        #print(template5)
        template3 = inv_str(template5)
        #print(template3)
        nontemplate5 = comp_str(template3)
        #print(nontemplate5)
    elif (orientation == "5") and (template == ('n' or 'no')):
        nontemplate5 = seq[3:]
    else:
        nontemplate3 = seq[3:]
        nontemplate5 = inv_str(nontemplate3)
    mrna = nontemplate5.replace("T","U")
    return mrna
if __name__ == "__main__":
    seq = user_input()
    mrna = transcription(seq)
    print (mrna)
