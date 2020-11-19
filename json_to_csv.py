import json
import csv
from datetime import datetime

import requests
from operator import itemgetter


def conv_to_csv(rates, base_sym, to_sym):
    main_json = {"rates": []}

    for (key, value) in rates.items():
        json_obj = {"date": key, base_sym: value[base_sym], to_sym: value[to_sym]}
        main_json["rates"].append(json_obj)

    json_array = json.dumps(main_json)
    data_json = json.loads(json_array)
    print(type(data_json))

    new_rates = data_json['rates']

    data_file = open('historical_data.csv', 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for rate in new_rates:
        if count == 0:
            count += 1
        # Writing data of CSV file
        csv_writer.writerow(rate.values())
    data_file.close()
    conv_dates(base_sym, to_sym)


def conv_dates(base_sym, to_sym):
    main_json_obj = {"rates": []}

    # sort dates (yyyy-mm-dd)
    read_file = open('historical_data.csv', 'r')
    with read_file as csv_file:
        old_data = [line for line in csv.reader(csv_file)]
        old_data.sort(key=itemgetter(0))
    csv_file.close()

    # write sorted dates to csv (yyyy-mm-dd)
    write_file = open('historical_data.csv', 'w')
    with write_file as csv_file:
        csv.writer(csv_file).writerow(['date', base_sym, to_sym])
        csv.writer(csv_file).writerows(old_data)
    csv_file.close()

    read_file = open('historical_data.csv', 'r')
    with read_file as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for lines in csv_reader:
            new_date = datetime.strptime(lines['date'], "%Y-%m-%d").strftime("%d\n%b")
            json_obj = {"date": new_date, base_sym: lines[base_sym], to_sym: lines[to_sym]}
            main_json_obj["rates"].append(json_obj)
    csv_file.close()

    # write sorted dates to csv (dd\nMonth)
    data_file = open('historical_data.csv', 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for rate in main_json_obj["rates"]:
        if count == 0:
            csv_writer.writerow(['date', base_sym, to_sym])
            count += 1
        # Writing data of CSV file
        csv_writer.writerow(rate.values())
    data_file.close()


# dates in yyy-mm-dd format (string)
def main(base_sym, to_sym, from_date, to_date):
    print("Requesting")
    url = 'https://api.exchangeratesapi.io/history?start_at=' + from_date + '&end_at=' + to_date \
          + '&symbols=' + base_sym + "," + to_sym + "&base=" + base_sym
    history_data_req = requests.get(url)
    print(url)

    if history_data_req.ok:
        jsondata = json.dumps(history_data_req.json())
        data = json.loads(jsondata)
        conv_to_csv(data.get('rates'), base_sym, to_sym)
        print("Done!")
    else:
        print("Error")


if __name__ == '__main__':
    base_sym = "MYR"
    to_sym = "INR"
    main(base_sym, to_sym, '2020-10-01', '2020-11-02')
