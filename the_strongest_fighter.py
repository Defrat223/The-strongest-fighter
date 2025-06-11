import pygame
import random
pygame.init()
put = ''
put_ = 'C:/Program Files/the_strongest_fighter/'

back = pygame.image.load(put+'images/set/back.png')
back_0_x = 0
back_1_x = 1600
back_2_x = -1600
end = pygame.image.load(put+'images/set/end.png')
win = pygame.image.load(put + 'images/set/win.png')

screan = pygame.display.set_mode((1600,600))
clock = pygame.time.Clock()
icon = pygame.image.load('images/set/ico.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('The strongest fighter')

tik_6 = 0
tik_3 = 0

text = pygame.font.Font(put + 'images/text/text.ttf',30)
text_hp = text.render('HP:',True,'white')
text_kills = text.render('пройдено волн:',True,'red')

main_manu = pygame.image.load(put + 'images/set/menu/main.png')
setting_manu = pygame.image.load(put + 'images/set/menu/setting.png')
setting_open__manu = pygame.image.load(put + 'images/set/menu/setting_open.png')
stat_manu = pygame.image.load(put + 'images/set/menu/start.png')

piece = pygame.image.load(put + 'images/set/piece.png')
piece_y = -10

platforma = pygame.image.load(put + 'images/set/platforma.png')
platforma_list = []
platforma_x = 1601
platforma_y = 475

hp_bar_x = 0

player_wait_right = pygame.image.load(put+'images/walk_right/1.png')
player_wait_left = pygame.image.load(put+'images/walk_left/1.png')
player_jump_right = pygame.image.load(put+'images/jump/1.png')
player_jump_left = pygame.image.load(put+'images/jump/2.png')
player_platform_hit_box = pygame.image.load(put + 'images/player/hit_platform.png')
player_jump_is_ = True

punch_efekt = pygame.image.load(put+'images/punch/boom.png')
punch_efekt_1 = pygame.image.load(put+'images/punch/boom_1.png')

player_walk_left = [
    pygame.image.load(put+'images/walk_right/2.png'),
    pygame.image.load(put+'images/walk_right/3.png'),
    pygame.image.load(put+'images/walk_right/4.png'),
    pygame.image.load(put+'images/walk_right/5.png'),
    pygame.image.load(put+'images/walk_right/6.png'),
    pygame.image.load(put+'images/walk_right/7.png'),
    pygame.image.load(put+'images/walk_right/8.png'),
]

player_walk_right = [
    pygame.image.load(put+'images/walk_left/2.png'),
    pygame.image.load(put+'images/walk_left/3.png'),
    pygame.image.load(put+'images/walk_left/4.png'),
    pygame.image.load(put+'images/walk_left/5.png'),
    pygame.image.load(put+'images/walk_left/6.png'),
    pygame.image.load(put+'images/walk_left/7.png'),
    pygame.image.load(put+'images/walk_left/8.png'),
]

player_punch_right = [
    pygame.image.load(put+'images/punch/punch_right/6.png'),
    pygame.image.load(put+'images/punch/punch_right/5.png'),
    pygame.image.load(put+'images/punch/punch_right/1.png'),
    pygame.image.load(put+'images/punch/punch_right/2.png'),
    pygame.image.load(put+'images/punch/punch_right/3.png'),
    pygame.image.load(put+'images/punch/punch_right/4.png')
]

player_punch_left = [
    pygame.image.load(put+'images/punch/punch_left/6.png'),
    pygame.image.load(put+'images/punch/punch_left/5.png'),
    pygame.image.load(put+'images/punch/punch_left/1.png'),
    pygame.image.load(put+'images/punch/punch_left/2.png'),
    pygame.image.load(put+'images/punch/punch_left/3.png'),
    pygame.image.load(put+'images/punch/punch_left/4.png')
]

fura_l = pygame.image.load('images/fura/f_left.png')
fura_l_x = 1600
fura_r = pygame.image.load('images/fura/f_right.png')
fura_r_x = -200
go = False

hyzen_left = pygame.image.load(put+'images/hayzen/hayzen_left.png')
hyzen_right = pygame.image.load(put+'images/hayzen/hayzen_right.png')
hyzen_ = pygame.image.load(put+'images/hayzen/hayzen.png')
hyzen_box = pygame.image.load(put+'images/hayzen/hit_box.png')
hyzen_x = 0
hyzen_x_1 = 1520
hyzen_list = []
tymer = pygame.USEREVENT + 1
hyzen_hp_ = 1
hyzen_hp_bar_0 = 80
hyzen_hp_bar_1 = 80
hyzen_hp_bar_caunter_0 = 2
hyzen_hp_bar_caunter_1 = 2
pygame.time.set_timer(tymer,100)

boss = pygame.image.load(put + 'images/boss/the_boss.png')
boss_x = -300
boss_y = 5
boss_is = False

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,3000)

