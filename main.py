# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')
# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import string
import pandas as pd
import requests as requests
from bs4 import BeautifulSoup
import numpy as np


# def get_and_clean_data():
#     data = pd.read_csv('test4.csv')
#     description = data['job_description']
#     cleaned_description = description.apply(lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
#     cleaned_description = cleaned_description.apply(lambda s: s.lower())
#     cleaned_description = cleaned_description.apply(
#         lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))
#     cleaned_description = cleaned_description.drop_duplicates()
#     return cleaned_description
#
#
# def simple_tokenize(data):
#     cleaned_description = data.apply(lambda s: [x.strip() for x in s.split()])
#     return cleaned_description
#
#
# def parse_job_description():
#     cleaned_description = get_and_clean_data()
#     cleaned_description = simple_tokenize(cleaned_description)
#     return cleaned_description
#
#
# def count_python_mysql():
#     parsed_description = parse_job_description()
#     count_python = parsed_description.apply(lambda s: 'python' in s).sum()
#     count_mysql = parsed_description.apply(lambda s: 'mysql' in s).sum()
#     print('python: ' + str(count_python) + ' of ' + str(parsed_description.shape[0]))
#     print('mysql: ' + str(count_mysql) + ' of ' + str(parsed_description.shape[0]))
#
#
# def parse_db():
#     html_doc = requests.get("https://db-engines.com/en/ranking").content
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     db_table = soup.find("table", {"class": "dbi"})
#     all_db = [''.join(s.find('a').findAll(text=True, recursive=False)).strip() for s in db_table.findAll("th", {"class": "pad-l"})]
#     all_db = list(dict.fromkeys(all_db))
#     db_list = all_db[:10]
#     db_list = [s.lower() for s in db_list]
#     db_list = [[x.strip() for x in s.split()] for s in db_list]
#     # output: [['oracle'], ['mysql'], ['microsoft', 'sql', 'server'], ['postgresql'], ['mongodb'], ['redis'], ['ibm', 'db2'],
#     #  ['elasticsearch'], ['sqlite'], ['cassandra']]
#     return db_list
#
#
#
#
# def get_list_of_db():
#     parsed_description = parse_job_description()
#     cleaned_db = parse_db()
#     raw = [None] * len(cleaned_db)
#     for i, db in enumerate(cleaned_db):
#         raw[i] = parsed_description.apply(lambda s: np.all([x in s for x in db])).sum()
#         print(' '.join(db) + ': ' + str(raw[i]) + ' of ' + str(parsed_description.shape[0]))



# def counts_java():
#     parsed_description = parse_job_description()
#     count_java = parsed_description.apply(lambda s: 'oracle' in s).sum()
#     count_mysql = parsed_description.apply(lambda s: 'mysql' in s).sum()
#     print('oracle: ' + str(count_java) + ' of ' + str(parsed_description.shape[0]))
#     print('mysql: ' + str(count_mysql) + ' of ' + str(parsed_description.shape[0]))

import string
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests as requests


def get_and_clean_data():
    data = pd.read_csv('test4.csv')
    description = data['job_description']
    cleaned_description = description.apply(lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
    cleaned_description = cleaned_description.apply(lambda s: s.lower())
    cleaned_description = cleaned_description.apply(
        lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))
    cleaned_description = cleaned_description.drop_duplicates()
    return cleaned_description


def simple_tokenize(data):
    cleaned_description = data.apply(lambda s: [x.strip() for x in s.split()])
    return cleaned_description


def parse_job_description():
    cleaned_description = get_and_clean_data()
    cleaned_description = simple_tokenize(cleaned_description)
    return cleaned_description


def count_python_mysql():
    parsed_description = parse_job_description()
    count_python = parsed_description.apply(lambda s: 'python' in s).sum()
    count_mysql = parsed_description.apply(lambda s: 'mysql' in s).sum()
    print('python: ' + str(count_python) + ' of ' + str(parsed_description.shape[0]))
    print('mysql: ' + str(count_mysql) + ' of ' + str(parsed_description.shape[0]))


