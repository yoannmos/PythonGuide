"""
Module cinematic with scipy.optimize.root
"""
from scipy.optimize import root
import matplotlib.pyplot as plt


class CinematicPoint:
    """ Cinematic point """

    def __init__(self):

        self.position = None
        self.speed = None
        self.acceleration = None
        self.time = None

    def solve(self, other):
        """ Solve Equation"""

        def time_equation(other_time):
            # eq1 = 1/2.a0.t01**2 + v0.t01 + p01
            equation = (
                0.5 * self.acceleration * (other_time - self.time) ** 2
                + self.speed * (other_time - self.time)
                + self.position
                - other.position
            )
            return equation

        def position_equation(other_postion):
            # eq1 = 1/2.a0.t01**2 + v0.t01 + p01
            equation = (
                1 / 2 * self.acceleration * (other.time - self.time) ** 2
                + self.speed * (other.time - self.time)
                + self.position
                - other_postion
            )
            return equation

        def speed_equation(other_speed):
            # eq2 = a0.t01 + v0-v1
            equation = (
                self.acceleration * (other.time - self.time) + self.speed - other_speed
            )
            return equation

        def acceleration_and_time_equation(param):
            # eq3 = 1/2.a1.t1**2 + v0.t1 + p01
            # eq4 = a1*t1 + s0 - s1
            other_time, other_accel = param

            equation = [
                1 / 2 * other_accel * other_time ** 2
                + self.speed * other_time
                + self.position
                - other.position
            ]
            equation_2 = other_accel * other_time + self.speed - other.speed
            equation.append(equation_2)

            return equation

        loop = 0
        while loop < 5:
            loop += 1
            if other.time is None and other.acceleration is not None:
                try:
                    t_guess = [0.45]
                    result = root(time_equation, t_guess, method="lm")
                    other.time = round(float(result.x[0]), 3)
                except TypeError:
                    pass

            elif other.position is None:
                try:
                    p_guess = [0.8]
                    # print("position")
                    result = root(position_equation, p_guess, method="lm")
                    other.position = round(float(result.x[0]), 3)
                except TypeError:
                    pass

            elif other.speed is None:
                try:
                    # print("speed")
                    s_guess = [4.43]
                    result = root(speed_equation, s_guess, method="lm")
                    other.speed = round(float(result.x[0]), 3)
                except TypeError:
                    pass

            elif other.acceleration is None:
                try:
                    at_guess = [0.54, 50]
                    result = root(acceleration_and_time_equation, at_guess, method="lm")
                    other.time = round(float(result.x[0]) + self.time, 3)
                    other.acceleration = round(float(result.x[1]), 3)
                except TypeError:
                    pass

            elif (
                other.position and other.speed and other.acceleration and other.time
            ) is not None:
                # print("point solved")
                break

            # elif (
            #     other.position or other.speed or other.acceleration or other.time
            # ) is None:
            #     print("point not solved in this loop...")
            #     pass

            # print("point not solved in this loop...")

    def print_result(self, name):
        """ Print result """
        print("- ", name, ":")
        print(name + ".time =", self.time, "[s]")
        print(name + ".position =", self.position, "[m]")
        print(name + ".speed =", self.speed, "[m/s]")
        print(name + ".acceleration =", self.acceleration, "[m/s2]")
        print("\n")


class CinematicData:
    """ Cinematic point """

    def __init__(self):
        self.position = []
        self.speed = []
        self.acceleration = []
        self.time = []

    def append(self, cinematic_point):
        """ Append Method for cinematic point """
        # if cinematic_point.time == float:
        self.time.append(cinematic_point.time)
        self.position.append(cinematic_point.position)
        self.speed.append(cinematic_point.speed)
        self.acceleration.append(cinematic_point.acceleration)
        # if cinematic_point.time == list:
        #     self.time += cinematic_point.time
        #     self.position += cinematic_point.position
        #     self.speed += cinematic_point.speed
        #     self.acceleration += cinematic_point.acceleration


