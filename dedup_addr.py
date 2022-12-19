import sys
import csv
from csv import DictReader

csv.field_size_limit(sys.maxsize)

# open file in read mode
with open('addresses.csv', 'r') as read_obj, open('addresses_dedup.csv', 'w') as write_obj:
    # pass the file object to DictReader() to get the DictReader object
    reader = DictReader(read_obj)
    seen = set() # set for fast O(1) amortized lookup

    addr_writer = csv.DictWriter(write_obj, fieldnames = ["address", "balance", "txns"])
    addr_writer.writeheader()

    # iterate over each line as a ordered dictionary
    for row in reader:
        if row['address'] in seen: continue
        seen.add(row['address'])
        addr_writer.writerow(row)