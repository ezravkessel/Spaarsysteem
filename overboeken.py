import tkinter as tk

saldo = 1000


def overboeken():
    global saldo
    bedrag = float(invoer.get())
    if bedrag > saldo:
        tekst.config(text="Onvoldoende saldo")
    else:
        saldo = saldo - bedrag
        tekst.config(text=f"Nieuw saldo: {saldo}")


venster = tk.Tk()
tk.Label(venster, text="Bedrag:").pack()
invoer = tk.Entry(venster)
invoer.pack()
tk.Button(venster, text="Overboeken", command=overboeken).pack()
tekst = tk.Label(venster, text=f"Saldo: {saldo}")
tekst.pack()
venster.mainloop()
