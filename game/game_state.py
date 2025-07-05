"""
Gerenciamento do estado do jogo Space Defender
"""

import pygame
import math
from .player import Player
from .asteroid import AsteroidManager
from .utils import load_sound, create_explosion_particles, distance

class GameState:
    def __init__(self, screen):
        """
        Inicializa o estado do jogo
        
        Args:
            screen: Superfície principal do pygame
        """
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # Estados do jogo
        self.state = "MENU"  # MENU, PLAYING, GAME_OVER
        self.should_quit = False
        
        # Jogador
        self.player = Player(self.screen_width // 2, self.screen_height - 100,
                           self.screen_width, self.screen_height)
        
        # Asteroides
        self.asteroid_manager = AsteroidManager(self.screen_width, self.screen_height)
        
        # Pontuação
        self.score = 0
        self.high_score = 0
        
        # Efeitos visuais
        self.particles = []
        
        # Sons
        self.explosion_sound = load_sound("assets/sounds/explosion.wav")
        self.hit_sound = load_sound("assets/sounds/hit.wav")
        
        # Fonte para texto
        pygame.font.init()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
        # Timer para controles
        self.last_key_time = 0
        self.key_delay = 0.2  # segundos entre comandos de menu
    
    def handle_event(self, event):
        """
        Processa eventos do jogo
        
        Args:
            event: Evento do pygame
        """
        current_time = pygame.time.get_ticks() / 1000.0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.should_quit = True
            
            elif self.state == "MENU":
                if event.key == pygame.K_SPACE and current_time - self.last_key_time > self.key_delay:
                    self.start_game()
                    self.last_key_time = current_time
            
            elif self.state == "GAME_OVER":
                if event.key == pygame.K_r and current_time - self.last_key_time > self.key_delay:
                    self.restart_game()
                    self.last_key_time = current_time
                elif event.key == pygame.K_SPACE and current_time - self.last_key_time > self.key_delay:
                    self.state = "MENU"
                    self.last_key_time = current_time
    
    def start_game(self):
        """Inicia uma nova partida"""
        self.state = "PLAYING"
        self.score = 0
        self.player.lives = 3
        self.player.reset_position()
        self.asteroid_manager.clear()
        self.particles.clear()
    
    def restart_game(self):
        """Reinicia o jogo após game over"""
        self.start_game()
    
    def update(self):
        """Atualiza a lógica do jogo"""
        dt = 1/60  # Assume 60 FPS para simplicidade
        
        if self.state == "PLAYING":
            self.update_playing(dt)
        elif self.state == "MENU":
            self.update_menu(dt)
        elif self.state == "GAME_OVER":
            self.update_game_over(dt)
    
    def update_playing(self, dt):
        """Atualiza o jogo durante o estado PLAYING"""
        keys = pygame.key.get_pressed()
        
        # Atualiza jogador
        self.player.update(dt, keys)
        
        # Atualiza asteroides
        self.asteroid_manager.update(dt)
        
        # Verifica colisões entre projéteis e asteroides
        self.check_bullet_asteroid_collisions()
        
        # Verifica colisões entre jogador e asteroides
        self.check_player_asteroid_collisions()
        
        # Atualiza partículas
        self.update_particles(dt)
        
        # Verifica game over
        if not self.player.is_alive():
            self.state = "GAME_OVER"
            if self.score > self.high_score:
                self.high_score = self.score
    
    def update_menu(self, dt):
        """Atualiza o menu"""
        # Atualiza partículas de fundo se houver
        self.update_particles(dt)
    
    def update_game_over(self, dt):
        """Atualiza a tela de game over"""
        # Atualiza partículas
        self.update_particles(dt)
    
    def check_bullet_asteroid_collisions(self):
        """Verifica colisões entre projéteis e asteroides"""
        bullets = self.player.get_bullets()
        asteroids = self.asteroid_manager.get_asteroids()
        
        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                if asteroid.collides_with(bullet.rect, bullet.radius):
                    # Remove projétil e asteroide
                    self.player.remove_bullet(bullet)
                    self.asteroid_manager.remove_asteroid(asteroid)
                    
                    # Adiciona pontuação
                    self.score += asteroid.points
                    
                    # Cria explosão
                    self.create_explosion(asteroid.x, asteroid.y)
                    
                    # Toca som de explosão
                    if self.explosion_sound:
                        self.explosion_sound.play()
                    
                    # Divide asteroide se for grande
                    fragments = asteroid.split()
                    for fragment in fragments:
                        self.asteroid_manager.add_asteroid(fragment)
                    
                    break  # Sai do loop interno
    
    def check_player_asteroid_collisions(self):
        """Verifica colisões entre jogador e asteroides"""
        asteroids = self.asteroid_manager.get_asteroids()
        
        for asteroid in asteroids[:]:
            if asteroid.collides_with(self.player.rect, 15):  # Raio do jogador
                if self.player.take_damage():
                    # Remove asteroide
                    self.asteroid_manager.remove_asteroid(asteroid)
                    
                    # Cria explosão
                    self.create_explosion(asteroid.x, asteroid.y)
                    
                    # Toca som de hit
                    if self.hit_sound:
                        self.hit_sound.play()
                    
                    break
    
    def create_explosion(self, x, y):
        """Cria efeito de explosão"""
        new_particles = create_explosion_particles((x, y), 15)
        self.particles.extend(new_particles)
    
    def update_particles(self, dt):
        """Atualiza partículas de efeitos visuais"""
        for particle in self.particles[:]:
            # Atualiza posição
            particle['pos'][0] += particle['velocity'][0] * dt
            particle['pos'][1] += particle['velocity'][1] * dt
            
            # Reduz vida
            particle['life'] -= dt
            
            # Remove partículas mortas
            if particle['life'] <= 0:
                self.particles.remove(particle)
    
    def draw(self):
        """Desenha tudo na tela"""
        if self.state == "MENU":
            self.draw_menu()
        elif self.state == "PLAYING":
            self.draw_playing()
        elif self.state == "GAME_OVER":
            self.draw_game_over()
        
        # Sempre desenha partículas por último
        self.draw_particles()
    
    def draw_menu(self):
        """Desenha o menu principal"""
        # Título
        title = self.font_large.render("SPACE DEFENDER", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen_width // 2, 200))
        self.screen.blit(title, title_rect)
        
        # Instruções
        instructions = [
            "Proteja a Terra dos asteroides!",
            "",
            "Controles:",
            "Setas ou WASD - Mover",
            "Espaço - Atirar",
            "",
            "Pressione ESPAÇO para jogar",
            "ESC para sair"
        ]
        
        y = 280
        for instruction in instructions:
            if instruction:  # Pula linhas vazias
                text = self.font_small.render(instruction, True, (200, 200, 200))
                text_rect = text.get_rect(center=(self.screen_width // 2, y))
                self.screen.blit(text, text_rect)
            y += 30
        
        # High score
        if self.high_score > 0:
            high_score_text = self.font_medium.render(f"Recorde: {self.high_score}", True, (255, 255, 0))
            high_score_rect = high_score_text.get_rect(center=(self.screen_width // 2, 500))
            self.screen.blit(high_score_text, high_score_rect)

    def draw_playing(self):
        """Desenha o jogo em andamento"""
        # Desenha asteroides
        self.asteroid_manager.draw(self.screen)

        # Desenha jogador
        self.player.draw(self.screen)

        # HUD - Pontuação
        score_text = self.font_medium.render(f"Pontos: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # HUD - Vidas
        lives_text = self.font_medium.render(f"Vidas: {self.player.lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 50))

        # HUD - Instruções
        if self.score == 0:  # Mostra apenas no início
            help_text = self.font_small.render("Use setas/WASD para mover, ESPAÇO para atirar", True, (150, 150, 150))
            help_rect = help_text.get_rect(center=(self.screen_width // 2, self.screen_height - 30))
            self.screen.blit(help_text, help_rect)

    def draw_game_over(self):
        """Desenha a tela de game over"""
        # Fundo semi-transparente
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Texto principal
        game_over_text = self.font_large.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, 200))
        self.screen.blit(game_over_text, game_over_rect)

        # Pontuação final
        score_text = self.font_medium.render(f"Pontuação Final: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.screen_width // 2, 280))
        self.screen.blit(score_text, score_rect)

        # Novo recorde
        if self.score == self.high_score and self.high_score > 0:
            new_record_text = self.font_medium.render("NOVO RECORDE!", True, (255, 255, 0))
            new_record_rect = new_record_text.get_rect(center=(self.screen_width // 2, 320))
            self.screen.blit(new_record_text, new_record_rect)

        # Instruções
        restart_text = self.font_small.render("Pressione R para jogar novamente", True, (200, 200, 200))
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, 400))
        self.screen.blit(restart_text, restart_rect)

        menu_text = self.font_small.render("Pressione ESPAÇO para voltar ao menu", True, (200, 200, 200))
        menu_rect = menu_text.get_rect(center=(self.screen_width // 2, 430))
        self.screen.blit(menu_text, menu_rect)

    def draw_particles(self):
        """Desenha partículas de efeitos visuais"""
        for particle in self.particles:
            # Calcula alpha baseado na vida restante
            alpha = int(255 * (particle['life'] / particle['max_life']))
            alpha = max(0, min(255, alpha))

            # Cria superfície com alpha
            size = max(1, int(4 * (particle['life'] / particle['max_life'])))
            particle_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)

            # Cor com alpha
            color = (*particle['color'], alpha)
            pygame.draw.circle(particle_surface, color, (size, size), size)

            # Desenha na tela
            pos = (int(particle['pos'][0] - size), int(particle['pos'][1] - size))
            self.screen.blit(particle_surface, pos)
