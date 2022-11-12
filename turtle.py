8.
import turtle
t=turtle.Turtle()
t.shape('turtle')
x1=int(input('큰 원의 중심좌표 x1: '))
큰 원의 중심좌표 x1: 0
y1=int(input('큰 원의 중심좌표 y1: '))
큰 원의 중심좌표 y1: 0
r1=int(input('큰 원의 반지름:'))
큰 원의 반지름:100
x2=int(input('작은 원의 중심좌표 x2: '))
작은 원의 중심좌표 x2: 10
y2=int(input('작은 원의 중심좌표 y2: '))
작은 원의 중심좌표 y2: 10
r2=int(input('작은 원의 반지름: '))
작은 원의 반지름: 50
t.up()
t.goto(x1,y1)
t.down()
t.circle(r1)
t.up()
t.goto(x2,y2)
t.down()
t.circle(r2)
rr=(((x1-x2)**2)+((y1-y2)**2))**0.5
if rr <= (r1+r2):
    t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
else:
    t.write("두번째 원이 첫번째 원의 외부에 있습니다.")
