def bioinformatics(dna, k):
    count = {}
    x = len(dna)
    for i in range(0, x, k):
        result = dna[i:i+k]
        count.setdefault(result, 0)
        count[result] += 1
    return count

if __name__=="__main__":
    dna_input = input("Enter a string of DNA: ")
    k_mer = int(input("Enter an integer: "))
    print(bioinformatics(dna_input, k_mer))
