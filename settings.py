'''Classe que armazena as configuracoes gerais do jogo'''

class Settings:
    
    def __init__(self):
        '''inicializa as configuracoes do jogo'''
        
        # configuracoes da janela do jogo  
        self.screen_width = 1200
        self.screen_hight = 800
        
        # define a cor de background da janela do jogo
        self.bg_color = (230,230,230)
        self.bg_color_blue_sky = (0,169,251)
        
        # define a velocidade da espaconave 
        self.ship_speed = 1.5