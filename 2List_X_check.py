# Compare my uncovered addresses (addr_priv.txt) to the existing bitcoin addresses (test1.csv)
# this file takes addr_priv and strips out the extra columns
# then it converts test1.csv into a txt file called test1_fixed.txt
# then it compares the two lists of addresses to see if there are any matches,
# if so, then we have successfully found an address for which we have the private address
# address and private key printed to FREE_MONEY.txt (as an append, better to have the result twice than have it lost)

### CONVERT the existing btc addresses CSV to txt ###
import csv
csv_file = 'test1.csv'
txt_file = 'test1.txt'
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(",".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

### Strip the balance and RIPEMD160 (column 2 and 3) data leaving just the raw addresses of column 1
f = open("test1.txt", "r")
g = open("test1_fixed.txt", "w")  # Name of the clean file.

for line in f:
    if line.strip():
        g.write("\t".join(line.split(",")[:1]) + "\n")

f.close()
g.close()

### Strip the balance and RIPEMD160 (column 2 and 3) data leaving just the raw addresses of column 1
f = open("addr_priv.txt", "r")
g = open("MYaddresses.txt", "w")  # Name of the clean file.

for line in f:
    if line.strip():
        g.write("\t".join(line.split(",")[:1]) + "\n")

f.close()
g.close()

### ADDRESS MATCHING ALGO ! ### https://www.codespeedy.com/find-the-common-elements-in-two-lists-in-python/
print(" \n >>> Now comparing your list against known bitcoin addresses... \n")

file = open("test1_fixed.txt")
a = [line for line in file]
file.close()
# print(a)

file2 = open("MYaddresses.txt")
b = [line2 for line2 in file2]
file2.close()


def common(lst1, lst2):             #### Using <set> to compare two lists
    return list(set(lst1) & set(lst2))
e=common(a,b)
#convert e(list) into a string:
WinningString = ''.join(e)

# saving matches to file:
def save_winners(abc):
    if abc != 0:
        print ("YOU ONLY WENT AND BLOODY FOUND SOME FREE MONEY !! \n \t\t[($)] ")
        print(WinningString + " \t\t[($)] "+"\n  \t\t     ...these addresses are also saved to the file < FREE_MONEY.txt >")
        print('\a')
        z = open("FREE_MONEY.txt", "at")  # Save the matches to a file so we dont lose them, as an append too.
        z.write(WinningString)
        z.close()
    else:
        print (" no luck this time ... keep permutating!")
        print("\n")

save_winners(e)

