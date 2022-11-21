import pygame


def main():
   pygame.init() # 初始化所有模块
   FPSCLOCK = pygame.time.Clock() # 创建时钟对象
   WINSET = pygame.display.set_mode((640, 480)) # 创建窗体
   imge1 = pygame.image.load('bg.jpg') # 导入图片文件
   WINSET.blit(imge1,(0, 0)) #绘制图形
   BASICFONT = pygame.font.Font('STKAITI.TTF', 24)
   msgSurf1= BASICFONT.render('初始化……', True, (3, 54, 73), (255, 255, 193))
   msgSurf2= BASICFONT.render('上一步', True, (3, 54, 73), (255, 255, 193))
   msgSurf3= BASICFONT.render('游戏模式', True, (3, 54, 73), (255, 255, 193))
   msgSurf4= BASICFONT.render('重启', True, (3, 54, 73), (255, 255, 193))
   WINSET.blit(msgSurf1, (0, 0))
   WINSET.blit(msgSurf2, (540, 230))
   WINSET.blit(msgSurf3, (518, 330))
   WINSET.blit(msgSurf4, (564, 430))
   pygame.display.set_caption("推盘游戏") # 设置标题
   pygame.display.update() # 刷新窗口
   i = 0
   while True:
       i += 1
       print(i)
       FPSCLOCK.tick(1)

   pygame.quit() #退出所有模块，卸载所有模块

if __name__ == '__main__':
   main()