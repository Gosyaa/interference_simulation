from tkinter import *
from Physics import *
from math import pi, cos

class Line(Canvas):
    def __init__(self):
        super().__init__(window, width=100, height=200, bg='white')
        self.place(x=950, y=200)
    def add_line(self, x, color):
        self.create_rectangle((0, x), (100, x + 1), fill=color, outline=color)
    def create_picture(self, d, L, wavelength=700):
        self.cur_L = float(L) * 0.001
        self.cur_d = float(d) * 0.01 * 0.001
        self.cur_wavelength = int(wavelength)
        self.delete('all')
        k = 2 * pi / (self.cur_wavelength * 0.000000001)
        for i in range (-100, 100):
            intencity = cos(0.5 * k * OPD((i + 0.5) * 0.0001, self.cur_d, self.cur_L))**2
            self.add_line((i + 100), rgb_to_hex(wavelength_to_rgb(self.cur_wavelength), intencity))

class WaveFront(Canvas):
    def __init__(self, d=12, L=500, wavelength=700):
        super().__init__(window, width=900, height=500, bg='white')
        self.place(x=50, y=50)
        color = rgb_to_hex(wavelength_to_rgb(wavelength))
        self.original_source = self.create_oval(
            (5, 245),
            (15, 255), 
            fill=color
        )
        original_front = self.create_wavefront(10, 250, 150)
        self.create_line((150, 0), (150, 500))
        self.cur_d = d * 100 * 5
        self.source1 = self.create_oval(
            (145, 245 - self.cur_d),
            (155, 255 - self.cur_d),
            fill=color
        )
        self.source2 = self.create_oval(
            (145, 245 + self.cur_d),
            (155, 255 + self.cur_d),
            fill=color
        )
        self.wave1 = self.create_wavefront(150, 250 - self.cur_d, 350 + 500)
        self.wave2 = self.create_wavefront(150, 250 + self.cur_d, 350 + 500)
        self.screen = self.create_line((350 + 500, 0), (350 + 500, 500))
        
    def create_wavefront(self, x_start, y_start, x_finish):
        front = []
        cur = 25
        while x_start + cur + 10 < x_finish:
            front.append(self.create_arc(
                (x_start - cur, y_start - cur),
                (x_start + cur, y_start + cur),
                style=ARC,
                start=300,
                extent=120
            ))
            cur += 25
        return front
    def delete_wavefront(self, wave):
        for cur in wave:
            self.delete(cur)
    
    def update_secondary_sources(self, d, L, wavelength):
        color = rgb_to_hex(wavelength_to_rgb(wavelength))
        self.delete(self.source1)
        self.delete(self.source2)
        self.delete_wavefront(self.wave1)
        self.delete_wavefront(self.wave2)
        self.delete(self.screen)
        self.cur_L = int(L)
        self.cur_d = int(d) * 5
        self.original_source = self.create_oval(
            (5, 245),
            (15, 255), 
            fill=color
        )
        self.source1 = self.create_oval(
            (145, 245 - self.cur_d),
            (155, 255 - self.cur_d),
            fill=color
        )
        self.source2 = self.create_oval(
            (145, 245 + self.cur_d),
            (155, 255 + self.cur_d),
            fill=color
        )
        self.wave1 = self.create_wavefront(150, 250 - self.cur_d, 350 + self.cur_L)
        self.wave2 = self.create_wavefront(150, 250 + self.cur_d, 350 + self.cur_L)
        self.screen = self.create_line((350 + self.cur_L, 0), (350 + self.cur_L, 500))

class Cur_Vars(Label):
    def __init__(self):
        s = 'L = 100мм\nd=0.05мм\nλ=380нм' 
        super().__init__(window, text=s)
        self.place(x=50, y=550)
    def upd(self, new_L, new_d, new_w):
        s = 'L = ' + str(new_L) + 'мм\n' + 'd = ' + str(new_d / 100) + 'мм\n' + 'λ = ' + str(new_w) + 'нм'
        self.config(text=s)

def change(newVal):
    test.update_secondary_sources(scale_d.get(), scale_L.get(), scale_wavelength.get())
    Interference.create_picture(scale_d.get(), scale_L.get(), scale_wavelength.get())
    display.upd(scale_L.get(), scale_d.get(), scale_wavelength.get())

window = Tk()
window.geometry('1066x600')
window.resizable(False, False)

Interference = Line()
test = WaveFront()

scale_wavelength = Scale(window, orient=HORIZONTAL,
                        length=200, from_=380, to=780, 
                        command=change
                        )
scale_d = Scale(window, orient=HORIZONTAL,
                length=200, from_=5, to=30,
                command=change
                )
scale_L = Scale(window, orient=HORIZONTAL,
                length=200, from_=100, to=500,
                command=change)

test.update_secondary_sources(scale_d.get(), scale_L.get(), scale_wavelength.get())
Interference.create_picture(5, 100, 380)

scale_d.pack()
scale_wavelength.place(x=700, y=0)
scale_L.place(x=100, y=0)
display = Cur_Vars()

window.mainloop()