class Cinematic:
    """ Cinematic """

    def __init__(self, list_point, list_motion_type, pas):
        self.list_point = list_point
        self.list_motion_type = list_motion_type
        self.data = CinematicData()
        self.pas = pas

        self.create_cin()
        # print("Cinematic created")

    def uniform_movement(self, initial_point, final_point):
        """ Uniform Movement """
        calcul_time = 0

        while self.data.time[-1] < final_point.time:
            calcul_time += self.pas
            calcul_time = round(calcul_time, 3)
            calcul_point = CinematicPoint()
            calcul_point.time = calcul_time
            calcul_point.acceleration = final_point.acceleration
            initial_point.solve(calcul_point)

            calcul_point.time = initial_point.time + calcul_time
            self.data.append(calcul_point)
        # print("UM Done")

    def uniform_accelerated_movement(self, initial_point, final_point):
        """ Uniform Accelerated Movement """
        calcul_time = 0
        if not self.data.time:
            self.data.append(initial_point)

        while self.data.time[-1] < final_point.time:
            calcul_time += self.pas
            if calcul_time > final_point.time:
                break
            else:
                calcul_time = round(calcul_time, 3)
                calcul_point = CinematicPoint()
                calcul_point.time = calcul_time
                calcul_point.acceleration = initial_point.acceleration
                initial_point.solve(calcul_point)

                calcul_point.time = initial_point.time + calcul_time
                self.data.append(calcul_point)

        self.data.append(final_point)
        # print("UAM Done")

    def uniform_deccelerated_movement(self, initial_point, final_point):
        """ Uniform Accelerated Movement """
        calcul_time = initial_point.time
        while self.data.time[-1] < final_point.time:
            calcul_time += self.pas
            if calcul_time > final_point.time:
                break
            else:
                calcul_time = round(calcul_time, 3)
                calcul_point = CinematicPoint()
                calcul_point.time = calcul_time
                calcul_point.acceleration = final_point.acceleration
                initial_point.solve(calcul_point)
                self.data.append(calcul_point)

        self.data.append(final_point)
        # print("UDM Done")

    # def non_uniform_accelerated_movement(self, initial_point, final_point):
    #     """ Non-uniform Accelerated movement """
    #     print("NUAM Done")

    def create_cin(self):
        """ Create a set of data point between cinematitic point """

        for point in range(len(self.list_point) - 1):

            if self.list_motion_type[point] == "UM":
                self.uniform_movement(
                    self.list_point[point], self.list_point[point + 1]
                )
            if self.list_motion_type[point] == "UAM":
                self.uniform_accelerated_movement(
                    self.list_point[point], self.list_point[point + 1]
                )
            # if self.list_motion_type[point] == "NUAM":
            #     self.non_uniform_accelerated_movement(
            #         self.list_point[point], self.list_point[point + 1]
            #     )
            if self.list_motion_type[point] == "UDM":
                self.uniform_deccelerated_movement(
                    self.list_point[point], self.list_point[point + 1]
                )

    def plot_result(self):
        """ Plot curve and point """

        ax1 = plt.subplot(131)
        plt.title("Position [m]")
        plt.xlabel("time [s]")
        plt.plot(self.data.time, self.data.position, "-")
        for point in self.list_point:
            plt.scatter(point.time, point.position)

        plt.subplot(132, sharex=ax1)
        plt.title("Speed [m/s]")
        plt.xlabel("time [s]")
        plt.plot(self.data.time, self.data.speed, "-")
        for point in self.list_point:
            plt.scatter(point.time, point.speed)

        plt.subplot(133, sharex=ax1)
        plt.title("Acceleration [m/s2]")
        plt.xlabel("time [s]")
        plt.plot(self.data.time, self.data.acceleration, "-")
        for point in self.list_point:
            plt.scatter(point.time, point.acceleration)

        plt.show()


if __name__ == "__main__":

    GRAVITY = 9.81
    PAS = 0.01

    C_1 = CinematicPoint()
    C_1.time = 0
    C_1.position = 2
    C_1.speed = 0
    C_1.acceleration = -GRAVITY
    C_1.print_result("C_1")

    C_2 = CinematicPoint()
    C_2.position = 0.2
    C_2.acceleration = -GRAVITY
    C_1.solve(C_2)
    C_2.print_result("C_2")

    C_3 = CinematicPoint()
    C_3.position = 0.0
    C_3.speed = 0
    C_2.solve(C_3)
    C_3.print_result("C_3")

    C_2p = CinematicPoint()
    C_2p.time = C_2.time  # + PAS
    C_2p.position = C_2.position
    C_2p.speed = C_2.speed
    C_2p.acceleration = C_3.acceleration
    C_2p.print_result("C_2p")

    CINEMATIC = Cinematic([C_1, C_2, C_2p, C_3], ["UAM", "UAM", "UDM"], PAS)
    CINEMATIC.plot_result()
