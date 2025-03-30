# Follow @bagusde._ :D

import tkinter as tk
from tkinter import messagebox
import time
import threading

#atur waktu belajar (disini 2 jam)
WAKTU_FOKUS = 25 * 60
WAKTU_ISTIRAHAT = 5 * 60
TOTAL_SESI = 4

class PomodoroTimer:
    def __init__(self, main):
        self.main = main
        self.main.title('Pomodoro Timer')
        self.main.geometry('300x100')
        self.main.attributes('-topmost', True)
        self.main.protocol('WM_DELETE_WINDOW', self.sedang_ditutup)
        self.main.resizable(False, False)

        self.label = tk.Label(main, text='25:00', font=('Poppins 36 bold'))
        self.label.pack(pady=1)

        self.start_button = tk.Button(main, text='Mulai', command=self.start_pomodoro, font=('Poppins', 10), width=10)
        self.start_button.pack(pady=2)

    def start_pomodoro(self):
        self.main.geometry('250x60')
        self.start_button.config(state='disabled')
        self.thread = threading.Thread(target=self.run_sesi_pomodoro)
        self.thread.start()

    def run_timer(self, durasi, pesan_akhir):
        for remaining in range(durasi, 0, -1):
            menit, detik = divmod(remaining, 60)
            time_str = f'{menit:02d}:{detik:02d}'
            self.label.config(text=time_str)
            time.sleep(1)
        messagebox.showinfo('Pomodoro Timer', pesan_akhir)
        self.label.config(text='25:00')

    def run_sesi_pomodoro(self):
        for sesi in range(TOTAL_SESI):
            self.run_timer(WAKTU_FOKUS, f'sesi {sesi + 1} selesai! Istirahat Sejenak')
            if sesi < TOTAL_SESI - 1:
                self.run_timer(WAKTU_ISTIRAHAT, f'Istirahat Selesai! Memulai sesi {sesi + 1}')
        messagebox.showinfo('Pomodoro Timer', 'Semua sesi selesai!')
        self.main.destroy()

    def sedang_ditutup(self):
        if self.start_button['state'] == 'disabled':
            messagebox.showwarning('Pomodoro Timer', 'Lanjutkan Sesi Pembelajaran!')
        else:
            self.main.destroy()


if __name__ == '__main__':
    main = tk.Tk()
    app = PomodoroTimer(main)
    main.mainloop()