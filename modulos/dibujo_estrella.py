import turtle
estrella=turtle.Pen()


#ajustes para la estrella
estrella.speed(5)
estrella.right(90)

n=int(input('¿Cuantas puntas tiene su estrella?'))

#bucle para dibujar la estrella
for i in range(n):
    estrella.foward(100)
    estrella.right(180-180/n)
    