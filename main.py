from tkinter import *

import data

root = Tk()
root.title = "Currency Converter"
root.geometry("400x400")
Label(root, text="").grid(pady=10)

currency_from = StringVar()
currency_to = StringVar()
currencyList = [
    "AUD: Australian Dollar",
    "BGN: Bulgarian Lev",
    "BRL: Brazilian Real",
    "CAD: Canadian Dollar",
    "CHF: Swiss Franc",
    "CNY: Chinese Yuan",
    "CZK: Czech Republic Koruna",
    "DKK: Danish Krone",
    "EUR: Euro",
    "GBP: British Pound Sterling",
    "HKD: Hong Kong Dollar",
    "HRK: Croatian Kuna",
    "HUF: Hungarian Forint",
    "IDR: Indonesian Rupiah",
    "ILS: Israeli New Sheqel",
    "INR: Indian Rupee",
    "ISK: Icelandic Króna",
    "JPY: Japanese Yen",
    "KRW: South Korean Won",
    "MXN: Mexican Peso",
    "MYR: Malaysian Ringgit",
    "NOK: Norwegian Krone",
    "NZD: New Zealand Dollar",
    "PHP: Philippine Peso",
    "PLN: Polish Zloty",
    "RON: Romanian Leu",
    "RUB: Russian Ruble",
    "SEK: Swedish Krona",
    "SGD: Singapore Dollar",
    "THB: Thai Baht",
    "TRY: Turkish Lira",
    "USD: United States Dollar",
    "ZAR: South African Rand"
]

label_from = Label(root, text="From")
menu_from = OptionMenu(root, currency_from, *currencyList)
currency_from.set(currencyList[15])
label_from.grid(sticky=W, padx=25, pady=5)
menu_from.grid(sticky=W, padx=22, ipady=3, ipadx=7)

label_amount = Label(root, text="Amount")
entry_amount = Entry(root, font=("bold", 12,))
label_amount.grid(sticky=W, padx=25, pady=5)
entry_amount.grid(sticky=W, padx=25, ipady=7)

label_to = Label(root, text="To")
menu_to = OptionMenu(root, currency_to, *currencyList)
currency_to.set(currencyList[31])
label_to.grid(sticky=W, padx=25, pady=5)
menu_to.grid(sticky=W, padx=22, ipady=3, ipadx=7)


def convert_clicked():
    base = currency_from.get()[0:3]
    sec = currency_to.get()[0:3]
    amount = float(entry_amount.get())
    if amount < 0:
        print("Invalid Amount Entered")
    else:
        print(data.print_amount(amount, base, sec))


button_convert = Button(root, text="Convert", font=("bold", 12,), command=convert_clicked)
button_convert.grid(sticky=W, padx=25, pady=20, ipady=3, ipadx=7)

root.mainloop()
