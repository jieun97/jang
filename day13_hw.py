import turtle as t 
import random #임의의 수를 뽑는 기능 구현

#벽그리기
t.speed(0) 
t.pensize(3)
t.color("red")
t.up() 
t.goto(-250,-250) #벽그리기 시작위치로 이동
t.down()
for x in range(4): #아래 작업 4번 반복
    t.fd(500) 
    t.lt(90)

t.up() 
t.home() #거북이의 위치와 방향을 처음 상태로 돌림
t.down()

t.pensize(1)
t.color("black")

a=random.randint(0,359) #a는 0부터 359사이에 있는 임의의 정수

t.seth(a) #거북이의 방향을 랜덤 설정된 각도로  회전

while -250 < t.xcor() < 250 and -250 < t.ycor() < 250:#벽 안쪽 공간에 거북이가 위치하는 동안
    t.fd(1) #앞으로 1씩 이동
#벽에 부딪칠 때까지 1씩 이동

while True: #아래 작업 영원히 반복
    b=t.heading() #현재 바라보는 각도 저장
    
    if a==0 or a==45 or a==90 or a==135 or a==180 or a==225 or a==270 or a==315: #거북이가 [모서리,(250,0),(0,250),(-250,0),(0,-250)]로 향하면 
        t.lt(180) #왼쪽으로 180도 회전
        t.fd(1) #벽에서 1만큼 앞으로  이동
        while -250<t.xcor()<250 and -250<t.ycor()<250: #벽 내부에 위치할 동안
            t.fd(1) #1씩 앞으로 이동(벽에 부딪칠 때까지 이동)
            
    if 0<b<45 or 135<b<180 or 225<b<270:
        if -250<t.xcor()<250: #좌우 벽에 부딪치면
            t.seth(360-b) 
            t.fd(1) 
            while -250 <t.xcor()< 250 and -250<t.ycor()< 250:  
                t.fd(1) 
        else:  #위아래 벽에 부딪치면
            t.seth(180-b) 
            t.fd(1) 
            while -250<t.xcor()< 250 and -250 <t.ycor()< 250:  
                t.fd(1)
                
    if 45<b<135 or 180<b<225 or 270<b<360 and b!=315: 
        if -250<t.xcor()< 250 : 
            t.seth(360-b) 
            t.fd(1) 
            while -250<t.xcor()< 250 and -250<t.ycor()< 250:  
                t.fd(1) 
        else: 
            t.seth(540-b) 
            t.fd(1) 
            while -250<t.xcor()<250 and -250<t.ycor()< 250:  
                t.fd(1)
                
    


