from tkinter import Tk, Label, Entry, Button, messagebox

class rohrtool:
    def __init__(self, master):
        self.master = master

        #initiate labels
        self.i_rohr_l = Label(width=30, text="Innenrohr Aussendurchmesser [mm]", anchor='w').grid(row=0, column=0)
        self.a_rohr_l = Label(width=30, text="Aussenrohr Innendurchmesser [mm]", anchor='w').grid(row=1, column=0)
        self.rohrlaenge_l = Label(width=30, text="Rohrlänge [m]", anchor='w').grid(row=2, column=0)
        self.reserve_l = Label(width=30, text="Reserve [%]", anchor='w').grid(row=3, column=0)
        self.dichte_l = Label(width=30, text="Dichte [kg * m⁻³]", anchor='w').grid(row=4, column=0)

        self.volumen_l = Label(width=30, text="Volumen [m³]", anchor='w').grid(row=6, column=0)
        self.gewicht_l = Label(width=30, text="Volumen [kg]", anchor='w').grid(row=7, column=0)

        #initiate entry boxes
        self.i_rohr_entry = Entry(width=10)
        self.i_rohr_entry.grid(row=0, column=1)
        
        self.a_rohr_entry = Entry(width=10)
        self.a_rohr_entry.grid(row=1, column=1)
        
        self.rohrlaenge_entry = Entry(width=10)
        self.rohrlaenge_entry.grid(row=2, column=1)
        
        self.reserve_entry = Entry(width=10)
        self.reserve_entry.grid(row=3, column=1)
        
        self.dichte_entry = Entry(width=10)
        self.dichte_entry.grid(row=4, column=1)

        #create button for calculation
        self.calculate_button = Button(text="Berechnen", command=self.calculater).grid(row=5, column=1)

    def calculater(self):
        try:
            i = float(self.i_rohr_entry.get())
            a = float(self.a_rohr_entry.get())
            l = float(self.rohrlaenge_entry.get())
            reserve = float(self.reserve_entry.get())
            dichte = float(self.dichte_entry.get())
        except:
            messagebox.showinfo("Error!", "Die Eingaben müssen Zahlen sein")
        
        vol = round(((a/2/1000)**2*3.14159*l - (i/2/1000)**2*3.14159*l) * (1+reserve/100),2)
        gew = round((vol*dichte),2)

        Label(width=10, text=vol).grid(row=6, column=1)
        Label(width=10, text=gew).grid(row=7, column=1)

root = Tk()
rohrtool(root)
root.geometry("500x200")
root.mainloop()