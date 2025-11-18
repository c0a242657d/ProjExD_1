import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flipped = pg.transform.flip(bg_img, True, False)#問題８
    kokaton_img = pg.image.load("fig/3.png")#問題３
    kokaton_img = pg.transform.flip(kokaton_img, True, False)#問題３
    koukaton_rect = kokaton_img.get_rect()#問題１０
    koukaton_rect.center = 300, 200#問題１０
   
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr % 3200 # 練習５・９
        screen.blit(bg_img, [-x, 0]) # 練習５
        screen.blit(bg_img_flipped, [-x+1600, 0]) # 練習７
        screen.blit(bg_img, (-x + 3200, 0))#問題８
        screen.blit(kokaton_img,koukaton_rect)#問題４
        pg.display.update()
        tmr += 1        
        clock.tick(200)

        key_list = pg.key.get_pressed()#問題１０
        kx = -1
        ky = 0
        
        if key_list[pg.K_UP]:#問題１０
            ky=-1
        if key_list[pg.K_DOWN]:#問題１０
            ky=1
        if key_list[pg.K_LEFT]:#問題１０
            kx-=1
        if key_list[pg.K_RIGHT]:#問題１０
            kx+=2
        koukaton_rect.move_ip(kx, ky)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()