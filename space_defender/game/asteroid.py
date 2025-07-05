"""
Classe dos asteroides para o jogo Space Defender
"""

import pygame
import random
import math
from .utils import create_asteroid_sprite, distance

class Asteroid:
    def __init__(self, x, y, screen_width, screen_height):
        """
        Inicializa um asteroide
        
        Args:
            x (float): Posição inicial X
            y (float): Posição inicial Y
            screen_width (int): Largura da tela
            screen_height (int): Altura da tela
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Posição
        self.x = x
        self.y = y
        
        # Tamanho aleatório
        self.size = random.randint(20, 50)
        self.radius = self.size // 2
        
        # Velocidade
        self.vel_x = random.uniform(-50, 50)  # Movimento horizontal leve
        self.vel_y = random.uniform(100, 200)  # Movimento para baixo
        
        # Rotação
        self.rotation = 0
        self.rotation_speed = random.uniform(-180, 180)  # graus por segundo
        
        # Sprite
        self.sprite = create_asteroid_sprite((self.size, self.size))
        self.rect = self.sprite.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        # Pontuação que dá quando destruído
        self.points = max(10, 60 - self.size)  # Asteroides menores dão mais pontos
    
    def update(self, dt):
        """
        Atualiza a posição e rotação do asteroide
        
        Args:
            dt (float): Delta time em segundos
        """
        # Movimento
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt
        
        # Rotação
        self.rotation += self.rotation_speed * dt
        
        # Mantém rotação entre 0-360
        self.rotation = self.rotation % 360
        
        # Atualiza rect
        self.rect.centerx = self.x
        self.rect.centery = self.y
        
        # Wrap horizontal (volta do outro lado)
        if self.x < -self.radius:
            self.x = self.screen_width + self.radius
        elif self.x > self.screen_width + self.radius:
            self.x = -self.radius
    
    def draw(self, screen):
        """
        Desenha o asteroide na tela com rotação
        
        Args:
            screen: Superfície do pygame para desenhar
        """
        # Rotaciona o sprite
        rotated_sprite = pygame.transform.rotate(self.sprite, self.rotation)
        rotated_rect = rotated_sprite.get_rect(center=(self.x, self.y))
        
        screen.blit(rotated_sprite, rotated_rect)
    
    def is_off_screen(self):
        """
        Verifica se o asteroide saiu da tela (parte inferior)
        
        Returns:
            bool: True se estiver fora da tela
        """
        return self.y > self.screen_height + self.radius
    
    def collides_with(self, other_rect, other_radius=None):
        """
        Verifica colisão com outro objeto
        
        Args:
            other_rect: Rect do outro objeto
            other_radius: Raio do outro objeto (para colisão circular)
        
        Returns:
            bool: True se houver colisão
        """
        if other_radius:
            # Colisão circular
            other_center = other_rect.center
            dist = distance((self.x, self.y), other_center)
            return dist < (self.radius + other_radius)
        else:
            # Colisão retangular
            return self.rect.colliderect(other_rect)
    
    def split(self):
        """
        Divide o asteroide em pedaços menores (se for grande o suficiente)
        
        Returns:
            list: Lista de novos asteroides menores ou lista vazia
        """
        if self.size > 25:  # Só divide se for grande o suficiente
            fragments = []
            num_fragments = random.randint(2, 3)
            
            for _ in range(num_fragments):
                # Cria fragmento menor
                fragment = Asteroid(self.x, self.y, self.screen_width, self.screen_height)
                fragment.size = self.size // 2
                fragment.radius = fragment.size // 2
                fragment.sprite = create_asteroid_sprite((fragment.size, fragment.size))
                fragment.rect = fragment.sprite.get_rect()
                
                # Velocidade aleatória para os fragmentos
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(50, 150)
                fragment.vel_x = math.cos(angle) * speed
                fragment.vel_y = math.sin(angle) * speed + 50  # Mantém movimento para baixo
                
                # Rotação mais rápida para fragmentos
                fragment.rotation_speed = random.uniform(-360, 360)
                
                fragments.append(fragment)
            
            return fragments
        
        return []

class AsteroidManager:
    def __init__(self, screen_width, screen_height):
        """
        Gerenciador de asteroides
        
        Args:
            screen_width (int): Largura da tela
            screen_height (int): Altura da tela
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.asteroids = []
        
        # Configurações de spawn
        self.spawn_timer = 0
        self.spawn_interval = 2.0  # segundos entre spawns
        self.min_spawn_interval = 0.5
        self.spawn_acceleration = 0.98  # Reduz intervalo gradualmente
    
    def update(self, dt):
        """
        Atualiza todos os asteroides
        
        Args:
            dt (float): Delta time em segundos
        """
        # Atualiza asteroides existentes
        for asteroid in self.asteroids[:]:
            asteroid.update(dt)
            
            # Remove asteroides que saíram da tela
            if asteroid.is_off_screen():
                self.asteroids.remove(asteroid)
        
        # Sistema de spawn
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_asteroid()
            self.spawn_timer = 0
            
            # Acelera o spawn gradualmente
            self.spawn_interval = max(self.min_spawn_interval, 
                                    self.spawn_interval * self.spawn_acceleration)
    
    def spawn_asteroid(self):
        """Cria um novo asteroide no topo da tela"""
        x = random.randint(0, self.screen_width)
        y = -50  # Começa acima da tela
        
        asteroid = Asteroid(x, y, self.screen_width, self.screen_height)
        self.asteroids.append(asteroid)
    
    def draw(self, screen):
        """
        Desenha todos os asteroides
        
        Args:
            screen: Superfície do pygame para desenhar
        """
        for asteroid in self.asteroids:
            asteroid.draw(screen)
    
    def get_asteroids(self):
        """Retorna lista de asteroides ativos"""
        return self.asteroids
    
    def remove_asteroid(self, asteroid):
        """Remove um asteroide específico"""
        if asteroid in self.asteroids:
            self.asteroids.remove(asteroid)
    
    def add_asteroid(self, asteroid):
        """Adiciona um asteroide à lista"""
        self.asteroids.append(asteroid)
    
    def clear(self):
        """Remove todos os asteroides"""
        self.asteroids.clear()
        self.spawn_timer = 0
        self.spawn_interval = 2.0