def parse_db():
    html_doc = requests.get("https://db-engines.com/en/ranking").content
    soup = BeautifulSoup(html_doc, 'html.parser')
    db_table = soup.find("table", {"class": "dbi"})
    all_db = [''.join(s.find('a').findAll(text=True, recursive=False)).strip() for s in
              db_table.findAll("th", {"class": "pad-l"})]
    all_db = list(dict.fromkeys(all_db))
    db_list = all_db[:10]
    # db_list = [s.lower() for s in all_db]
    db_list = [s.lower() for s in db_list]
    db_list = [[x.strip() for x in s.split()] for s in db_list]
    return db_list


def get_list_of_db():
    parsed_description = parse_job_description()
    cleaned_db = parse_db()
    ##############################Alongside python###############################
    lang = [['java'], ['python'], ['c'], ['kotlin'], ['swift'], ['rust'], ['ruby'], ['scala'], ['julia'], ['lua']]
    rawpy = [None] * len(lang)
    for i, db in enumerate(lang):
        rawpy[i] = parsed_description.apply(lambda s: np.all([x in s for x in db])).sum()
        # print( str(rawpy[i]) + ' of ' + str(parsed_description.shape[0]))

    n = len(rawpy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if rawpy[j] < rawpy[j + 1]:
                rawpy[j], rawpy[j + 1] = rawpy[j + 1], rawpy[j]
    for i, db in enumerate(lang):
        print(' '.join(db) + ': ' + str(rawpy[i]) + ' of ' + str(parsed_description.shape[0]))

    all_terms = lang
    query_map = pd.DataFrame(parsed_description.apply
                             (lambda s: [1 if np.all([d in s for d in db]) else 0 for db in all_terms])
                             .values.tolist(), columns=[' '.join(d) for d in all_terms])
    #############################################################################



    ##############################Alongside Oracle###############################
    raw = [None] * len(cleaned_db)
    for i, db in enumerate(cleaned_db):
        raw[i] = parsed_description.apply(lambda s: np.all([x in s for x in db])).sum()
        # print(' '.join(db) + ': ' + str(raw[i]) + ' of ' + str(parsed_description.shape[0]))
    n = len(raw)
    for i in range(n):
        for j in range(0, n - i - 1):
            if raw[j] < raw[j + 1]:
                raw[j], raw[j + 1] = raw[j + 1], raw[j]

    for i, db in enumerate(cleaned_db):
        print(' '.join(db) + ': ' + str(raw[i]) + ' of ' + str(parsed_description.shape[0]))
    ##############################################################
    # with_python = [None] * len(cleaned_db)
    # for i, db in enumerate(cleaned_db):
    #     with_python[i] = parsed_description.apply(lambda s: np.all([x in s for x in db]) and 'python' in s).sum()
    #     print(' '.join(db) + ' + python: ' + str(with_python[i]) + ' of ' + str(parsed_description.shape[0]))
    #
    # for i, db in enumerate(cleaned_db):
    #     print(' '.join(db) + ' + python: ' + str(with_python[i]) + ' of ' + str(raw[i]) + ' (' + str(
    #         np.around(with_python[i] / raw[i] * 100, 2)) + '%)')

# prepare data for java and DB
    with_java = [None] * len(cleaned_db)
    for i, db in enumerate(cleaned_db):
        with_java[i] = parsed_description.apply(lambda s: np.all([x in s for x in db]) and 'java' in s).sum()
        print(' '.join(db) + ' + java: ' + str(with_java[i]) + ' of ' + str(parsed_description.shape[0]))

    for i, db in enumerate(cleaned_db):
        print(' '.join(db) + ' + java: ' + str(with_java[i]) + ' of ' + str(raw[i]) + ' (' + str(
            np.around(with_java[i] / raw[i] * 100, 2)) + '%)')




def create_index():
    lang = [['java'], ['python'], ['c'], ['kotlin'], ['swift'], ['rust'], ['ruby'], ['scala'], ['julia'],['lua']]
    parsed_description = parse_job_description()
    parsed_db = parse_db()
    all_terms = lang + parsed_db
    query_map = pd.DataFrame(parsed_description.apply
                             (lambda s: [1 if np.all([d in s for d in db])else 0 for db in all_terms])
                             .values.tolist(), columns=[' '.join(d) for d in all_terms])

    query_map[query_map['java'] > 0].apply(lambda s: np.where(s == 1)[0], axis=1).apply(lambda s: list(query_map.columns[s]))
