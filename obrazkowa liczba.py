from turtle import *
from math import sqrt


def zero(a, c):
    lt(45)
    fd(c)
    rt(45)
    pu()
    bk(a)
    rt(45)
    pd()
    fd(c)
    lt(45)

def jeden(a, c):
    zero(a, c)
    pu()
    bk(a)
    lt(90)
    pd()
    fd(a)
    bk(a)
    rt(90)
    pu()
    fd(a)
    pd()

def dwa(a, c):
    jeden(a, c)
    lt(90)
    fd(a)
    bk(a)
    rt(90)

def trzy(a, c):
    dwa(a, c)
    pu()
    bk(a/2)
    lt(90)
    pd()
    fd(a)
    bk(a)
    rt(90)
    pu()
    fd(a/2)
    pd()

def cztery(a, c):
    trzy(a, c)
    bk(a)
    fd(a)

def piec(a, c):
    cztery(a, c)
    lt(90)
    fd(a)
    rt(90)
    bk(a)
    fd(a)
    rt(90)
    fd(a)
    lt(90)

def szesc(a, c):
    piec(a, c)
    lt(90)
    fd(a/2)
    rt(90)
    bk(a)
    fd(a)
    rt(90)
    fd(a/2)
    lt(90)

def siedem(a, c):
    szesc(a, c)
    bk(a*3/4)
    lt(90)
    fd(a)
    bk(a)
    rt(90)
    fd(a*3/4)

def osiem(a, c):
    siedem(a, c)
    bk(a/4)
    lt(90)
    fd(a)
    bk(a)
    rt(90)
    fd(a/4)

def dziewiec(a):
    for i in range(2):
        fd(a/2)
        lt(90)
        fd(a)
        lt(90)
    fd(a/2)

def ol(liczba):
    speed(0)
    a = 720 / (len(str(liczba)) + (len(str(liczba)) - 1) / 2)
    c = sqrt(2) * a
    pu()
    bk(360)
    lt(90)
    bk(a/2)
    rt(90)
    pd()
    for i in str(liczba):
        if i == '0':
            zero(a, c)
        elif i == '1':
            jeden(a, c)
        elif i == '2':
            dwa(a, c)
        elif i == '3':
            trzy(a, c)
        elif i == '4':
            cztery(a, c)
        elif i == '5':
            piec(a, c)
        elif i == '6':
            szesc(a, c)
        elif i == '7':
            siedem(a, c)
        elif i == '8':
            osiem(a, c)
        elif i == '9':
            dziewiec(a)
        pu()
        fd(a/2)
        pd()
        
ol(45432)
