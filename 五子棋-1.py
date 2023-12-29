import pygame
import os
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((511,800))#畫面大小
pygame.display.set_caption("五子棋")#標題
clock=pygame.time.Clock()
#圖片導入
back = pygame.image.load(os.path.join("未命名的作品.png")).convert()
white = pygame.image.load(os.path.join("五子棋-圖片", "白棋.png")).convert()
black = pygame.image.load(os.path.join("五子棋-圖片", "黑棋.png")).convert()
B_wins = pygame.image.load(os.path.join("五子棋-圖片", "黑棋獲勝.png")).convert()
W_wins = pygame.image.load(os.path.join("五子棋-圖片", "白棋獲勝.png")).convert()
tie = pygame.image.load(os.path.join("五子棋-圖片", "平手.png")).convert()

font_name = os.path.join("font.ttf")#文字框
def draw_text(surf, text, size, x, y):#畫面 文字 大小 座標
    font = pygame.font.Font(font_name, size)#字體字體 大小
    text_surface = font.render(text, True, 640)
    text_rect = text_surface.get_rect()
    text_rect.center = x,y
    surf.blit(text_surface, text_rect)

def lines():
    for k in range(1,3):
        for j in range(15):#-方向連線
            for first in range(11):
                p=0
                for i in range(first,first+5):
                    if block[j][i]==k:
                        p+=1
                    if p==5:
                        win[0]=k
                        line_check[0]=0
                        line_check[1]=i-4
                        line_check[2]=j
                        break
                if p==5:
                    break
            if p==5:
                break
        if p==5:
            break
        for i in range(15):#|方向連線
            for first in range(11):
                p=0
                for j in range(first,first+5):
                    if block[j][i]==k:
                        p+=1
                    if p==5:
                        win[0]=k
                        line_check[0]=1
                        line_check[1]=i
                        line_check[2]=j-4
                        break
                if p==5:
                    break
            if p==5:
                break    
        if p==5:
            break    
        for firstx in range(11):#\方向連線
            for firsty in range(11):
                p=0
                for i in range(firstx,firstx+5):
                    j=i+firsty-firstx
                    if block[i][j]==k:
                        p+=1
                    if p==5:
                        win[0]=k
                        line_check[0]=2
                        line_check[1]=j-4
                        line_check[2]=i-4

        for firstx in range(11):#/方向連線
            for firsty in range(4,15):
                p=0
                for i in range(firstx,firstx+5):
                    j=firsty-i+firstx
                    if block[i][j]==k:
                        p+=1
                    if p==5:
                        win[0]=k
                        line_check[0]=3
                        line_check[1]=j+4
                        line_check[2]=i-4
class player1(pygame.sprite.Sprite):#黑棋.棋子物件
    def __init__(self , x , y ):
        pygame.sprite.Sprite.__init__(self)
        self.image=black
        self.image.set_colorkey((248,228,191))
        self.image=pygame.transform.scale(self.image,(31,31))
        self.rect = self.image.get_rect()
        self.rect.left=(x*34)+2
        self.rect.top=(y*34)+151

class player2(pygame.sprite.Sprite):#白棋.棋子物件
    def __init__(self , x , y ):
        pygame.sprite.Sprite.__init__(self)
        self.image=white
        self.image.set_colorkey((248,228,191))
        self.image=pygame.transform.scale(self.image,(31,31))
        self.rect = self.image.get_rect()
        self.rect.left=(x*34)+2
        self.rect.top=(y*34)+151

class Bwin_back(pygame.sprite.Sprite):#黑棋贏
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=B_wins
        self.rect = self.image.get_rect()
        self.rect.centerx=256
        self.rect.centery=300
class Wwin_back(pygame.sprite.Sprite):#白棋贏
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=W_wins
        self.rect = self.image.get_rect()
        self.rect.centerx=256
        self.rect.centery=300
class tie_back(pygame.sprite.Sprite):#平手
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=tie
        self.rect = self.image.get_rect()
        self.rect.centerx=256
        self.rect.centery=300
pic=pygame.sprite.Group()#棋子群組
win_backs=pygame.sprite.Group()#輸贏背景群組
running=True#整體遊戲迴圈

