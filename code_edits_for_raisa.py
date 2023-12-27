#Official Zombie Game code
import random

# changed this from arbitrary numbers (1-4) just used as labels/flags in own variables
# to numbers used in PyGame angle setting variables/functions to simplify code
LEFT = 180
UP = 90
RIGHT = 0
DOWN = -90


# defines standard movement amount, change bigger/smaller to make characters move faster/slower
STEP_DISTANCE = 3


# defines constants for size of game screen, midpoints, and a standard offset amount from edges
WIDTH = 800
HEIGHT = 800
HORIZ_CENTER = WIDTH / 2
VERT_CENTER = HEIGHT / 2
OFFSET = 100
BARN_X = 700
BARN_Y = 100
LAB_X = 100
LAB_Y = 700


# sets the initial scores to zero, IDs that game isn't over and weapon is available but not out
human_health = 150
zombie_health = 100
game_over = False
weapon_out = False
weapon_available = True


# identifies the exact .png file names for all of the art in your images folder
ZOMBIE_ART = 'zombie'
MIRRORED_ZOMBIE_ART = 'zombie_mirror'
HUMAN_ART = 'human'
MIRRORED_HUMAN_ART = 'human_mirror'
HUMAN_W_WEAPON_ART = 'human_weapon'
MIRRORED_HUMAN_W_WEAPON_ART = 'human_mirror_weapon'
HEALTHKIT_ART = 'healthkit'
BACKGROUND_ART = 'background'
# background art needs to be exactly 800 by 800 pixels in size and include your farm & lab where you want them


# creates game objects using png images in the 'Images' folder with the EXACT names in quotes above
zombie = Actor(ZOMBIE_ART)
human = Actor(HUMAN_ART)
healthkit = Actor(HEALTHKIT_ART)


# defines starting positions and directions for the human and zombie game objects
human.pos = BARN_X, BARN_Y  # human starts at barn position
zombie.pos = LAB_X, LAB_Y  # zombie starts at lab position
human.angle = DOWN  # human starts facing down
zombie.angle = RIGHT  # zombie starts facing right


def set_art():
'''
this function sets the right art for the human and zombie game objects given their
current direction and whether or not the humans weapon is out
'''

    if zombie.angle == LEFT:
        zombie.image = MIRRORED_ZOMBIE_ART
    else:
        zombie.image = ZOMBIE_ART

    if weapon_out:
        if human.angle == LEFT:
            human.image = MIRRORED_HUMAN_W_WEAPON_ART
        else:
            human.image = HUMAN_W_WEAPON_ART
    else:
        if human.angle == LEFT:
            human.image = MIRRORED_HUMAN_ART
        else:
            human.image = HUMAN_ART


def reset_positions():
    human.pos = BARN_X, BARN_Y  # human resets at barn position
    zombie.pos = LAB_X, LAB_Y  # zombie resets at lab position


def turn(human_or_zombie_obj, relative_turn):
'''
this function takes a game actor object (human or zombie) and a relative turn direction
(LEFT or RIGHT) and uses it to update the angle that game actor object is facing. For example,
turn(human, LEFT) would take a human game object that was facing right and turn it to face up
'''

    if relative_turn == LEFT:
    # if you're turning left, add 90deg to your current angle unless you're
    # already at the max value of 180deg, in which case reset to -90
        if human_or_zombie_obj.angle == LEFT:
            human_or_zombie_obj.angle = DOWN
        else:
            human_or_zombie_obj.angle = human_or_zombie_obj.angle + 90

    elif relative_turn == RIGHT:
    # if you're turning right, subtract 90deg unless already at min angle value
        if human_or_zombie_obj.angle == DOWN:
            human_or_zombie_obj.angle = LEFT
        else:
            human_or_zombie_obj.angle = human_or_zombie_obj.angle - 90


def move_forward(human_or_zombie_obj):
'''
this function takes in either the zombie game object or the human game object and then checks
the direction that it's facing and moves that game object in the corresponding direction
for example, if the zombie was facing down, move_forward(zombie) would increase the y value of the
zombie object's position, moving the zombie character farther down the vertical (y) axis of screen
'''
    if human_or_zombie_obj.angle == UP:
        human_or_zombie_obj.y = human_or_zombie_obj.y - STEP_DISTANCE
    elif human_or_zombie_obj.angle == RIGHT:
        human_or_zombie_obj.x = human_or_zombie_obj.x + STEP_DISTANCE
    elif human_or_zombie_obj.angle == LEFT:
        human_or_zombie_obj.x = human_or_zombie_obj.x - STEP_DISTANCE
    elif human_or_zombie_obj.angle == DOWN:
        human_or_zombie_obj.y = human_or_zombie_obj.y + STEP_DISTANCE


def put_away_weapon():
    global weapon_out
    weapon_out = False
    schedule_unique(cooldown, 2)


def cooldown():
    global weapon_available
    weapon_available = True


def new_healthkit():
    rand_x = random.randint(OFFSET, (WIDTH - OFFSET))
    rand_y = random.randit(OFFSET, (HEIGHT - OFFSET))
    healthkit.x = rand_x
    healthkit.y = rand_y


new_healthkit()


def update():
    global game_over, weapon_out, weapon_available, human_health, zombie_health
    if not game_over:
        if keyboard.k and weapon_available:
            weapon_out = True
            weapon_available = False
            schedule_unique(put_away_weapon, 1)
        elif keyboard.i:
            move_forward(human)
        elif keyboard.j:
            turn(human, LEFT)
        elif keyboard.l:
            turn(human, RIGHT)

        if keyboard.w:
            move_forward(zombie)
        elif keyboard.a:
            turn(zombie, LEFT)
        elif keyboard.d:
            turn(zombie, RIGHT)

        zombie_contact = human.colliderect(zombie)  # checks if human touches zombie
        healthkit_contact = human.colliderect(healthkit)  # checks if human touches healthkit

        if zombie_contact:
            if weapon_out:  # human wins, zombie health decreases
                zombie_health = zombie_health - 10
            else:  # no weapon, zombie wins, human health decreases
                human_health = human_health - 20
            reset_positions()  # in either case, reset player positions
        elif healthkit_contact and (human_health <= 145):
            human_health = human_health + 5
            new_healthkit()

        if (human_health <= 0) or (zombie_health <= 0):
            game_over = True


def draw():
    if game_over:
        if human_health <= 0:
            screen.fill("dark red")
            screen.draw.text("The Zombie won!", topleft=(10, 10), fontsize=60)
        elif zombie_health <= 0:
            screen.fill("dark red")
            screen.draw.text("The Human won!", topleft=(10, 10), fontsize=60)
    else:
        screen.blit(BACKGROUND_ART, (0,0))
        screen.draw.text("Human Health: " + str(human_health), color="white", topleft=(10, 10))
        screen.draw.text("Zombie Health: " + str(zombie_health), color="green", topleft=(10, 50))
        set_art()
        zombie.draw()
        human.draw()
        healthkit.draw()

