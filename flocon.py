from turtle import left, right, forward, setup, speed, tracer, hideturtle, up, down, update, exitonclick, done

def flocon(n):
    '''construction du flocon de Koch pré : n est positif ou nul'''
    for _ in range(3):
        ligne(n, 350)
        right(120)

def ligne(n, longueur):
    '''construction d'une ligne du triangle pré : n est positif ou nul, longueur est positif'''
    if n == 1:
        forward(longueur)
        return None
    ligne(n-1, longueur/3)
    left(60)
    ligne(n-1, longueur/3)
    right(120)
    ligne(n-1, longueur/3)
    left(60)
    ligne(n-1, longueur/3)

setup(600, 600, 100, 0)
#speed(0) # faire la figure le plus vite possible avec toutes les étapes
tracer(0) # faire la figure en une seule fois sans les étapes intermédiaires
hideturtle()
up()
left(90)
forward(200)
right(150)
down()

flocon(6)

update()
exitonclick()
done()