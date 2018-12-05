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
  def update(self,dt):
    self.age += dt
    
    #粒子范围扩大
    if self.alive() and self.expand():
        move_x = cos(radians(self.id * 360 / self.total)) * self.initial_speed
        move_y = sin(radians(self.id * 360 / self.total)) * self.initial_speed
        self.cv.move(self.cid,move_x,move_y)
        self.vx = move_x / (float(dt) * 1000)
        
        #以自由落体坠落
        elif self.alive():
            move_x = cos(radians(self.id * 360 / self.total)) 
            # we technically don't need to update x,y because move will do the job
            self.cv.move(self.cid,self.vx + move_x,self.vy + GRAVITY * dt)
            self.vy += GRAVITY *dt
            
            #移动超过最高时长的粒子
            elif self.cid is not None:
                cv.delete(self.cid)
                self.cid = None
            #扩大的时间
            def expand (self):
                return self.age <= 1.2
            
            #粒子是否在最高存在时长内
            def alive(self):
                return self.age <= self.lifespan
'''
循环调用保持不停
'''
def simulate(cv):
    t = time()
    explode_points = []
    wait_time = randint(10,100)
                
