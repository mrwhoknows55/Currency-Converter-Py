from tkinter import *
from tkinter import ttk, messagebox, font
from ttkthemes import ThemedTk
from urllib3.exceptions import MaxRetryError, NewConnectionError

import data

root = ThemedTk(theme="breeze")
root.title("Currency Converter")
root.geometry("500x500")
ttk.Label(root, text="").grid(pady=10)

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

label_from = ttk.Label(root, text="From:", padding=10, font="Helvetica 14 normal")
menu_from = ttk.OptionMenu(root, currency_from, *currencyList)
currency_from.set(currencyList[15])
label_from.grid(sticky=E, padx=40, pady=5)
menu_from.grid(row=1, column=1, stick=W, ipady=3, ipadx=7)

label_amount_1 = ttk.Label(root, text="Amount", padding=10, font="Helvetica 14 normal")
entry_amount = ttk.Entry(root, font="Helvetica 14 normal")
label_amount_1.grid(sticky=E, padx=40, pady=5)
entry_amount.grid(row=2, column=1, stick=W, ipady=3, ipadx=7)

label_to = ttk.Label(root, text="To:", padding=10, font=("bold", 12,))
menu_to = ttk.OptionMenu(root, currency_to, *currencyList)
currency_to.set(currencyList[31])
label_to.grid(sticky=E, padx=40, pady=5)
menu_to.grid(row=3, column=1, sticky=W, ipady=3, ipadx=7)


def convert_clicked():
    base = currency_from.get()[0:3]
    sec = currency_to.get()[0:3]
    try:
        amount = float(entry_amount.get())
    except ValueError:
        print("Invalid Amount Entered")
        messagebox.showerror("Enter Valid Amount", "Please Enter Valid Amount")
        return

    if amount < 0:
        print("Invalid Amount Entered")
        messagebox.showerror("Enter Valid Amount", "Amount Should Be Greater Than Zero")

    else:
        converted_amount = data.print_amount(amount, base, sec)
        print(converted_amount)
        final_amount.set(converted_amount)


label_amount_2 = ttk.Label(root, text="Amount", padding=10, font="Helvetica 14 normal")
label_amount_2.grid(row=4, column=0, sticky=E, padx=40, pady=5)

final_amount = StringVar()
label_final_amount = ttk.Entry(root, textvariable=final_amount, font=("bold", 12,))
label_final_amount.grid(row=4, column=1, sticky=W, pady=15, ipady=7)

button_convert = ttk.Button(root, text="Convert", command=convert_clicked)
button_convert.grid(column=1, sticky=W, pady=20, ipady=3, ipadx=7)

root.mainloop()
