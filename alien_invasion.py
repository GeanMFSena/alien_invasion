import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import random as rd
from stars import Stars
from time import sleep
from game_stats import GameStats
from button import Button


class AlienInvasion:
    '''Classe geral para gerenciar ativos e comportamento do jogo'''
    
    def __init__(self):
        '''Inicializa e cria os arquivos do jogo'''
        pygame.init()
        self.active_game = False
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        # self.creat_fleet_stars()    
        self._create_fleet()
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        
        
    def run_game(self):
        '''Inicializa o loop principal do jogo'''
        while True:
            self._chec_events()
            if self.active_game:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
        
            
            
            
    def _chec_events(self):  
        # observa os eventos do teclado e do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._chec_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._chec_events_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            
                
    def _check_play_button(self,mouse_pos):
        '''inicia o jogo novo quando o jogador clica em play '''
        
        click_button = self.play_button.rect.collidepoint(mouse_pos)
        if click_button and not self.active_game :
            #redefine as estatisticas do jogo 
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()
            self.active_game = True
            
            # descarta projeteis e alienigenas
            self.bullet.empty()
            self.aliens.empty()
            
            # cria uma nova frota de aliens e centraliza a espaconave novamente
            self._create_fleet()
            self.ship.center_ship()
            
            # esconde o cursor do mouse
            pygame.mouse.set_visible(False)
            
            
    
    def _chec_events_keydown(self,event):  
        '''Responde as teclas pressionadas'''
        if event.key == pygame.K_RIGHT:
        # move a espaconave para a direita
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
        # move a espaconave para a esquerda
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
        elif event.key == pygame.K_p:
            self._check_play_button()

    def fire_bullets(self):
        '''cria um novo projetil e o adiciona ao grupo projeteis '''
        if len(self.bullet) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)
    
    def _update_bullets(self):
        self.bullet.update()
        # descarta os projeteis que desapareceram
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)
        self._check_bullet_collision()
        

                
    def _check_bullet_collision(self):
        # Verifica se um projetil atingiu um alienigena 
        # Se sim, descarta o projetil e o alienigena
        collisions = pygame.sprite.groupcollide(self.bullet,self.aliens,True,True)   
        # verifica se tem algum alienigena no grupo de alienigenas 
        # se for True apaga todos os sprites das balas e cria novos alienigenas 
        if not self.aliens:
            self.bullet.empty()
            self._create_fleet()
            self.settings.incrase_speed()
    
    def _update_aliens(self):
        self._check_fleet_direction()
        self.aliens.update()   
        # detecta colisoes entre alienigenas e espaconaves 
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        self._check_aliens_bottom()
        
        
    def ship_hit(self):
        '''Responde a espaconave sendo abatida por um alienigena'''
        # decrementa ship_left
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1 
            # descarta qualquer alienigena e bala restante 
            self.aliens.empty()
            self.bullet.empty()
            # cria uma nova frota de alienigenas e reposiciona a nava no meio denovo 
            self._create_fleet()
            self.ship.center_ship()
            # pausa o jogo 
            sleep(0.5)
        else:
            self.active_game = False
            pygame.mouse.set_visible(True)

        
    def _check_aliens_bottom(self):
        '''Verifica se um alien chegou a borda da tela e se sim reinicia o loop'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                '''Volta o loop como se a nava tivesse sido abatida '''
                self.ship_hit
                break

                                          
    def _chec_events_keyup(self, event):
                    '''Responde as teclas soltas'''
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                        
    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
            
            current_x = alien_width
            current_y += 2 * alien_height                
    
    def _create_alien(self,x_position,y_position):
        '''Cria a frota de alienigenas '''
        # cria um alienigena e continua adicionando alienigenas 
        # o distanciamento entre os alienigenas e a largura dos mesmos        
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        

            
    def _check_fleet_direction(self):
        '''Responde se algum alienigena chegou a borda da tela'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._changes_fleet_direction()
                break
            
    def _changes_fleet_direction(self):
        '''Faz toda frota descer e mudar de direcao '''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 
        
        
    # def creat_fleet_stars(self):
    #     star = Stars(self)
    #     star_width, star_height = star.rect.size
        
    #     star_current_x, star_current_y = star_width, star_height
        
    #     while star_current_y < (self.settings.screen_height - 3 * star_height):
    #         while star_current_x < (self.settings.screen_width - 2 * star_width):
    #             self._create_star(rd.randint(1,1200),rd.randint(1,800))
    #             star_current_x += 2 * star_width
            
    #         star_current_x = star_width
    #         star_current_y += 2 * star_height
        
    # def _create_star(self,x_position,y_position):
    #     '''Cria as estrelas no fundo'''
    #     new_star = Stars(self)
    #     new_star.x = x_position
    #     new_star.rect.x = x_position
    #     new_star.rect.y = y_position
    #     self.stars.add(new_star)
                    
    def _update_screen(self):
        # redesenha a tela durante cada passagem pelo loop
        self.screen.fill(self.settings.bg_color)  
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        self.ship.blitme() 
        self.aliens.draw(self.screen)
        # self.stars.draw(self.screen)
        # Deixa a tela desenhada mais recente visivel
        if self.active_game == False:
            self.play_button.drawn_button()
        pygame.display.flip()

                
if __name__ == '__main__':
# cria uma instancia do jogo e executa o jogo
    ai = AlienInvasion()
    ai.run_game()
        