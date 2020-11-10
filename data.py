import json

import requests


def getdata(base, sec, con_amount):
    latestReq = requests.get("https://api.exchangeratesapi.io/latest?base=" + base + "&symbols=" + base + "," + sec)

    if latestReq.ok:
        data = json.dumps(latestReq.json())
        rates = json.loads(data).get('rates')
        print(data)
        convRate = float(rates[sec])
        print(convRate)
        return float(convRate * con_amount)
    else:
        print(latestReq.text)
        print("Something Went Wrong")
        return -1.0


def print_amount(amount, base_currency, to_currency):
    if amount < 0:
        print("Invalid amount")
        return "Invalid amount"
    else:
        final_amount = getdata(base_currency, to_currency, amount)
        if final_amount < 0:
            return "Something Went Wrong, Please Try After Some Time!"
        else:
            return str(final_amount)
