import sys
import csv
from csv import DictReader

csv.field_size_limit(sys.maxsize)

# open file in read mode
# with open('transactions.csv', 'r') as read_obj:
#     csv.field_size_limit(sys.maxsize)
#     # pass the file object to DictReader() to get the DictReader object
#     reader = DictReader(read_obj)
#     # iterate over each line as a ordered dictionary
#     for row in reader:
#         # row variable is a dictionary that represents a row in csv
#         print(row['from_address'], row['to_address'])


with open('addresses.csv', 'w', newline='') as addr_csv:
    addr_writer = csv.DictWriter(addr_csv, fieldnames = ["address", "balance", "txns"])
    addr_writer.writeheader()

    with open('transactions.csv', 'r') as txn_obj:
        # pass the file object to DictReader() to get the DictReader object
        txn_reader = DictReader(txn_obj)
        # iterate over each line as a ordered dictionary
        i = 0
        for row in txn_reader:
            # row variable is a dictionary that represents a row in csv
            print(row['from_address'], row['to_address'])
            addr_writer.writerow({'address': row['from_address'], 'balance': i })
            i = i + 1