import sys

import random

 

def is_valid_dna(scrambled):

    # Check for no tetrahomomers (four consecutive identical nucleotides)

    for i in range(len(scrambled) - 3):

        if scrambled[i] == scrambled[i+1] == scrambled[i+2] == scrambled[i+3]:

            return False

    return True

 

def scramble_dna(dna_string):

    scrambled = list(dna_string)

    # Continue scrambling until a valid string is found

    while True:

        random.shuffle(scrambled)

        scrambled_str = ''.join(scrambled)

        if is_valid_dna(scrambled_str):

            return scrambled_str

 

if __name__ == "__main__":

    # Check for command line arguments

    if len(sys.argv) != 2:

        print("Usage: python script.py DNA_string")

        sys.exit(1)

 

    dna_string = sys.argv[1].upper()

 

    # Validate that the input string contains only A, T, C, G

    if not all(base in "ATCG" for base in dna_string):

        print("Error: DNA string should contain only A, T, C, and G")

        sys.exit(1)

 

    scrambled_dna = scramble_dna(dna_string)

    print(f"Original DNA: {dna_string}")

    print(f"Scrambled DNA: {scrambled_dna}")
