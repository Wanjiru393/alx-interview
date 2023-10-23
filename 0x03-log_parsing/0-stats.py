#!/usr/bin/python3
'''Log parser'''


import sys

words = []

size_list = []

status_dict = {'200': 0, '301': 0, '400': 0,
               '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

sum_size = 0
try:
    for line in sys.stdin:
        words.append(line)
        if len(words) % 10 == 0:
            for i in range(len(words)):
                size_file = words[i]
                file_split = size_file.split(' ')
                file_size = file_split[-1]
                status_code = file_split[-2]
                if status_code in status_dict:
                    status_dict[status_code] += 1
                size_list.append(file_size)
            for sizes in size_list:
                sum_size = sum_size + int(sizes)
            print("File size: {}".format(sum_size))
            for k, v in status_dict.items():
                if status_dict[k] != 0:
                    print("{}: {}".format(k, status_dict[k]))
            status_dict = {'200': 0, '301': 0, '400': 0,
                           '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
except KeyboardInterrupt:
    pass
finally:
    for sizes in size_list:
        sum_size = sum_size + int(sizes)
    print("File size: {}".format(sum_size))
    for k, v in status_dict.items():
        if status_dict[k] != 0:
            print("{}: {}".format(k, status_dict[k]))
