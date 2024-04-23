import tkinter as tk
from datetime import datetime
import csv
import os
from PIL import Image
import pystray
from pystray import MenuItem as item

class PontoEletronico:
    def __init__(self, master):
        self.master = master
        self.master.title("Ponto Eletrônico")
        self.master.geometry("300x200")

        self.entrada_btn = tk.Button(master, text="Entrada", command=self.registrar_entrada)
        self.entrada_btn.pack(pady=20)

        self.saida_btn = tk.Button(master, text="Saída", command=self.registrar_saida)
        self.saida_btn.pack(pady=20)
        self.saida_btn.pack_forget()

        self.timer_label = tk.Label(master, text="00:00:00")
        self.timer_label.pack(pady=20)
        self.timer_label.pack_forget()

        self.entrada_time = None
        self.timer_id = None

    def registrar_entrada(self):
        self.entrada_time = datetime.now()
        self.update_csv('entrada')
        self.entrada_btn.pack_forget()
        self.saida_btn.pack()
        self.timer_label.pack()
        self.update_timer()

    def registrar_saida(self):
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
        self.update_csv('saida')
        self.quit_application()

    def update_csv(self, action):
        filename = "dataset_ponto.csv"
        dia_semana = datetime.now().strftime("%A, %d/%m/%Y")
        hora_atual = datetime.now().strftime("%H:%M:%S")

        file_exists = os.path.isfile(filename)
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = ['Dia', 'Entrada', 'Saída']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            if action == 'entrada':
                writer.writerow({'Dia': dia_semana, 'Entrada': hora_atual, 'Saída': ''})
            elif action == 'saida':
                lines = []
                with open(filename, 'r') as readfile:
                    reader = csv.reader(readfile)
                    for row in reader:
                        lines.append(row)
                    if len(lines) > 1:
                        lines[-1][2] = hora_atual

                with open(filename, 'w', newline='') as writefile:
                    writer = csv.writer(writefile)
                    writer.writerows(lines)

    def update_timer(self):
        if self.entrada_time:
            elapsed = datetime.now() - self.entrada_time
            self.timer_label.config(text=str(elapsed).split('.')[0])
        self.timer_id = self.master.after(1000, self.update_timer)

    def quit_application(self):
        self.master.quit()
        self.master.destroy()

    def hide_window(self):
        self.master.withdraw()
        icon = pystray.Icon("Ponto Eletrônico", Image.open("icon.png"), "Ponto Eletrônico", self.menu())
        icon.run()

    def menu(self):
        return (item('Show', self.show_window), item('Quit', self.quit_application))

    def show_window(self, icon, item):
        icon.stop()
        self.master.after(0, self.master.deiconify)

if __name__ == "__main__":
    root = tk.Tk()
    app = PontoEletronico(root)
    root.protocol("WM_DELETE_WINDOW", app.hide_window)
    root.mainloop()
