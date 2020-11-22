import tkinter as tk
from datetime import date, timedelta
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import data

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas

import json_to_csv

SMALL_FONT = ("Fira Sans", 12)
MID_FONT = ("Fira Sans", 19)
LARGE_FONT = ("Fira Sans", 32)
FONT_NORMAL = ("Roboto", 12)


class CurrencyApp(ThemedTk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        ThemedTk.__init__(self, *args, **kwargs)
        self.set_theme("breeze")
        self.minsize(1050, 720)

        # creating a container
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, History):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

        # to display the current frame passed as

    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):

    def convert_clicked(self):

        base = self.currency_from.get()[0:3]
        sec = self.currency_to.get()[0:3]

        try:
            amount = float(self.entry_amount.get())
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
            self.final_amount.set(converted_amount)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.currencyList = [
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
        self.currency_from = tk.StringVar()
        self.currency_to = tk.StringVar()
        self.final_amount = tk.StringVar()
        self.entry_amount = tk.StringVar()

        label = ttk.Label(self, text="Currency Converter", font=MID_FONT)
        label.grid(row=0, column=1, pady=20)

        label_from = ttk.Label(self, text="From: ", padding=10, font=FONT_NORMAL)
        menu_from = ttk.OptionMenu(self, self.currency_from, *self.currencyList)
        self.currency_from.set(self.currencyList[15])
        label_from.grid(row=1, column=0, sticky=tk.E, padx=40, pady=5)
        menu_from.grid(row=1, column=1, stick=tk.W, ipady=3, ipadx=7)

        label_amount_1 = ttk.Label(self, text="Amount: ", padding=10, font=FONT_NORMAL)
        entry_amount = ttk.Entry(self, textvariable=self.entry_amount, font=FONT_NORMAL)
        label_amount_1.grid(sticky=tk.E, padx=40, pady=5)
        entry_amount.grid(row=2, column=1, stick=tk.W, ipady=3, ipadx=7)

        label_to = ttk.Label(self, text="To: ", padding=10, font=FONT_NORMAL)
        menu_to = ttk.OptionMenu(self, self.currency_to, *self.currencyList)
        self.currency_to.set(self.currencyList[31])
        label_to.grid(sticky=tk.E, padx=40, pady=5)
        menu_to.grid(row=3, column=1, sticky=tk.W, ipady=3, ipadx=7)

        label_amount_2 = ttk.Label(self, text="Amount: ", padding=10, font=FONT_NORMAL)
        label_amount_2.grid(row=4, column=0, sticky=tk.E, padx=40, pady=5)

        label_final_amount = ttk.Entry(self, textvariable=self.final_amount, font=("bold", 12,))
        label_final_amount.grid(row=4, column=1, sticky=tk.W, pady=15, ipady=7)

        button_convert = ttk.Button(self, text="Convert", command=self.convert_clicked)
        button_convert.grid(column=1, sticky=tk.W, pady=20, ipady=3, ipadx=7)

        # Nav Button
        button_goto_history = ttk.Button(self, text="History", command=lambda: controller.show_frame(History))
        button_goto_history.grid(column=1, sticky=tk.W, pady=20, ipady=3, ipadx=7)


class History(tk.Frame):

    def show_graph(self, base_sym, to_sym):
        # analyze data and plt
        sampleData = pandas.read_csv('historical_data.csv')
        fig = Figure(figsize=(10, 5), dpi=100)
        plt = fig.add_subplot(111)

        list_name = self.pack_slaves()
        c = 1
        for item in list_name:
            if c == 4:
                plt.clear()
                item.destroy()
            c += 1

        title = "1 " + base_sym + " VS " + to_sym
        plt.set_title(title)
        plt.plot(sampleData.date, sampleData.get(to_sym), '-', label=to_sym)
        plt.grid(True)

        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0), loc=3, ncol=2, borderaxespad=0.5)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=20, pady=20)

    def get_history_data(self):
        span = str(self.history_span.get())
        current_date = date.today().isoformat()

        if span == 'Week':
            days_before = (date.today() - timedelta(days=7)).isoformat()
        elif span == 'Half Month':
            days_before = (date.today() - timedelta(days=15)).isoformat()
        else:
            days_before = (date.today() - timedelta(days=30)).isoformat()

        # get selected currencies from dropdown menu
        base_sym = self.currency_base.get()[0:3]
        to_sym = self.currency_to.get()[0:3]

        json_to_csv.main(base_sym, to_sym, days_before, current_date)
        self.show_graph(base_sym, to_sym)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="History", font=MID_FONT)
        label.pack(pady=20, anchor=tk.CENTER)

        self.currencyList = [
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
        self.currency_base = tk.StringVar()
        self.currency_to = tk.StringVar()
        self.final_amount = tk.StringVar()
        self.entry_amount = tk.StringVar()
        self.history_span = tk.StringVar()
        self.date_span_list = ['', 'Week', 'Half Month', 'Month']

        menu_frame = tk.Frame(self)
        menu_frame.pack(side=tk.TOP)

        menu_base_currencies = ttk.OptionMenu(menu_frame, self.currency_base, *self.currencyList)
        self.currency_base.set(self.currencyList[31])
        menu_base_currencies.pack(side=tk.LEFT, padx=10, ipady=3, ipadx=7)

        label_vs = ttk.Label(menu_frame, text="VS")
        label_vs.pack(side=tk.LEFT, padx=5)

        menu_to_currencies = ttk.OptionMenu(menu_frame, self.currency_to, *self.currencyList)
        self.currency_to.set(self.currencyList[15])
        menu_to_currencies.pack(side=tk.LEFT, padx=5, ipady=3, ipadx=7)

        menu_history_span = ttk.OptionMenu(menu_frame, self.history_span, *self.date_span_list)
        self.history_span.set(self.date_span_list[1])
        menu_history_span.pack(side=tk.LEFT, fill=tk.X, padx=5, ipady=3, ipadx=7)

        button_get_history = ttk.Button(menu_frame, text="Get History", command=self.get_history_data)
        button_get_history.pack(side=tk.LEFT, fill=tk.X, pady=5, ipady=3, ipadx=7)

        button_goto_home = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
        button_goto_home.pack(ipady=3, ipadx=7, side=tk.BOTTOM)


# Driver Code
app = CurrencyApp()
app.mainloop()