while running:
    #棋盤，0空1黑2白
    block=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
    #block=[[1,2,1,2,1,2,1,2,1,2,1,2,1,2,1],
    #[2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    #[1,2,2,1,2,1,2,1,2,1,2,1,2,2,1],
    #[2,1,1,1,2,1,2,1,2,1,2,1,1,1,2],
    #[1,2,2,2,1,2,1,2,1,2,1,2,2,2,1],
    #[2,1,1,1,2,2,1,2,1,2,2,1,1,1,2],
    #[1,2,2,2,1,1,2,1,2,1,1,2,2,2,1],
    #[2,1,1,1,2,2,1,0,1,2,2,1,1,1,2],
    #[1,2,2,2,1,1,2,1,2,1,1,2,2,2,1],
    #[2,1,1,1,2,2,1,2,1,2,2,1,1,1,2],
    #[1,2,2,2,1,2,1,2,1,2,1,2,2,2,1],
    #[2,1,1,1,2,1,2,1,2,1,2,1,1,1,2],
    #[1,2,2,1,2,1,2,1,2,1,2,1,2,2,1],
    #[2,1,2,1,2,1,2,1,2,1,2,1,2,1,2],
    #[1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]]
    user=0#確認換哪位玩家 0黑1白
    line_check=[-1,-1,-1]#連線方式，起始格子(a,b)

    win=[0,255]#(空.黑.白.平),棋子數
    while (win[0]==0)|(win[1]!=0):#沒棋子或有人贏時，離開迴圈
        clock.tick(60)
        screen.blit(back, (0,0))#背景
        pic.draw(screen)#畫棋子
        if user==0:
            draw_text(screen, '現在輪到黑棋', 20,170,125)
        else:
            draw_text(screen, '現在輪到白棋', 20,341,125)
        pygame.display.update()
        x=0
        y=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x,mouse_y = event.pos
                #print(mouse_x,mouse_y)
                #每隔棋格34像素
                x=(mouse_x-2)//34
                y=(mouse_y-151)//34
                if (0<=x & x<=14 )&( 0<=y & y<=14):
                    if block[y][x]==0:
                        if user==0:
                            block[y][x]=1#下黑棋
                            user=1
                        else:
                            block[y][x]=2#下白棋
                            user=0
                        win[1]-=1
                        if win[1]==0:#平手判斷
                            win[0]=3
                        #for j in range(15):
                        #    print(block[j][0],block[j][1],block[j][2],block[j][3],block[j][4],block[j][5],block[j][6],block[j][7],block[j][8],block[j][9],block[j][10],block[j][11],block[j][12],block[j][13],block[j][14])
                        #print("剩餘棋子數",win[1])
                        pic.empty()#清空群組內棋子
                        for i in range(15):#重新將棋子加入
                            for j in range(15):
                                if block[j][i]==1:
                                    a=player1(i,j)
                                    pic.add(a)
                                if block[j][i]==2:
                                    a=player2(i,j)
                                    pic.add(a)
                        lines()#連線判斷
                        if win[0]!=0:#有人贏，則棋子數變為0
                            win[1]=0
                        pic.draw(screen)#將棋子群組畫在畫面上
                        pygame.display.update()#更新畫面
    #結束畫面
    checking = True#連線確認畫面
    wining = True#勝負畫面
    
    #刷新掉輪到誰的顯示
    screen.blit(back, (0,0))#背景重置
    pic.draw(screen)#畫棋子

    while wining:#連線
        if win[0]==1:#黑棋贏
            a=Bwin_back()
            win_backs.add(a)
            win_backs.draw(screen)
        elif win[0]==2:#白棋贏
            a=Wwin_back()
            win_backs.add(a)
            win_backs.draw(screen)
        else:#平手
            a=tie_back()
            win_backs.add(a)
            win_backs.draw(screen)
        draw_text(screen, '點擊畫面查看棋盤', 45,256,120)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                wining = False
                win_backs.empty()#使輸贏顯示背景消失
        
    while checking:#連線
        if line_check[0]==1:#53行
            a=line_check[1]*34+17
            b=(line_check[2]+4)*34+166
        elif line_check[0]==0:#35行
            a=(line_check[1]+4)*34+17
            b=line_check[2]*34+166
        elif line_check[0]==2:#72行
            a=(line_check[1]+4)*34+17
            b=(line_check[2]+4)*34+166
        elif line_check[0]==3:#85行
            a=(line_check[1]-4)*34+17
            b=(line_check[2]+4)*34+166
        color=(255,0,0)
        width=11
        screen.blit(back, (0,0))
        pic.draw(screen)
        if win[0]!=3:#將連線畫出
            pygame.draw.line(screen,color,(line_check[1]*34+17,line_check[2]*34+166),(a,b),width)
        draw_text(screen, '再次點擊畫面重啟遊戲', 30,256,120)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                checking = False
                waiting = False

    pic.empty()

    #screen.fill((255,255,255))
    #a=win_back((64,110+39+75))
    #pic.add(a)
    #pygame.display.update()
    # 取得輸入


    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        pygame.quit()
    #    elif event.type == MOUSEBUTTONDOWN:
    #        waiting = False
pygame.quit()