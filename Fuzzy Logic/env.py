import tkinter as tk
from math import cos, sin, radians, pi, degrees
from fuzzy.storage.fcl.Reader import Reader
from random import randint

M = 0.4  # kg | mass of the cart
m = 0.2  # kg | mass of the pendulum
b = 0.1  # N/m/sec |  coefficient of friction for cart
l = 0.15  # m | length to pendulum center of mass
I = 0.1  # kg.m^2 | mass moment of inertia of the pendulum
g = 9.8


class Cart:
    def __init__(self, canvas):

        # view
        self.canvas = canvas
        self.last_x = 400
        self.rod_len = 80
        self.rod_y_start = 300-20-30
        rod_y_end = self.rod_y_start - self.rod_len

        self.rect = canvas.create_rectangle(self.last_x-35, 300-20-30, self.last_x+35, 300-20)
        self.w1 = canvas.create_oval(self.last_x-30, 300-20, self.last_x-10, 300)
        self.w2 = canvas.create_oval(self.last_x+10, 300-20, self.last_x+30, 300)
        self.ball = canvas.create_oval(self.last_x - 10, rod_y_end - 10,
                                       self.last_x + 10, rod_y_end + 10
                                       , fill="gray")
        self.rod = canvas.create_line(self.last_x, self.rod_y_start,
                                      self.last_x, rod_y_end
                                      , width=3, fill="gray")

        # simulation
        self.x = 400.0
        self.x_dot = 0.0
        self.x_dot_dot = 0.0
        self.theta = radians(10)
        self.theta_dot = 0.0
        self.theta_dot_dot = 0.0
        self.time_scale = 0.01
        self.F = 0

        # controller
        self.input = {}
        self.output = {"F":0}
        self.controller = Reader().load_from_file("inverted_pendulum.fcl")

    def initialize(self):
        self.x = 400.0
        self.x_dot = 0.0
        self.x_dot_dot = 0.0
        self.theta = radians(randint(0, 360))
        self.theta_dot = 0.0
        self.theta_dot_dot = 0.0
        self.time_scale = 0.01
        self.F = 0

    def simulate(self):
        # print("x:{} x_dot:{} x_dot_dot:{} theta:{} theta_dot:{} theta_dot_dot:{}"
        #       .format(self.x, self.x_dot, self.x_dot_dot, self.theta, self.theta_dot, self.theta_dot_dot))

        N = m*(self.x_dot_dot-l*self.theta_dot*self.theta_dot*sin(self.theta)+l*self.theta_dot_dot*cos(self.theta))
        P = g + m*(l*self.theta_dot*self.theta_dot*cos(self.theta)+l*self.theta_dot_dot*sin(self.theta))

        self.x_dot_dot = 1/M*(self.F-N-b*self.x_dot)
        self.theta_dot_dot = 1/I*(-N*l*cos(self.theta)-P*l*sin(self.theta))

        self.x_dot += self.x_dot_dot*self.time_scale
        self.theta_dot += self.theta_dot_dot * self.time_scale

        self.theta = (self.theta + self.theta_dot * self.time_scale) % (2 * pi)
        self.x += self.x_dot*self.time_scale

    def control(self):
        self.input["theta"] = degrees(self.theta)
        self.input["theta_dot"] = self.theta_dot
        self.input["x_dot"] = self.x_dot
        self.controller.calculate(self.input, self.output)
        self.F = self.output["F"]
        # print(self.F)

    def update_view(self):
        delta_x = self.x % 800 - self.last_x
        self.last_x = self.x % 800
        theta = self.theta - radians(180)

        self.canvas.move(self.w1, delta_x, 0)
        self.canvas.move(self.w2, delta_x, 0)
        self.canvas.move(self.rect, delta_x, 0)

        mass_x, mass_y = int(self.last_x-sin(theta)*self.rod_len), int(self.rod_y_start-cos(theta)*self.rod_len)
        rod_x_1, rod_y_1 = int(self.last_x), int(self.rod_y_start)
        rod_x_2, rod_y_2 = int(self.last_x-sin(theta)*self.rod_len), int(self.rod_y_start-cos(theta)*self.rod_len)

        self.canvas.coords(self.ball, mass_x - 10, mass_y - 10,
                           mass_x + 10, mass_y + 10)
        self.canvas.coords(self.rod,  rod_x_1, rod_y_1,
                                      rod_x_2, rod_y_2)


class Environment(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        canvas = tk.Canvas(self, width=800, height=400)
        canvas.configure(background='white')
        canvas.pack()
        self.title("Inverted Pendulum")

        canvas.create_line(0, 301, 800, 301)

        self.canvas = canvas
        self.cart = Cart(canvas)
        self.cart.initialize()

        b = tk.Button(self, text="Quit", command=self.quit, anchor=tk.W)
        b.configure(width=3, relief=tk.FLAT)
        canvas.create_window(10, 10, anchor=tk.NW, window=b)

        b = tk.Button(self, text="Restart", command=self.cart.initialize, anchor=tk.W)
        b.configure(width=5, relief=tk.FLAT)
        canvas.create_window(70, 10, anchor=tk.NW, window=b)

        self.update()

    def update(self):

        self.cart.simulate()
        self.cart.update_view()
        self.cart.control()

        self.after(15, self.update)

if __name__ == "__main__":
    env = Environment()
    env.mainloop()