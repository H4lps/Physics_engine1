import pygame
import math
import random
class Particle:
    #Constructor
    def __init__(self,box,vx,vy,mass,charge,radius =5):
        self.pos = pygame.math.Vector2(
                                        random.randint(box.left +100,box.right-100)
                                       ,random.randint(box.top +100,box.bottom-100)
        )
        self.vel = pygame.math.Vector2(vx,vy)
        self.mass = mass
        self.charge = charge
        self.radius = radius

    #Updates the position for each frame
    #This also handles collisions
    def update_position(self,dt,box):
        self.pos += self.vel * dt

        if self.pos.x <= box.left +self.radius:
            self.vel = self.vel *-.95
            self.pos.x+= 15
        elif self.pos.x >= box.right -self.radius:
            self.vel = self.vel *-.95
            self.pos.x -=15
        elif self.pos.y <= box.top + self.radius:
            self.vel = self.vel *-.95
            self.pos.y+= 15
        elif self.pos.y >= box.bottom -self.radius:
            self.vel = self.vel *-.95
            self.pos.y -=15
        
    #Draws each circle on the screen based on charge
    def draw(self,screen):
        if self.charge >0:
            color = (255,0,0)
        elif self.charge<0:
            color = (0,0,255)
        else:
            color = (100,100,100)
        
        pygame.draw.circle(screen,color,(int(self.pos.x),int(self.pos.y)),int(self.radius))
    
class Simulation:
    #Force of gravity for each particle
    def force_gravity(self,p1,dt):
        Fg = p1.mass * 9.8
        ay = Fg / p1.mass
        p1.vel.y += ay * dt
    
    #Strong Nuclear Force
    def strong_nuclear_force(self,p1,p2,dt):
        dx = p1.pos.x - p2.pos.x
        dy = p1.pos.y - p2.pos.y
        radius = math.sqrt((dx)**2 + (dy)**2)/20
        range_force = 1
        g = 1000
        force_magnitude = (g**2) *math.exp(-radius/range_force)/range_force
        if radius < range_force:
            p1.vel.x =0.01
            p2.vel.x =0.01
            p1.vel.y =0.01
            p2.vel.y =0.01
            p1.vel *= -((radius/force_magnitude)**2)
            p2.vel *= -((radius/force_magnitude)**2)
    #Electric force Interactiorns
    def force_electric(self,p1,p2,dt):
        dx = p1.pos.x - p2.pos.x
        dy = p1.pos.y - p2.pos.y
        radius = math.sqrt((dx)**2 + (dy)**2)/20
        force_magnitude = (p1.charge* p2.charge)/(radius**2)
        fx = force_magnitude *dx / radius
        fy = force_magnitude * dy/radius

        a1x = fx/p1.mass
        a1y = fy/p1.mass
        a2x = -fx/p2.mass
        a2y = -fy/p2.mass


        p1.vel.x += a1x*dt 
        p1.vel.y += a1y*dt
        p2.vel.x += a2x*dt
        p2.vel.y += a2y*dt

        #Handles Two opposite charged particles from crashing into each other
        if radius <= 1 and p1.charge * p2.charge <0:
            p1.vel *= -((radius/2)**2)
            p2.vel *= -((radius/2)**2)
    def resolve_overlap(self,p1,p2):
        delta = p2.pos -p1.pos
        distance = delta.length()
        min_distance = p1.radius + p2.radius
        if distance <min_distance:
            overlap = min_distance - distance
            direction = delta/distance
            correction = (direction * (overlap / 2))*4
            p1.pos += correction
            p2.pos -= correction
