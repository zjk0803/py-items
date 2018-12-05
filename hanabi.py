
import thinter sa tk
from PIL import Image,ImageTK
from time import time,sleep
from random import choice,uniform,randint
from math import sin,cos,randians

#模拟重力
GRAVITY = 0.05
#颜色选项（随机或按顺序）
colors = ['red','blue','yellow','white','green','orange','purple','seagreen','indigo','cornflowerblue']
''' 
particles 类
例子在空中随机生成随机，变成一个圈、下坠、消失、
属性；
    - id：粒子的id
    - x，y：粒子的坐标
    - vx，vy：在坐标的变化速度
    - total：总数
    - age：粒子的存在时长
    - color：颜色
    - cv：画布
    - lifespan：最高存在时长
'''
class Particle:
  def __init__(self,cv,idx,total,explosion_speed,x=0.,y=0.,vx=0.,vy=0.,size=2.,color='red',lifespan=2, **kwargs):
    self.id = idx
    self.x = x
    self.y = y
    self.initial_speed = explosion_speed
    self.vx = vx
    self.vy = vy
    self.total = total
    self.age = 0
    self.color = color
    self.cv =cv
    self.cid = self.cv.create_oval(x - size,y - size,x + size,y + size,fill = self.color)
    self.lifespan = lifespan
