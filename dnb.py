import pygame
import os
import random

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/',os.sep).replace('\\',os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

pygame.init()
pygame.mixer.init(channels=4)
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('[^0^] I AIN\'T DO SHIT !!!!!!!!! [.~.]')
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont("Monaco", 30)
text = font.render("YOOOOOO", True, (255, 255, 255))

crash1 = 'sample/amen/amencrash1.wav'
kick1 = 'sample/amen/amenkick1.wav'
kickcrash = 'sample/amen/amenkickcrash1.wav'
snare1 ='sample/amen/amensnare1.wav'
snare2 ='sample/amen/amensnare2.wav'
ride = 'sample/amen/amenride.wav'
snareride = 'sample/amen/amensnareride1.wav'
punchy = 'sample/amen/organ2gs.wav'

org_a = 'sample/organ/org_a.wav'
org_b = 'sample/organ/org_b.wav'
org_c = 'sample/organ/org_c.wav'
org_d = 'sample/organ/org_d.wav'
org_e_fl = 'sample/organ/org_e_fl.wav'
org_f = 'sample/organ/org_f.wav'
org_f_sh = 'sample/organ/org_f_sh.wav'
org_g_sh = 'sample/organ/org_g_sh.wav'
org_rest = 'sample/organ/org_rest.wav'
org_drest = 'sample/organ/org_drest.wav'

bpm = 750 # 80bpm 
bpm_time = 0 

while not done:
    # Event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
           is_blue = not is_blue

    # Key bindings
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]: 
        pygame.mixer.music.load(kick1)
        pygame.mixer.music.play(0)
    if pressed[pygame.K_s]: 
        pygame.mixer.music.load(snare1)
        pygame.mixer.music.play(0)
    if pressed[pygame.K_d]: 
        pygame.mixer.music.load(crash1)
        pygame.mixer.music.play(0)

	# Drum Samples
    drummy = [kick1,snare1,snare2,snareride,crash1,kickcrash,ride,org_rest]
    randy = random.randint(0,len(drummy)-1)
    drum = pygame.mixer.Sound(drummy[randy])
    #pygame.mixer.Channel(0).play(drum)

	# Synth Samples
    orgi = [org_a,org_b,org_c,org_d,org_e_fl,org_f,org_f_sh,org_g_sh,org_rest,org_drest]
    rando = random.randint(0,len(orgi)-1)    
    synth = pygame.mixer.Sound(orgi[rando])
    synth2 = pygame.mixer.Sound(orgi[randy])

    # Timing
    ticky = clock.tick()
    bpm_time += ticky 
    if bpm_time > 150:
        pygame.mixer.Channel(0).stop
        pygame.mixer.Channel(1).stop
        pygame.mixer.Channel(2).stop
        pygame.mixer.Channel(0).play(drum)
        pygame.mixer.Channel(1).play(synth)
        #pygame.mixer.Channel(2).play(synth2)
        bpm_time = 0


	# Sprite and Text
    screen.fill((0,0,0)) # Redraw the screen
    sX = random.randint(0,300)
    sY = random.randint(0,200)
    screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
    screen.blit(get_image('lil_black.png'),(sX,sY))

    # Ending
    pygame.display.flip()
    #clock.tick(30)
    
