# Compare my uncovered addresses (addr_priv.txt) to the existing bitcoin addresses (test1.csv)
# this file takes addr_priv and strips out the extra columns
# then it converts test1.csv into a txt file called test1_fixed.txt
# then it compares the two lists of addresses to see if there are any matches,
# if so, then we have successfully found an address for which we have the private address
# address and private key printed to FREE_MONEY.txt (as an append, better to have the result twice than have it lost)

### CONVERT the existing btc addresses CSV to txt ###
import csv
def csv_txt():
    csv_file = 'test1.csv'
    txt_file = 'test1.txt'
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(",".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

csv_txt()

### Strip the balance and RIPEMD160 (column 2 and 3) data leaving just the raw addresses of column 1

def strip_cols_database():
    f = open("test1.txt", "r")
    g = open("test1_fixed.txt", "w")  # Name of the clean file.
    for line in f:
        if line.strip():
            g.write("\t".join(line.split(",")[:1]) + "\n")
    f.close()
    g.close()

strip_cols_database()

### Strip the balance and RIPEMD160 (column 2 and 3) data leaving just the raw addresses of column 1
def strip_cols_MyAddresses():
    f = open("addr_priv.txt", "r")
    g = open("MYaddresses.txt", "w")  # Name of the clean file.
    for line in f:
        if line.strip():
            g.write("\t".join(line.split(",")[:1]) + "\n")
    f.close()
    g.close()

strip_cols_MyAddresses()

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

number_of_winners = len(e)
if number_of_winners > 0: print ("NO OF WINNERS: ",number_of_winners, "\n")


# saving matches to file:
def save_winners(abc):
    if abc != 0:
        WinningString = ''.join(e)
        print ("YOU ONLY WENT AND BLOODY FOUND SOME FREE MONEY !! \n \t\t[($)] ")
        print(WinningString + " \t\t[($)] \t\t... Private key not printed to screen")
        print('\a')
        z = open("FREE_MONEY.txt", "at")  # Save the matches to a file so we dont lose them, as an append too.
        z.write(WinningString)
        z.close()
    else:
        print (" no luck this time ... keep permutating!")
        print("\n")

WinningString = ''.join(e)
save_winners(e) # call the above function

### Now we create a file with the private keys copied in, again as an 'append' so we dont risk overwriting previously found keys
def save_winning_keys():
    FILE1 = "FREE_MONEY.txt"
    FILE2 = "addr_priv.txt"
    OUTPUT = "FREE_MONEY_KEYS.txt"

    with open(FILE1) as inf:
        match = set(line.strip() for line in inf)

    with open(FILE2) as inf, open(OUTPUT, "a") as outf:
        for line in inf:
            if line.split(',', 1)[0] in match:
                outf.write(line)
    print("\n  ...these addresses are also saved to the file < FREE_MONEY.txt > \n\t ...the private keys are saved to < FREE_MONEY_KEYS.txt >\n")

if number_of_winners > 0: save_winning_keys() 

## Clean up files for *unique-only* results and avoid reptition:

import hashlib
output_file_path = "FREE_MONEY_KEYS_unique_results.txt"
input_file_path = "FREE_MONEY_KEYS.txt"
completed_lines_hash = set()
output_file = open(output_file_path, "w")

for line in open(input_file_path, "r"):
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()

output_file_path = "FREE_MONEY_unique_results.txt"
input_file_path = "FREE_MONEY.txt"
completed_lines_hash = set()
output_file = open(output_file_path, "w")

for line in open(input_file_path, "r"):
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
output_file.close()
 ## I am proud of how lazy my code is, until I have to run it ##

