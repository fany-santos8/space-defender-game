"""
Classe do jogador para o jogo Space Defender
"""

import pygame
import math
from .utils import create_ship_sprite, create_bullet_sprite, load_sound
from .bullet import Bullet

class Player:
    def __init__(self, x, y, screen_width, screen_height):
        """
        Inicializa o jogador
        
        Args:
            x (int): Posição inicial X
            y (int): Posição inicial Y
            screen_width (int): Largura da tela
            screen_height (int): Altura da tela
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Posição e movimento
        self.x = x
        self.y = y
        self.speed = 300  # pixels por segundo
        
        # Sprite
        self.sprite = create_ship_sprite((40, 30))
        self.rect = self.sprite.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        # Sistema de tiro
        self.bullets = []
        self.shoot_cooldown = 0.2  # segundos entre tiros
        self.last_shot = 0
        
        # Sons
        self.shoot_sound = load_sound("assets/sounds/shoot.wav")
        
        # Vidas
        self.lives = 3
        self.invulnerable = False
        self.invulnerable_time = 0
        self.invulnerable_duration = 2.0  # segundos de invulnerabilidade após hit
        
    def update(self, dt, keys):
        """
        Atualiza o jogador
        
        Args:
            dt (float): Delta time em segundos
            keys: Estado das teclas pressionadas
        """
        # Movimento
        dx = 0
        dy = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.speed * dt
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= self.speed * dt
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += self.speed * dt
        
        # Aplica movimento
        self.x += dx
        self.y += dy
        
        # Mantém dentro da tela
        self.x = max(self.rect.width // 2, 
                    min(self.x, self.screen_width - self.rect.width // 2))
        self.y = max(self.rect.height // 2, 
                    min(self.y, self.screen_height - self.rect.height // 2))
        
        # Atualiza rect
        self.rect.centerx = self.x
        self.rect.centery = self.y
        
        # Sistema de tiro
        current_time = pygame.time.get_ticks() / 1000.0
        if keys[pygame.K_SPACE] and current_time - self.last_shot > self.shoot_cooldown:
            self.shoot()
            self.last_shot = current_time
        
        # Atualiza projéteis
        for bullet in self.bullets[:]:
            bullet.update(dt)
            if bullet.y < 0:  # Remove projéteis que saíram da tela
                self.bullets.remove(bullet)
        
        # Atualiza invulnerabilidade
        if self.invulnerable:
            self.invulnerable_time -= dt
            if self.invulnerable_time <= 0:
                self.invulnerable = False
    
    def shoot(self):
        """Cria um novo projétil"""
        bullet = Bullet(self.x, self.y - self.rect.height // 2, 0, -500)
        self.bullets.append(bullet)
        
        # Toca som do tiro
        if self.shoot_sound:
            self.shoot_sound.play()
    
    def take_damage(self):
        """Jogador recebe dano"""
        if not self.invulnerable:
            self.lives -= 1
            self.invulnerable = True
            self.invulnerable_time = self.invulnerable_duration
            return True
        return False
    
    def is_alive(self):
        """Verifica se o jogador ainda está vivo"""
        return self.lives > 0
    
    def reset_position(self):
        """Reseta a posição do jogador"""
        self.x = self.screen_width // 2
        self.y = self.screen_height - 100
        self.rect.centerx = self.x
        self.rect.centery = self.y
    
    def draw(self, screen):
        """
        Desenha o jogador na tela
        
        Args:
            screen: Superfície do pygame para desenhar
        """
        # Efeito de piscar quando invulnerável
        if self.invulnerable:
            # Pisca a cada 0.1 segundos
            if int(self.invulnerable_time * 10) % 2 == 0:
                return  # Não desenha (efeito de piscar)
        
        screen.blit(self.sprite, self.rect)
        
        # Desenha projéteis
        for bullet in self.bullets:
            bullet.draw(screen)
    
    def get_bullets(self):
        """Retorna lista de projéteis ativos"""
        return self.bullets
    
    def remove_bullet(self, bullet):
        """Remove um projétil específico"""
        if bullet in self.bullets:
            self.bullets.remove(bullet)
