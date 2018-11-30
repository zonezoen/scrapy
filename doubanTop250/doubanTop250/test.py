import csv


# with open('data.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     print(headers)
#     old_data = list(f_csv)
#     old_data.append(['abc',123])
#     print(old_data)
#     with open('data.csv', 'w') as f:
#         f_csv = csv.writer(f)
#         f_csv.writerow(headers)
#         f_csv.writerows(old_data)

def appendDta2Csv(file_name, new_headers, new_data):
    with open(file_name) as f:
        f_csv = csv.reader(f)
        try:
            headers = next(f_csv)
        except:
            headers = new_headers
        print(headers)
        old_data = list(f_csv)
        old_data.append(new_data)
        print(old_data)
        with open(file_name, 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(old_data)
            f.close()


appendDta2Csv('data.csv', ["title"],["aaa"])
