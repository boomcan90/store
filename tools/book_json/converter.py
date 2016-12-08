import json
from pprint import pprint

with open('book_sample.json') as data_file:
    data = json.load(data_file)


keys = sorted(list(data.keys()))

for k in keys:
    # byear_of_pub = None
    # bnum_of_copies = None
    # bsubject = None
    # bkeywords = None
    # btitle = None
    # bauthor = None
    # bisbn13 = None
    # bformat = None
    # bpublisher = None
    # bprice = None
    b = "sample_list.append(Book(\"{}\", \"{}\", \"{}\", \"{}\", {}, {}, {}, \"{}\", \"{}\", \"{}\"))".format(
        data[k]["isbn13"],
        data[k]["title"],
        data[k]["author"],
        data[k]["publisher"],
        data[k]["year_of_pub"],
        data[k]["num_of_copies"],
        data[k]["price"],
        data[k]["format"],
        data[k]["subject"],
        data[k]["keywords"]
    )

    print(b)
