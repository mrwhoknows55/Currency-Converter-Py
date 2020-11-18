import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import data

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas

SMALL_FONT = ("Fira Sans", 12)
MID_FONT = ("Fira Sans", 19)
LARGE_FONT = ("Fira Sans", 32)


class CurrencyApp(ThemedTk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        ThemedTk.__init__(self, *args, **kwargs)
        self.set_theme("breeze")
        self.minsize(600, 600)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

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

        label_from = ttk.Label(self, text="From:", padding=10, font="Helvetica 14 normal")
        menu_from = ttk.OptionMenu(self, self.currency_from, *self.currencyList)
        self.currency_from.set(self.currencyList[15])
        label_from.grid(row=1, column=0, sticky=tk.E, padx=40, pady=5)
        menu_from.grid(row=1, column=1, stick=tk.W, ipady=3, ipadx=7)

        label_amount_1 = ttk.Label(self, text="Amount", padding=10, font="Helvetica 14 normal")
        entry_amount = ttk.Entry(self, textvariable=self.entry_amount, font="Helvetica 14 normal")
        label_amount_1.grid(sticky=tk.E, padx=40, pady=5)
        entry_amount.grid(row=2, column=1, stick=tk.W, ipady=3, ipadx=7)

        label_to = ttk.Label(self, text="To:", padding=10, font=("bold", 12,))
        menu_to = ttk.OptionMenu(self, self.currency_to, *self.currencyList)
        self.currency_to.set(self.currencyList[31])
        label_to.grid(sticky=tk.E, padx=40, pady=5)
        menu_to.grid(row=3, column=1, sticky=tk.W, ipady=3, ipadx=7)

        label_amount_2 = ttk.Label(self, text="Amount", padding=10, font="Helvetica 14 normal")
        label_amount_2.grid(row=4, column=0, sticky=tk.E, padx=40, pady=5)

        label_final_amount = ttk.Entry(self, textvariable=self.final_amount, font=("bold", 12,))
        label_final_amount.grid(row=4, column=1, sticky=tk.W, pady=15, ipady=7)

        button_convert = ttk.Button(self, text="Convert", command=self.convert_clicked)
        button_convert.grid(column=1, sticky=tk.W, pady=20, ipady=3, ipadx=7)

        # Nav Button
        button_goto_history = ttk.Button(self, text="History", command=lambda: controller.show_frame(History))
        button_goto_history.grid(column=1, sticky=tk.W, pady=20, ipady=3, ipadx=7)


class History(tk.Frame):

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

        menu_base_currencies = ttk.OptionMenu(self, self.currency_base, *self.currencyList)
        self.currency_base.set(self.currencyList[15])
        menu_base_currencies.pack(ipady=3, ipadx=7, pady=10)

        label_vs = ttk.Label(self, text="VS")
        label_vs.pack()

        menu_to_currencies = ttk.OptionMenu(self, self.currency_to, *self.currencyList)
        self.currency_to.set(self.currencyList[31])
        menu_to_currencies.pack(pady=10, ipady=3, ipadx=7)

        # analyze data and plt
        sampleData = pandas.read_csv('historical_data.csv')
        fig = Figure(figsize=(15, 6), dpi=100)
        fig.autofmt_xdate(rotation=45)

        plt = fig.add_subplot(111)
        plt.clear()

        # TODO: add it to fun params
        base_sym = "USD"
        to_sym = "INR"
        title = "1 " + base_sym + " to " + to_sym
        plt.set_title(title)
        plt.plot_date(sampleData.date, sampleData.get(to_sym), '-', label=to_sym)
        plt.grid(True)

        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0), loc=3, ncol=2, borderaxespad=0.5)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=15, pady=15)

        toolbar = NavigationToolbar2Tk(canvas, self)

        button_goto_home = ttk.Button(self, text="Home", command=lambda: controller.show_frame(HomePage))
        button_goto_home.pack(pady=20, ipady=3, ipadx=7)


# Driver Code
app = CurrencyApp()
app.mainloop()
