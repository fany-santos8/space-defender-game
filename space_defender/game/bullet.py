"""
Classe dos projéteis para o jogo Space Defender
"""

import pygame
from .utils import create_bullet_sprite

class Bullet:
    def __init__(self, x, y, vel_x, vel_y):
        """
        Inicializa um projétil
        
        Args:
            x (float): Posição inicial X
            y (float): Posição inicial Y
            vel_x (float): Velocidade X (pixels por segundo)
            vel_y (float): Velocidade Y (pixels por segundo)
        """
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        
        # Sprite
        self.sprite = create_bullet_sprite((4, 10))
        self.rect = self.sprite.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        # Raio para detecção de colisão
        self.radius = 2
    
    def update(self, dt):
        """
        Atualiza a posição do projétil
        
        Args:
            dt (float): Delta time em segundos
        """
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt
        
        # Atualiza rect
        self.rect.centerx = self.x
        self.rect.centery = self.y
    
    def draw(self, screen):
        """
        Desenha o projétil na tela
        
        Args:
            screen: Superfície do pygame para desenhar
        """
        screen.blit(self.sprite, self.rect)
    
    def is_off_screen(self, screen_width, screen_height):
        """
        Verifica se o projétil saiu da tela
        
        Args:
            screen_width (int): Largura da tela
            screen_height (int): Altura da tela
        
        Returns:
            bool: True se estiver fora da tela
        """
        return (self.x < 0 or self.x > screen_width or 
                self.y < 0 or self.y > screen_height)
