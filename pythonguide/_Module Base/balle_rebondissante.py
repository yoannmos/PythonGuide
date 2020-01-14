import os, time, math
from pprint import pprint

from random import randrange


class Board:
    
    def __init__(self, size=[15, 40]):
        self.size = size

    def get_status(self, position):
        if position.x >= self.size[1] or position.y >= self.size[0]:
            return "NaN"
        else:
            return self.layout[position.y][position.x]  

    @property
    def layout(self):
        layout = []
        for l in range(self.size[0]):
            ligne_value = []

            if l==0 or l==self.size[0]-1:
                ligne_value = [1 for p in range(self.size[1])]
            else:
                for c in range(self.size[1]):
                    if c==0 or c==self.size[1]-1:
                        ligne_value.append(1)
                    else:
                        ligne_value.append(0)
            layout.append(ligne_value)
        return layout

    

# if __name__ == "__main__":
#     b = Board()
#     print(b.size)
#     print(b.layout)
     

class Vector:
    """ 
    TODO : Add Origine and Extremity
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x,y)

    def __repr__(self):
        return "[{}, {}]".format(self.x, self.y)

    @property
    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def angle(self):
        theta_x = None
        theta_y = None
        # theta = None
        try:
            theta_x = math.acos(self.x/self.norme)
            theta_y = math.asin(self.y/self.norme)

        except ZeroDivisionError:
            print('Error on angle')
            return 0

        # finally:
        if theta_y and theta_y < 0:
            return theta_x + abs(theta_y)*2
        else:
            return theta_x 
        
            # if thetasin < 0:



        #     theta = math.acos(self.x/self.norme)
        # except ZeroDivisionError:
        #     pass
        # else:
        #     
        # return round(theta*180 /math.pi, 10)
        # try:
        #     theta1f = math.acos(self.x/self.norme)
        #     theta1 = round(theta1f*180 /math.pi, 10)
        # except ZeroDivisionError:
        #     theta1 = "Error"
        # try:
        #     theta2f = math.asin(self.y/self.norme)
        #     theta2 = round(theta2f*180 /math.pi, 10)
        # except ZeroDivisionError:
        #     theta2 = "Error"

        # return [theta_x, theta_y]

    def rotation(self, angle_degree):
        angle_radian = angle_degree *  math.pi / 180
        self.x = round(self.x * math.cos(angle_radian) -  self.y * math.sin(angle_radian),1)
        self.y = round(self.x * math.sin(angle_radian) +  self.y * math.cos(angle_radian),1)
        return

if __name__ == "__main__":
    # v = Vector(-2, -2)
    # print(v)
    # print("norm = ", v.norme)
    # print("angle = ",v.angle)

    v = Vector(0, 0)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(1, 0)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(1.24, 1.24)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(0, 1)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(-1.24, 1.24)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(-1, 0)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(-1.24, -1.24)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(0, -1)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(1.24, -1.24)
    print("angle = ", 180*v.angle/math.pi)
    v = Vector(1, 0)
    print("angle = ", 180*v.angle/math.pi)

    # v.rotation(45)
    # print(v)

# class Ball():

#     def __init__(self):
#         self.board = Board()
#         px = randrange(1, self.board.size[1], 1)
#         py = randrange(1, self.board.size[0], 1)
#         self.position = Vector(px, py)
#         # vx = randrange(-1, 2, 1)
#         # vy = randrange(-1, 2, 1)
#         vx = -1
#         vy = -1
#         self.vitesse = Vector(vx, vy)

#     def move(self):

#         new_vitesse = self.vitesse
#         new_position = self.position + self.vitesse
#         status_new_position = self.board.get_status(new_position)

#         if status_new_position != 0:
#             if abs(new_vitesse.x) + abs(new_vitesse.y) == 2:
#                 # Rotation 90 Anti-Horaire
#                 test_vitesse = self.vitesse.rotation(90)
#                 test_position = self.position + test_vitesse
#                 status_test_position = self.board.get_status(test_position)
#                 if status_test_position == 0:
#                     new_vitesse = test_vitesse
#                 else:
#                     new_vitesse = self.vitesse.rotation(-90)
#             else:
#                 new_vitesse = new_vitesse.rotation(180)

#             new_position = self.position + new_vitesse

#         self.vitesse = new_vitesse
#         self.position = new_position
#         return  self.position, self.vitesse

    
# class Game(Ball):

#     def __init__(self):
#         super().__init__()
#         self.board = Board()

#     def draw_game(self):
#         os.system('cls')
#         for l in range(self.board.size[0]):
#             for c in range(self.board.size[1]):
#                 coordinate = Vector(c,l)
#                 status = self.get_status(coordinate)
#                 if status == 1:
#                     print("X", end='')
#                 elif status == 0:
#                     if self.position.x == coordinate.x and self.position.y == coordinate.y :
#                         print("o", end='')
#                     else:
#                         print(" ", end='')
#                 else:
#                     print("ERROR")
#                 # print(self.board.get_status(position), end='')
#             print("")

#     def play_game(self):
#         playtime = 200 + 1
#         t = 0
#         while t < playtime :
#             self.draw_game()

#             print ("frame =",t,"/",playtime-1, end='')
#             print (" | Position :",self.position.x,":", self.position.y, end='')
#             print (" | Vitesse :", self.vitesse.x,":", self.vitesse.y)

#             self.move()
#             t += 1
            
#             time.sleep(0.03)
            

# 

#     a = Game()
#     a.play_game()

