#Run the code
#You will see a black screen
#Click somewhere on the screen to place a point
#Repeat it two more times to get three points, which form our triangle (these are coloured red)
#Now place another random point somewhere inside of the triangle
#Click Run to start building of sierpinski triangle
#If you want to pause, click "stop" button
#If you want to resume it, click "run" button
#If you want to start off with clean slate again, click "reset" button

import pygame
import random

pygame.init()


#Constants
screen_width, screen_height = 1000, 700
fps = 100
radius_ver = 7
radius_inter = 4
font_size = 40
button_vertical_offset = 100
button_horizontal_offset = 100
button_vertical_spacing = 100


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sierpinski triangle")
clock = pygame.time.Clock()


#Dynamic variables
game_loop = True
points_ver = []
points_inter = []
reset = False
stop = True

#Text
font = pygame.font.Font(None, font_size)
reset_surf = font.render("RESET", True, (255, 255, 255))
reset_rect = reset_surf.get_rect()
run_surf = font.render("RUN", True, (255, 255, 255))    
run_rect = run_surf.get_rect()
stop_surf = font.render("STOP", True, (255, 255, 255))
stop_rect = stop_surf.get_rect()
button_width = reset_rect.width
button_height = reset_rect.height

reset_rect.center = (screen_width-button_width, button_height)
run_rect.center = (screen_width-button_width, button_height*2+button_height//2)
stop_rect.center = (screen_width-button_width, button_height*3+button_height)


#Functions

#---------------------------Geometry----------------------------------

#Checks if the point "p" lies on left side of line joining "p1" and "p2"
#Such condition is satisfied when cross product of vectors p1p2 and p1p is >= 0
def on_left_side(p1, p2, p):
    cross_product = (p2[0]-p1[0])*(p[1]-p1[1])-(p[0]-p1[0])*(p2[1]-p1[1])   
    if(cross_product >= 0):
        return True
    return False

#checks whether a point "p" is inside the triangle formed by the points in "points_ver"
def lies_inside(p):
    if(not on_left_side(points_ver[0], points_ver[1], p)):
        return False
    if(not on_left_side(points_ver[1], points_ver[2], p)):
        return False
    if(not on_left_side(points_ver[2], points_ver[0], p)):
        return False
    return True


#Arranges the points in "points_ver" in anti_clockwise manner
def orient_points():
    if(not on_left_side(points_ver[0], points_ver[1], points_ver[2])):
        points_ver[1], points_ver[2] = points_ver[2], points_ver[1]


#Generate new point from last point and randomly selected vertex point
def add_point():
    latest_point = points_inter[-1]
    ind = random.choice([0, 1, 2])
    random_vertex = points_ver[ind]
    new_x = (latest_point[0]+random_vertex[0])//2
    new_y = (latest_point[1]+random_vertex[1])//2
    points_inter.append((new_x, new_y))

#---------------------------Geometry----------------------------------


#---------------------------Displaying--------------------------------

#Draws all the points in "points_ver" and "points_inter"
def draw_points():
    if(len(points_ver) == 3):
        for i in range(3):
            pygame.draw.line(screen,(255, 0, 0), points_ver[i%3], points_ver[(i+1)%3])
    for center in points_ver:
        pygame.draw.circle(screen, (255, 0, 0), center, radius_ver)
    for center in points_inter:
        pygame.draw.circle(screen, (0, 255, 0), center, radius_inter)

        
def draw_buttons():
    screen.blit(reset_surf, reset_rect)
    screen.blit(run_surf, run_rect)
    screen.blit(stop_surf, stop_rect)


#updates the points onto the screen
def update_screen():
    screen.fill((0, 0, 0))
    draw_points()
    draw_buttons()
    pygame.display.update()

#---------------------------Displaying--------------------------------




while game_loop:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if(len(points_ver) < 3):
                    points_ver.append(event.pos)
                elif(len(points_inter) == 0):
                    points_inter.append(event.pos)
                    orient_points()
            
                if(stop_rect.collidepoint(event.pos)):
                    stop = True
                
                if(run_rect.collidepoint(event.pos)):
                    stop = False

                if(reset_rect.collidepoint(event.pos)):
                    reset = True
    
    if(reset):
        points_inter.clear()
        points_ver.clear()
        reset = False

    if(len(points_inter) > 0 and not stop):
        add_point()

    update_screen()

    


pygame.quit()