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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import string
#
# import pandas as pd
#
#
# def get_and_clean_data():
#     data = pd.read_csv('software_developer_united_states_1971_20191023_1.csv')
#     description = data['job_description']
#     cleaned_description = description.apply(lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
#     cleaned_description = cleaned_description.apply(lambda s: s.lower())
#     cleaned_description = cleaned_description.apply(lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))
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
