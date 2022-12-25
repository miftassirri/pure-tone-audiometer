from tkinter import *
import tkinter as tk
from audiometer import controller
from audiometer import audiogram
from tkPDFViewer import tkPDFViewer as pdf

class App(tk.Frame, object):
    def __init__(self, master = None):
        super(App, self).__init__(master)
        self.ctrl = controller.Controller()
        self.click = True

        self.run_button = Button(root, text="BOTH EARS TEST", width=15, height=5, command=self.run)
        self.run_button.pack()

        self.run_button = Button(root, text="RIGHT EAR TEST", width=15, height=5, command=self.run_right)
        self.run_button.pack()

        self.run_button = Button(root, text="LEFT EAR TEST", width=15, height=5, command=self.run_left)
        self.run_button.pack()

    def increment_click(self, level_increment):
        self.current_level += level_increment
        self.click = self.ctrl.clicktone(self.freq, self.current_level, self.earside)

    def hearing_test(self):
        self.current_level = 0
        self.click = self.ctrl.clicktone(self.freq, self.current_level, self.earside)

        while not self.click:
            self.increment_click(self.ctrl.config.small_level_increment)

        current_level_list = []
        current_level_list.append(self.current_level)

    def run(self):
        for self.earside in self.ctrl.config.earsides:
            for self.freq in self.ctrl.config.freqs:
                try:
                    self.hearing_test()
                    self.ctrl.save_results(self.current_level, self.freq, self.earside)

                except OverflowError:
                    print("The signal is distorted. Possible causes are "
                          "an incorrect calibration or a severe hearing "
                          "loss. I'm going to the next frequency.")
                    self.current_level = None
                    continue

        self.ctrl.__exit__()
        audiogram.make_audiogram(self.ctrl.config.filename, self.ctrl.config.results_path)

    def run_right(self):
        for self.earside in self.ctrl.config.right_ear:
            for self.freq in self.ctrl.config.freqs:
                try:
                    self.hearing_test()
                    self.ctrl.save_results(self.current_level, self.freq, self.earside)

                except OverflowError:
                    print("The signal is distorted. Possible causes are "
                          "an incorrect calibration or a severe hearing "
                          "loss. I'm going to the next frequency.")
                    self.current_level = None
                    continue

        self.ctrl.__exit__()
        audiogram.make_audiogram(self.ctrl.config.filename, self.ctrl.config.results_path)

    def run_left(self):
        for self.earside in self.ctrl.config.left_ear:
            for self.freq in self.ctrl.config.freqs:
                try:
                    self.hearing_test()
                    self.ctrl.save_results(self.current_level, self.freq, self.earside)

                except OverflowError:
                    print("The signal is distorted. Possible causes are "
                          "an incorrect calibration or a severe hearing "
                          "loss. I'm going to the next frequency.")
                    self.current_level = None
                    continue

        self.ctrl.__exit__()
        audiogram.make_audiogram(self.ctrl.config.filename, self.ctrl.config.results_path)

    def run(self):
        for self.earside in self.ctrl.config.earsides:
            for self.freq in self.ctrl.config.freqs:
                try:
                    self.hearing_test()
                    self.ctrl.save_results(self.current_level, self.freq, self.earside)

                except OverflowError:
                    print("The signal is distorted. Possible causes are "
                          "an incorrect calibration or a severe hearing "
                          "loss. I'm going to the next frequency.")
                    self.current_level = None
                    continue

        self.ctrl.__exit__()
        audiogram.make_audiogram(self.ctrl.config.filename, self.ctrl.config.results_path)

    def __exit__(self, *args):
        self.ctrl.__exit__()
        audiogram.make_audiogram(self.ctrl.config.filename,
                                 self.ctrl.config.results_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = App()
    app.master.attributes('-fullscreen', True)
    app.master.title("Audiometer")
    app.master.close_button = Button(root, text="QUIT", command = root.destroy)
    app.master.close_button.pack()
    root.mainloop()

    with App() as app:
        app.run()