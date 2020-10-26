import turtle
import random

d = turtle.Turtle()

turtle.title("TMNT")
#title screen

d.color("purple")
d.shape("turtle")
d.shapesize(1,1,1)
d.penup()
d.goto(-470,100)
d.write("Donatello", False, align = "right")
d_life = 20
d.write(d_life, True, align="left", font=("Arial",20,"normal"))
#Donatello

l = d.clone()
l.color("blue")
l.penup()
l.goto(-470,50)
l.write("Leonardo", True, align = "right")
l_life = 20
l.write(l_life, True, align="left", font=("Arial",20,"normal"))
#Leonardo

r = d.clone()
r.color("red")
r.penup()
r.goto(-470,0)
r.write("Rafael", False, align = "right")
r_life=20
r.write(r_life, True, align="left", font=("Arial",20,"normal"))
#Rafael

m = d.clone()
m.color("orange")
m.penup()
m.goto(-470,-50)
m.write("Michelangelo", False, align = "right")
m_life=20
m.write(d_life, True, align="left", font=("Arial",20,"normal"))
#Michelangelo

s = d.clone()
s.color("black")
s.shapesize(1,1,1)
s.shape("circle")
s.penup()
s.goto(470,0)
s.write("BOSS", False, align = "left")
s_life=100
s.write(s_life, True, align="right", font=("Arial",20,"normal"))
#The Enemie

def attack_Donatello(x,y):
    print("The Boss lose ", die_outcome)
    print("hitpoints!")
    d.fd(30)
    d.write("Donatello", False, align="right")
    d.write(d_life, True, align="left", font=("Arial", 20, "normal"))

def attack_Leonardo(x,y):
    print("The Boss lose ", die_outcome)
    print("hitpoints!")
    l.fd(30)
    l.write("Leonardo", False, align="right")
    l.write(l_life, True, align="left", font=("Arial", 20, "normal"))

def attack_Rafael(x,y):
    print("The Boss lose ", die_outcome)
    print("hitpoints!")
    r.fd(30)
    r.write("Rafael", False, align="right")
    r.write(r_life, True, align="left", font=("Arial", 20, "normal"))

def attack_Michelangelo(x,y):
    print("The Boss lose ", die_outcome)
    print("hitpoints!")
    m.fd(30)
    m.write("Michelangelo", False, align="right")
    m.write(m_life, True, align="left", font=("Arial", 20, "normal"))


die = [1,2,3,4,5,6]
die_Boss = [9,11,12,14,15,16,17,18,19,20]
target_lst = [1,2,3,4]

n = 1
a = 1
b = 1
c = 1
f = 1

while n == 1:
    if s_life < 0:
        print("The TMNT WINS!")
        n=0
    elif d_life<=0 and l_life<=0 and r_life<=0 and m_life<=0:
        print("The BOSS WINS!")
        n=0
    else:
        if d_life <= 0 and a == 1:
            d.clear()
            d.hideturtle()
            target_lst.remove(1)
            a=0
        elif d_life > 0:
            die_outcome = random.choice(die)
            attack_Donatello(die_outcome,d_life)
            s_life = s_life - die_outcome
        if l_life <= 0 and b==1:
            l.clear()
            l.hideturtle()
            target_lst.remove(2)
            b=0
        elif l_life > 0:
            die_outcome = random.choice(die)
            attack_Leonardo(die_outcome, l_life)
            s_life = s_life - die_outcome
        if r_life <= 0 and c==1:
            r.clear()
            r.hideturtle()
            target_lst.remove(3)
            c=0
        elif r_life > 0:
            die_outcome = random.choice(die)
            attack_Rafael(die_outcome, r_life)
            s_life = s_life - die_outcome
        if m_life <= 0 and f==1:
            m.clear()
            m.hideturtle()
            target_lst.remove(4)
            f=0
        elif m_life > 0:
            die_outcome = random.choice(die)
            attack_Michelangelo(die_outcome, m_life)
            s_life = s_life - die_outcome
        dmg_Boss = random.choice(die_Boss)
        target = random.choice(target_lst)
        if target == 1:
            print("Donattelo lose ", dmg_Boss)
            print("hitpoints!")
            d_life = d_life - dmg_Boss
        if target == 2:
            print("Leonardo lose ", dmg_Boss)
            print("hitpoints!")
            l_life = l_life - dmg_Boss
        if target == 3:
            print("Rafael lose ", dmg_Boss)
            print("hitpoints!")
            r_life = r_life - dmg_Boss
        if target == 4:
            print("Michelangelo lose ", dmg_Boss)
            print("hitpoints!")
            m_life = m_life - dmg_Boss
        s.fd(-60)
        s.write("BOSS", False, align="left")
        s.write(s_life, True, align="right", font=("Arial", 20, "normal"))



