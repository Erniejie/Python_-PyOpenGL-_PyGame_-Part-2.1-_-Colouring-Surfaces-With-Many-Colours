#SENTDEX-OpenGL with PyOpenGL tutorial Python and PyGame - Part 2.1
#--- Coloring Surfaces with different colour-Example-Nov 6th 2014

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# 8 verticies(nodes)
verticies = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
    )

# 12 egdes:
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces=(
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1)
    )

def Cube():

    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        x +=1
        glColor3fv((0,1,0))  #  0:minimum ; 1:maximum

        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])





    glEnd()











    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()


def main():
    pygame.init()
    display =(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

    gluPerspective(45,(display[0]/display[1]) ,0.1, 50)

    glTranslate(0,0,-5)

    """ EXPLANATION:glRotate(degree,move in x,?,?)"""
    glRotate(0,0,0,0)   #  this "rotation function" makes the ANIMATION IN 3D

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        #glRotate(1,3,2,1)
        #glRotate(1,1,-1,1)
        glRotate(1,1,1,1)
                

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