hp_boxs = []
hp_box = pygame.image.load(put + 'images/set/hp_box.png')
box_go = False
box_y = -50
random_number = random.randint(0,1550)

ship = pygame.image.load(put + 'images/set/ship.png')
ship_0_y = 690
ship_0_x = 0
up_0 = True
sh_0 = True
ship_1_y = 690
ship_1_x = 800
up_1 = False
sh_1 = False

music = pygame.mixer.Sound(put+'images/music/music.mp3')
music_key = 1

player_x = 720
player_y = 520
player_speed = 15
player_jump_is = False
player_jump_count = 20
punch = False
kills = 0

right = False
left = True
move = False

_0 = 2
_1 = 2

hp = 228

menu = 'main'

gravity = False

infinity = False

while True:

    if hp == 228:

        if menu == 'start':
            screan.blit(stat_manu,(0,0))
        elif menu == 'setting':
            screan.blit(setting_manu,(0,0))
        elif menu == 'main':
            screan.blit(main_manu,(0,0))
        elif menu == 'setting_open':
            screan.blit(setting_open__manu,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if menu == 'setting' or menu == 'main':
                        menu = 'start'
                    elif menu == 'start' or menu == 'main':
                        menu = 'setting'
                elif event.key == pygame.K_DOWN:
                    if menu == 'setting' or menu == 'main':
                        menu = 'start'
                    elif menu == 'start' or menu == 'main':
                        menu = 'setting'

                elif event.key == pygame.K_RETURN:
                    if menu == 'setting':
                        menu = 'setting_open'
                    if menu == 'start':
                        hp = 10
                        menu = 'main'
                elif event.key == pygame.K_ESCAPE:
                    if menu == 'setting_open':
                        menu = 'main'

    elif hp > 0:
        clock.tick(10)

        screan.blit(back, (back_0_x, 0))
        screan.blit(back, (back_1_x, 0))
        screan.blit(back, (back_2_x, 0))

        #фура
        screan.blit(fura_l,(fura_l_x,450))
        if fura_l_x > -100 and not boss_is:
            fura_l_x -= 40
        screan.blit(fura_r, (fura_r_x, 450))
        if fura_r_x < 1500 and not boss_is:
            fura_r_x += 40
        else:
            go = True

        player_hit_box = player_wait_right.get_rect(topleft=(player_x, player_y))
        player_platform_hitbox = player_platform_hit_box.get_rect(topleft=(player_x+15,player_y+30))

        hp_ = str(round(hp,1))
        pygame.draw.rect(screan, 'grey', (0, 7, 403, 35))
        pygame.draw.rect(screan, (13, 62, 0), (hp_bar_x, 10, 400, 30))
        text_hp_render = text.render(hp_,True,'white')
        screan.blit(text_hp_render,(60,10))
        screan.blit(text_hp, (10, 10))

        # хайзенберг
        if _0 > 0 and go:
            pygame.draw.rect(screan,'red',(hyzen_x,485,hyzen_hp_bar_0,10))
            if hyzen_x < player_x:
                hyzen_x += 3
                screan.blit(hyzen_right,(hyzen_x,500))
            elif hyzen_x > player_x:
                hyzen_x -= 3
                screan.blit(hyzen_left, (hyzen_x, 500))
            else:
                screan.blit(hyzen_,(hyzen_x,500))
            hyzen_atak_box = hyzen_box.get_rect(topleft=(hyzen_x,555))
            if hyzen_atak_box.colliderect(player_hit_box):
                hp -= 1
                hp_bar_x -= 40
                box_go = True
        hyzen_hit_box = hyzen_.get_rect(topleft=(hyzen_x,500))

        #хайзенберг_1
        if _1 > 0 and go:
            pygame.draw.rect(screan,'red',(hyzen_x_1,485,hyzen_hp_bar_1,10))
            if hyzen_x_1 < player_x:
                hyzen_x_1 += 3
                screan.blit(hyzen_right,(hyzen_x_1,500))
            elif hyzen_x_1 > player_x:
                hyzen_x_1 -= 3
                screan.blit(hyzen_left, (hyzen_x_1, 500))
            else:
                screan.blit(hyzen_,(hyzen_x_1,500))
            hyzen_atak_box_1 = hyzen_box.get_rect(topleft=(hyzen_x_1, 555))
            if hyzen_atak_box_1.colliderect(player_hit_box):
                hp -= 1
                hp_bar_x -= 40
                box_go = True
        hyzen_1_hit_box = hyzen_.get_rect(topleft=(hyzen_x_1,500))

        if _1 <= 0 and _0 <= 0 and not boss_is:
            kills += 1
            _1 = 2 + hyzen_hp_
            _0 = 2 + hyzen_hp_
            hyzen_hp_bar_0 = 80
            hyzen_hp_bar_1 = 80
            hyzen_hp_bar_caunter_0 = _0
            hyzen_hp_bar_caunter_1 = _1
            hyzen_x = 0
            hyzen_x_1 = 1520
            hyzen_hp_ = hyzen_hp_ + 1

        # коробки с приколами
        box_hit_box = hp_box.get_rect(topleft=(random_number, box_y))
        if box_go and hp < 7:
            box_y += 15
            if box_y > 600:
                box_go = False
                box_y = -30
            screan.blit(hp_box, (random_number, box_y))
            if player_hit_box.colliderect(box_hit_box):
                if hp > 5:
                    hp += 10-hp
                    hp_bar_x = 0
                    box_y = 50
                    box_go = False
                else:
                    hp += 5
                    hp_bar_x += 200
                    box_y = -50
                    box_go = False

        keys = pygame.key.get_pressed()

        #движение игрока и анимация
        if keys[pygame.K_RIGHT] and player_x < 1520:
            if boss_is:
                fura_r_x -= 4
                fura_l_x -= 4
                back_0_x -= 4
                if back_0_x == -1600 or back_0_x == 1600:
                    back_0_x = 0
                back_1_x -= 4
                if back_1_x == 0:
                    back_1_x = 1600
                back_2_x -= 4
                if back_2_x == 0:
                    back_2_x = -1600
            player_x += player_speed
            if not player_jump_is and not punch and not gravity:
                screan.blit(player_walk_left[tik_6],(player_x,player_y))
            right = True
            left = False
            move = True

        elif keys[pygame.K_LEFT] and player_x > 0:
            if boss_is:
                back_0_x += 2
                fura_l_x += 2
                fura_r_x += 2
                if back_0_x == -1600 or back_0_x == 1600:
                    back_0_x = 0
                back_1_x += 2
                if back_1_x == 0:
                    back_1_x = 1600
                back_2_x += 2
                if back_2_x == 0:
                    back_2_x = -1600

            player_x -= player_speed
            if not player_jump_is and not punch and not gravity:
                screan.blit(player_walk_right[tik_6], (player_x, player_y))
            right = False
            left = True
            move = False

        # punch
        elif keys[pygame.K_f] and not player_jump_is and not gravity:
            move = False
            if right:
                # нервный тик
                if tik_3 == 5:
                    tik_3 = 0
                else:
                    tik_3 += 1
                screan.blit(player_punch_right[tik_3], (player_x, player_y))
                if tik_3 == 4:
                    screan.blit(punch_efekt_1,(player_x+80,player_y+35))
                    punch_hit_box_1 = punch_efekt_1.get_rect(topleft=(player_x+80,player_y+35))
                    if punch_hit_box_1.colliderect(hyzen_hit_box):
                        hyzen_hp_bar_0 -= (80//hyzen_hp_bar_caunter_0)
                        _0 -= 1
                    if punch_hit_box_1.colliderect(hyzen_1_hit_box):
                        _1 -= 1
                        hyzen_hp_bar_1 -= (80//hyzen_hp_bar_caunter_1)
            if left:
                # нервный тик
                if tik_3 == 5:
                    tik_3 = 0
                else:
                    tik_3 += 1
                screan.blit(player_punch_left[tik_3],(player_x,player_y))
                if tik_3 == 4:
                    screan.blit(punch_efekt,(player_x-35,player_y+35))
                    punch_hit_box = punch_efekt.get_rect(topleft=(player_x-35,player_y+35))
                    if punch_hit_box.colliderect(hyzen_hit_box):
                        _0 -= 1
                        hyzen_hp_bar_0 -= (80//hyzen_hp_bar_caunter_0)
                    if punch_hit_box.colliderect(hyzen_1_hit_box):
                        _1 -= 1
                        hyzen_hp_bar_1 -= (80//hyzen_hp_bar_caunter_1)
        elif not player_jump_is and not gravity:
            move = False
            if right:
                screan.blit(player_wait_right,(player_x,player_y))
            elif left:
                screan.blit(player_wait_left,(player_x,player_y))

        #большой босс
        if kills == 3 and not infinity:
            print(boss_x)
            ship_0 = ship.get_rect(topleft=(ship_0_x,ship_0_y))
            if ship_0.colliderect(player_hit_box):
                hp_bar_x -= 4
                hp -= 0.1
            screan.blit(ship, (ship_0_x, ship_0_y))
            ship_1 = ship.get_rect(topleft=(ship_1_x,ship_1_y))
            if ship_1.colliderect(player_hit_box):
                hp -= 0.1
                hp_bar_x -= 4
            screan.blit(ship, (ship_1_x, ship_1_y))
            if not up_1:
                if up_0:
                    if ship_0_y >= 580 and sh_0:
                        ship_0_y -= 20
                        sh_0 = True
                    else:
                        sh_0 = False
                        ship_0_y += 10
                        if ship_0_y == 690:
                            sh_0 = True
                            up_0 = False
                            up_1 = True
                            sh_1 = True
            if not up_0:
                if up_1:
                    if ship_1_y >= 580 and sh_1:
                        ship_1_y -= 20
                        sh_1 = True
                    else:
                        sh_1 = False
                        ship_1_y += 10
                        if ship_1_y == 690:
                            sh_1 = True
                            up_1 = False
                            up_0 = True
                            sh_0 = True
            boss_x += 5
            boss_hit_box = boss.get_rect(topleft=(boss_x-30,boss_y))
            if boss_hit_box.colliderect(player_hit_box):
                hp -= 10
            screan.blit(boss, (boss_x, boss_y))
            if not move:
                boss_x += 2
            elif move and boss_x >= 0:
                boss_x -= 4
            boss_is = True
            _1 = False
            _0 = False

        if boss_x >= 1200 and not infinity:
            _1 = False
            _0 = False
            kills = 4
            screan.blit(boss,(boss_x,boss_y))
            screan.blit(piece,(boss_x+50,piece_y))
            if piece_y <= 420:
                piece_y += 150
            else:
                boss_y += 100
                if piece_y <= 600:
                    piece_y += 100
            if boss_y >= 6000:
                hp = -52

        #прыжки
        if not player_jump_is and not gravity:
            if keys[pygame.K_SPACE]:
                player_jump_is = True
        if player_jump_is:
            player_jump_is_ = False
            if player_jump_count >= -20:
                if player_y == 0:
                    move = False
                    player_y += player_jump_count
                else:
                    move = False
                    player_y -= player_jump_count
                player_jump_count -= 2
                if right:
                    move = False
                    screan.blit(player_jump_right,(player_x,player_y))
                elif left:
                    move = False
                    screan.blit(player_jump_left,(player_x,player_y))
                else:
                    move = False
                    screan.blit(player_jump_right, (player_x, player_y))

            else:
                player_jump_is_ = True
                player_jump_is = False
                player_jump_count = 20

        #время для анимки
        if tik_6 == 6:
            tik_6 = 0
        else:
            tik_6 += 1

        platforma_hit_box = platforma.get_rect(topleft=(platforma_x, platforma_y))

        # гравитация
        if player_y < 520 and not player_jump_is:
            player_y += 10
            if gravity:
                if right:
                    screan.blit(player_jump_right, (player_x, player_y))
                elif left:
                    screan.blit(player_jump_left, (player_x, player_y))
            gravity = True
        else:
            gravity = False

        # всякое
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    hp = 0
                elif event.key == pygame.K_m:
                    if music_key % 2 == 0:
                        music.stop()
                        music_key += 1
                    else:
                        music.play()
                        music_key += 1
            elif boss_is:
                if event.type == timer:
                    platforma_list.append(platforma_hit_box)

        if platforma_list:
            for el in platforma_list:
                screan.blit(platforma,el)
                el.x -= 15
                platforma_hit_box = platforma.get_rect(topleft=(el.x,el.y))
                if platforma_hit_box.colliderect(player_hit_box):
                    if not keys[pygame.K_SPACE]:
                        gravity = False
                        player_jump_is = False
                    player_jump_count = 20
                    if not player_jump_is:
                        player_y = 390
                    if player_x > 0 and player_x < 1500:
                        player_x -= 15

    elif hp == -52:
        screan.blit(win,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    infinity = True
                    hp = 10
                    player_x = 720
                    player_y = 520
                    player_speed = 15
                    player_jump_is = False
                    player_jump_count = 20
                    punch = False
                    hp_bar_x = 0

                    boss_is = False
                    boss_x = -300

                    right = False
                    left = True

                    fura_r_x = 1500
                    fura_l_x = -100

                    _0 = 2
                    _1 = 2
                    hyzen_x = 0
                    hyzen_x_1 = 1520
                    hyzen_hp_bar_0 = 80
                    hyzen_hp_bar_1 = 80
                    hyzen_hp_bar_caunter_0 = _0
                    hyzen_hp_bar_caunter_1 = _1
                    hyzen_hp_ = 1
                    kills = 0

                    platforma_list.clear()

                elif event.key == pygame.K_r:
                    hp = 10
                    player_x = 720
                    player_y = 520
                    player_speed = 15
                    player_jump_is = False
                    player_jump_count = 20
                    punch = False
                    hp_bar_x = 0

                    boss_is = False
                    boss_x = -300
                    boss_y = 5

                    right = False
                    left = True

                    fura_r_x = 1500
                    fura_l_x = -100

                    _0 = 2
                    _1 = 2
                    hyzen_x = 0
                    hyzen_x_1 = 1520
                    hyzen_hp_bar_0 = 80
                    hyzen_hp_bar_1 = 80
                    hyzen_hp_bar_caunter_0 = _0
                    hyzen_hp_bar_caunter_1 = _1
                    hyzen_hp_ = 1
                    kills = 0

                    platforma_list.clear()

    else:
        screan.blit(end,(0,0))
        t_kills = str(kills)
        text_kills_count = text.render(t_kills,True,'red')
        screan.blit(text_kills_count,(210,13))
        screan.blit(text_kills,(10,10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    hp = 10
                    player_x = 720
                    player_y = 520
                    player_speed = 15
                    player_jump_is = False
                    player_jump_count = 20
                    punch = False
                    hp_bar_x = 0

                    boss_is = False
                    boss_x = -300

                    right = False
                    left = True

                    fura_r_x = 1500
                    fura_l_x = -100

                    _0 = 2
                    _1 = 2
                    hyzen_x = 0
                    hyzen_x_1 = 1520
                    hyzen_hp_bar_0 = 80
                    hyzen_hp_bar_1 = 80
                    hyzen_hp_bar_caunter_0 = _0
                    hyzen_hp_bar_caunter_1 = _1
                    hyzen_hp_ = 1
                    kills = 0

                    platforma_list.clear()

    pygame.display.update()