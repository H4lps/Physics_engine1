# Example file showing a basic pygame "game loop"
import pygame

import Physics_utils
# pygame setup

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
list_chars = [pygame.K_0,pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
              pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
mass_text = ''
charge_text = ''
#Initializing Simulation class
sim = Physics_utils.Simulation()
mass_active=False;charge_active=False
particles = []
dt = 1/20
while running:
    #Event Handling
    for event in pygame.event.get():
        #Quit Button
        if event.type == pygame.QUIT:
            running = False
        #Generation of Particles
        if event.type == pygame.MOUSEBUTTONDOWN:
            if generate_particle_positve_button.left <= mouse[0] <=generate_particle_positve_button.right and generate_particle_positve_button.top <= mouse[1] <= generate_particle_positve_button.bottom:
                if len(charge_text) >0 and len(mass_text) >0 and int(mass_text) >0:
                    new_particle = Physics_utils.Particle(box,5,5,int(mass_text),int(charge_text))
                else:
                    new_particle = Physics_utils.Particle(box,0,1,5,5)
                particles.append(new_particle)
            if mass_button.collidepoint(event.pos):
                mass_active = True
            else:
                mass_active = False
            if charge_button.collidepoint(event.pos):
                charge_active =True
            else:
                charge_active =False
        
        if event.type == pygame.KEYDOWN: 
            if mass_active ==True:
                if event.key == pygame.K_BACKSPACE and len(mass_text) >0: 

                    # get text input from 0 to -1 i.e. end. 
                    mass_text = mass_text[:-1]
                # Unicode standard is used for string 
                # formation 
                elif len(mass_text) <7 and event.key in list_chars: 
                    mass_text += event.unicode
            if charge_active ==True:
                if event.key == pygame.K_BACKSPACE and len(charge_text) >0: 

                    # get text input from 0 to -1 i.e. end. 
                    charge_text = charge_text[:-1]
                if len(charge_text) ==0 and event.key == pygame.K_MINUS:
                    charge_text += '-'
                # Unicode standard is used for string 
                # formation 
                elif len(charge_text) <7 and event.key in list_chars: 
                    charge_text += event.unicode


    #Generating Static elements

    screen.fill("black")
    font = pygame.font.Font(None,50)
    box = pygame.draw.rect(screen,color=(255,255,255),rect=pygame.Rect(screen.get_width()/5,screen.get_height()/5,600,400),width=10)
    screen.blit(font.render("Physics Engine",True,(255,255,255)),(box.left,box.top-40))

    font = pygame.font.Font(None,30)
    box_2=pygame.draw.rect(screen,color=(255,255,255),rect=pygame.Rect(screen.get_width()-200,100,200,400),width=4)
    screen.blit(font.render("Particle Generator",True,(255,255,255)),(box_2.left,box_2.top-20))

    font = pygame.font.Font(None,24)
    generate_particle_positve_button = pygame.draw.rect(screen,color=(255,0,0),rect=pygame.Rect(box_2.left+4,box_2.bottom-104,box_2.width-10,100))
    screen.blit(font.render("Generate",True,(255,255,255)),(generate_particle_positve_button.left,generate_particle_positve_button.top+20))



    mass_label = screen.blit(font.render("Mass",True,(0,255,81)), (box_2.left+10, box.top+10))
    mass_button = pygame.draw.rect(screen,color=(0,255,81),rect=pygame.Rect(mass_label.right + 40,mass_label.top-10,80,30),width=2)

    mass_text_surface = font.render(mass_text, True, (255, 255, 255)) 
    screen.blit(mass_text_surface, (mass_button.left+5, mass_button.top+5))

    charge_label = screen.blit(font.render("Charge",True,(255,170,0)), (box_2.left+10, mass_label.bottom+20))
    charge_button = pygame.draw.rect(screen,color=(255,170,0),rect=pygame.Rect(mass_button.left,charge_label.top,80,30),width=2)

    charge_text_surface = font.render(charge_text,True,(255,255,255))
    screen.blit(charge_text_surface, (charge_button.left+5, charge_button.top+5))
    #Applying all forces and updating velocities in the time interval
    for i,p in enumerate(particles):
        if p.nuke == False:
            sim.force_gravity(p,dt)
    for i,p in enumerate(particles):
        if len(particles) >1:
            for j in range(i+1,len(particles)):
                sim.force_electric(p,particles[j],dt)
                sim.resolve_overlap(p,particles[j])
                if (p.charge * particles[j].charge == 0) and not(p.charge <0 or particles[j].charge<0):
                    sim.strong_nuclear_force(p,particles[j],dt)


    #Updating positions and visualizing
    for p in particles:
        p.update_position(dt,box)
        p.draw(screen)
    

    mouse = pygame.mouse.get_pos()
    
    pygame.display.flip()

    clock.tick(120)  

pygame.quit()