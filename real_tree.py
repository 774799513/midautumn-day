#import tensorflow as tf
#import matplotlib.pyplot as plt
#import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
#import math,sympy
#import time,os,sys, 
#import requests,re
#with open    as file:
from turtle import *
from random import *
from math import *
import time

# 设置全屏显示
setup(width=.8,height=1.0,startx=None,starty=None)
#获取宽和高
WIDTH = window_width()
HEIGHT = window_height()
# 画树函数
def tree(n, l):
    pd() # 下笔
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    # color_list2 = [int(255*t)]*3
    pencolor(t,t,t)
    pensize(2)
    forward(l) # 画树枝
    if n > 0:
        b = random() * 15 + 10 # 右分支偏转角度
        c = random() * 15 + 10 # 左分支偏转角度
        d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
        # 右转一定角度，画右分支
        right(b)
        tree(n - 1, d)
        # 左转一定角度，画左分支
        left(b + c)
        tree(n - 1, d)
        # 转回来
        right(c)
    else:
        # 画叶子
        right(90)
        n = cos(radians(heading() - 45)) / 5 + 0.5
        color_list = [n*0.5+0.5,0.4*n+0.4,0.4+0.4*n]
        # color_list_final = list(map(lambda x:int(255*x+10),color_list))
        # color(color_list_final)
        # color(randint(0,50),randint(250,255),randint(50,155))
        color(color_list)
        begin_fill()
        circle(3,360,randint(5,10))
        end_fill()
        left(90)

        # 添加0.3倍的飘落叶子
        if(random() > 0.7):
            pu()
            # 飘落
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)

            # 画叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            color_list1 = [n*0.5+0.5,0.4*n+0.4,0.4+0.4*n]
            # color_list1_final = list(map(lambda x:int(255*x),color_list1))
            # color(color_list1_final)
            color(color_list1)
            begin_fill()
            circle(2)
            end_fill()
            left(90)
            pu()

            #返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)# 退回
def diag():
    penup()
    goto(500,-500)
    pendown()
    pencolor(0,0.7,0.5)
    write("中秋节快乐！",False,align="center",font=('Arial',50,'normal'))
    penup()
    home()
    pensize(1)
bgpic('c.gif')
bgcolor(0.5, 0.5, 0.5) # 背景色
#ht() # 隐藏turtle
# speed(0) # 速度，1-10渐进，0最快
tracer(0, 0)
pu() # 抬笔
backward(500)
left(90) # 左转90度
pu() # 抬笔
backward(500) # 后退300
tree(12, 100) # 递归7层
diag()
done()
