#on a grid, the formula for the distance is
# math.sqrt(x_diffrence**2 + y_diffrence**2)
# Diaganol lines are worth sqrt(2) EXACTLY DIAGANOL
# straight line is worth 1
# 1 y two x is worth 2.23606797749979
import math

class Node:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return int(self.x)
    def get_y(self):
        return int(self.y)
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y

node1 = Node(x=2,y=3)
node2 = Node(x=1, y=1)

x_diff= node1.x - node2.x
y_diff= node1.y - node2.y

total_diff = math.sqrt(x_diff**2 + y_diff**2)
print(total_diff)