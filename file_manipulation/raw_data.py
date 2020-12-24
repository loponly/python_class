# open reader

import csv
from pprint import pprint


class File():

    def __init__(self):
        self.file_path = 'file_manipulation/file.csv'

    def file_copy(self):
        pass

    def file_edit(self, file_path='file_manipulation/file.csv', edit='2020-02-10'):

        print('working')
        data = list()

        with open(file_path, 'r') as f:  # openning file f = open(file_path, 'r')
            raw_data = f.read().split('\n')  # retunrs as string and list array

            header = raw_data[0].split(',')

            for row in raw_data[1:]:

                new_row = dict()

                for column_name, value in zip(header, row.split(',')):
                    new_row[column_name] = value

                # for i, value in enumerate(row.split(',')):
                #     new_row[header[i]] = value

                data.append(new_row)

        data[3]['product_id'] = edit

        with open(file_path, 'w') as f:
            f.write(','.join(header)+'\n')  # join returns list as string

            for row in data:
                f.write(','.join(list(row.values()))+'\n')

        return True


if __name__ == "__main__":
    file_manipulation()
