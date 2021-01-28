# lookup-bitcoin-addresses

Compare my discovered addresses (addr_priv.txt) to the existing bitcoin addresses (test1.csv)
this file (2List_X_check.py) takes addr_priv and strips out the extra columns
then it converts test1.csv into a txt file called test1_fixed.txt
then it compares the two lists of addresses to see if there are any matches,
if so, then we have successfully found an address for which we have the private address
address and private key printed to FREE_MONEY.txt (as an append, better to have the result twice than have it lost)

TO RUN:

> python 2List_X_check.py
 