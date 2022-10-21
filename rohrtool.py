from tkinter import Tk, Label, Entry, Button, messagebox, OptionMenu, StringVar, END

class rohrtool:
    def __init__(self, master):
        self.master = master

        # initiate labels
        self.i_rohr_l = Label(width=30, text="Innenrohr Aussendurchmesser [mm]", anchor='w').grid(row=0, column=0)
        self.a_rohr_l = Label(width=30, text="Aussenrohr Innendurchmesser [mm]", anchor='w').grid(row=1, column=0)
        self.rohrlaenge_l = Label(width=30, text="Rohrlänge [m]", anchor='w').grid(row=2, column=0)
        self.reserve_l = Label(width=30, text="Reserve [%]", anchor='w').grid(row=3, column=0)
        self.dichte_l = Label(width=30, text="spez. Dichte [kg * m⁻³]", anchor='w').grid(row=4, column=0)

        self.volumen_l = Label(width=30, text="Volumen [m³]", anchor='w').grid(row=6, column=0)
        self.gewicht_l = Label(width=30, text="Volumen [kg]", anchor='w').grid(row=7, column=0)
        self.saecke_l = Label(width=30, text="Anzahl Sandsäcke à 25 kg", anchor='w').grid(row=8, column=0)

        # Drop down menues
        self.OptionList_i_rohr = {'RC70': 70, 'RC85': 85}
        self.variable_i_rohr = StringVar(root, value='RC70')
        self.opt_i_rohr = OptionMenu(root, self.variable_i_rohr, *self.OptionList_i_rohr.keys(), command=self.option_change())
        self.opt_i_rohr.config(width=20, font=('Helvetica', 10))
        self.opt_i_rohr.grid(row=0, column=2)

        self.OptionList_a_rohr = [110]
        self.variable_a_rohr = StringVar(root)
        self.opt_a_rohr = OptionMenu(root, self.variable_a_rohr, *self.OptionList_a_rohr)
        self.opt_a_rohr.config(width=20, font=('Helvetica', 10))
        self.opt_a_rohr.grid(row=1, column=2)

        self.OptionList_reserve = [10, 20]
        self.variable_reserve = StringVar(root)
        self.opt_reserve = OptionMenu(root, self.variable_reserve, *self.OptionList_reserve)
        self.opt_reserve.config(width=20, font=('Helvetica', 10))
        self.opt_reserve.grid(row=3, column=2)

        self.OptionList_dichte = [1700]
        self.variable_dichte = StringVar(root)
        self.opt_dichte = OptionMenu(root, self.variable_dichte, *self.OptionList_dichte)
        self.opt_dichte.config(width=20, font=('Helvetica', 10))
        self.opt_dichte.grid(row=4, column=2)

        # initiate entry boxes
        self.i_rohr_entry = Entry(root, width=10, textvariable=self.variable_i_rohr)
        self.i_rohr_entry.grid(row=0, column=1)

        self.a_rohr_entry = Entry(width=10, textvariable=self.variable_a_rohr)
        self.a_rohr_entry.grid(row=1, column=1)

        self.rohrlaenge_entry = Entry(width=10)
        self.rohrlaenge_entry.grid(row=2, column=1)

        self.reserve_entry = Entry(width=10, textvariable=self.variable_reserve)
        self.reserve_entry.grid(row=3, column=1)

        self.dichte_entry = Entry(width=10, textvariable=self.variable_dichte)
        self.dichte_entry.grid(row=4, column=1)

        # create button for calculation
        self.calculate_button = Button(text="Berechnen", command=self.calculater).grid(row=5, column=1)

    def option_change(self):
        input_var = self.OptionList_i_rohr[self.variable_i_rohr.get()]
        self.i_rohr_entry = Entry(root, width=10)
        self.i_rohr_entry.delete(0, END)
        self.i_rohr_entry.insert(0, input_var)

    def calculater(self):
        try:
            i = float(self.i_rohr_entry.get())
            a = float(self.a_rohr_entry.get())
            la = float(self.rohrlaenge_entry.get())
            reserve = float(self.reserve_entry.get())
            dichte = float(self.dichte_entry.get())
        except:
            messagebox.showinfo("Error!", "Die Eingaben müssen Zahlen sein")

        vol = round(((a / 2 / 1000) ** 2 * 3.14159 * la - (i / 2 / 1000) ** 2 * 3.14159 * la) * (1 + reserve / 100), 2)
        gew = round((vol * dichte), 2)
        saecke = gew/25

        Label(width=10, text=vol).grid(row=6, column=1)
        Label(width=10, text=gew).grid(row=7, column=1)
        Label(width=10, text=saecke).grid(row=8, column=1)


root = Tk()
rohrtool(root)
root.geometry("700x300")
root.mainloop()
