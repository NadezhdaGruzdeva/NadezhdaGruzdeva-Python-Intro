import csv


with open('csv_example_1.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        print(row, ' - ', type(row))


with open('csv_example_2.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    max_id = 1
    for row in reader:
        # print(type(row))
        if max_id < int(row['id']):
            max_id = int(row['id'])

with open('csv_example_2.csv', 'a', encoding='utf-8') as csvfile:
    field_names = ['id', 'first_name', 'second_name', 'last_name']
    csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)


    csv_writer.writerow({'id': max_id + 1, 'second_name': "Петрович",
                     'first_name': "Петр",
                     'last_name': "Петров"})


