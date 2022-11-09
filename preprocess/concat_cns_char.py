import os

filenames = ['CNS2UNICODE_Unicode 2.txt', 'CNS2UNICODE_Unicode 15.txt', 'CNS2UNICODE_Unicode BMP.txt']
with open('cns_char.txt', 'w') as outfile:
    for fname in filenames:
        with open(os.path.join("preprocess", fname)) as infile:
            outfile.write(infile.read())
