

"""
This is a retired interview question of Amazon Bar Raiser interviewer, Carlos Arguelles.
https://carloarg02.medium.com/my-favorite-coding-question-to-give-candidates-17ea4758880c


Let’s say we have a website and we keep track of what pages customers are viewing, for things like business metrics.
Every time somebody comes to the website, we write a record to a log file consisting of
    Timestamp
    PageId
    CustomerId
At the end of the day we have a big log file with many entries in that format.
And for every day we have a new file.
Now, given two log files (log file from day 1 and log file from day 2)

We want to generate a list of ‘loyal customers’ that meet the criteria of:
    (a) they came on both days, and
    (b) they visited at least two unique pages.

Specification is incomplete, clarifying questions are required:
Q1: Did you mean 2 unique pages per day or overall?
A1: 2 unique pages overall

Q2: What is the scale? Does data fit in memory (in both files, one file or none of them)?
A2: The contents of both files fit into memory

Optimize at the end!!!

"""

from csv import reader


def read_csv_as_customer_dict(file_path: str) -> dict:
    customer_dict = dict()
    with open(file_path) as csv_file:
        csv_reader = reader(csv_file, delimiter=',')
        for row in csv_reader:
            row_as_list = list(row)
            customer_id = row_as_list[-1]
            customer_dict[customer_id] = customer_dict.get(customer_id, set()).union({row_as_list[-2]})
    return customer_dict


def find_loyal_customer(threshold: int, customer_dict_1: dict, customer_dict_2: dict) -> list:
    loyal_customers = list()
    for customer_id, page_ids in customer_dict_2.items():
        try:
            page_ids_all = page_ids.union(customer_dict_1[customer_id])
        except KeyError:
            continue
        if threshold <= len(page_ids_all):
            loyal_customers.append(customer_id)
    return loyal_customers
