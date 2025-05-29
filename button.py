import pygame.font

class Button:
#这里是游戏中的按钮喔！

    def __init__(self,QI_game,msg):
        #初始化按钮的属性
        self.screen = QI_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #设置按钮的属性和其他属性
        self.width,self.height = 200, 50
        self.button_color = (80,80,80)
        self.text_color = (255,255,255)
        self.font =pygame.font.SysFont(None,48)
        
        #创建按钮的rect对象并使其居中(将按钮的center属性设置为屏幕的center属性)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        #Pygame处理文本的方式是，将要显示的字符串渲染为图像，
        #最后再调用_prep_mag()来处理这样的渲染
        #按钮的标签只需要创建一次
        self._prep_msg(msg)
    
    def _prep_msg(self,msg):
        #将msg渲染为图像，并使其在按钮上居中
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        #_prep_msg方法接受实参self以及要渲染为图像的文本（msg），
        #我们在其中调用font.render()将存储在msg中的文本转换为图像，
        #再将该图像存储至self.msg_image中
        #font.render()方法还接受一个布尔实参，该实参指定是否开启反锯齿功能
        #余下两个实参分别为文本的颜色与背景色（没有指定背景色则渲染
        #文本时将使用透明的背景
       
    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

        