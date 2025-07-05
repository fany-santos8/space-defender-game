"""
Funções utilitárias para o jogo Space Defender
"""

import pygame
import os
import math
import random

def load_image(path, scale=None):
    """
    Carrega uma imagem e opcionalmente redimensiona
    
    Args:
        path (str): Caminho para a imagem
        scale (tuple): Novo tamanho (width, height)
    
    Returns:
        pygame.Surface: Imagem carregada
    """
    try:
        image = pygame.image.load(path).convert_alpha()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except pygame.error:
        # Se não conseguir carregar, cria uma superfície colorida
        size = scale if scale else (32, 32)
        surface = pygame.Surface(size)
        surface.fill((255, 255, 255))  # Branco como fallback
        return surface

def load_sound(path):
    """
    Carrega um arquivo de som
    
    Args:
        path (str): Caminho para o arquivo de som
    
    Returns:
        pygame.mixer.Sound: Som carregado ou None se falhar
    """
    try:
        return pygame.mixer.Sound(path)
    except pygame.error:
        return None

def create_simple_sprite(size, color):
    """
    Cria um sprite simples colorido
    
    Args:
        size (tuple): Tamanho (width, height)
        color (tuple): Cor RGB
    
    Returns:
        pygame.Surface: Sprite criado
    """
    surface = pygame.Surface(size)
    surface.fill(color)
    return surface

def create_ship_sprite(size=(40, 30)):
    """
    Cria um sprite simples de nave espacial
    
    Args:
        size (tuple): Tamanho da nave
    
    Returns:
        pygame.Surface: Sprite da nave
    """
    surface = pygame.Surface(size, pygame.SRCALPHA)
    
    # Desenha uma nave triangular simples
    width, height = size
    points = [
        (width // 2, 0),           # Ponta da nave
        (0, height),               # Canto inferior esquerdo
        (width // 4, height * 3 // 4),  # Meio esquerdo
        (width * 3 // 4, height * 3 // 4),  # Meio direito
        (width, height)            # Canto inferior direito
    ]
    
    pygame.draw.polygon(surface, (0, 255, 255), points)  # Ciano
    pygame.draw.polygon(surface, (255, 255, 255), points, 2)  # Borda branca
    
    return surface

def create_asteroid_sprite(size=(30, 30)):
    """
    Cria um sprite simples de asteroide
    
    Args:
        size (tuple): Tamanho do asteroide
    
    Returns:
        pygame.Surface: Sprite do asteroide
    """
    surface = pygame.Surface(size, pygame.SRCALPHA)
    
    # Desenha um círculo irregular para simular asteroide
    width, height = size
    center = (width // 2, height // 2)
    radius = min(width, height) // 2 - 2
    
    # Círculo principal
    pygame.draw.circle(surface, (139, 69, 19), center, radius)  # Marrom
    pygame.draw.circle(surface, (160, 82, 45), center, radius, 2)  # Borda
    
    # Adiciona alguns detalhes
    for _ in range(3):
        x = random.randint(radius // 2, width - radius // 2)
        y = random.randint(radius // 2, height - radius // 2)
        r = random.randint(2, 5)
        pygame.draw.circle(surface, (101, 67, 33), (x, y), r)
    
    return surface

def create_bullet_sprite(size=(4, 10)):
    """
    Cria um sprite simples de projétil
    
    Args:
        size (tuple): Tamanho do projétil
    
    Returns:
        pygame.Surface: Sprite do projétil
    """
    surface = pygame.Surface(size, pygame.SRCALPHA)
    surface.fill((255, 255, 0))  # Amarelo
    return surface

def distance(pos1, pos2):
    """
    Calcula a distância entre dois pontos
    
    Args:
        pos1 (tuple): Primeira posição (x, y)
        pos2 (tuple): Segunda posição (x, y)
    
    Returns:
        float: Distância entre os pontos
    """
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def clamp(value, min_value, max_value):
    """
    Limita um valor entre um mínimo e máximo
    
    Args:
        value: Valor a ser limitado
        min_value: Valor mínimo
        max_value: Valor máximo
    
    Returns:
        Valor limitado
    """
    return max(min_value, min(value, max_value))

def create_explosion_particles(center, count=10):
    """
    Cria partículas para efeito de explosão
    
    Args:
        center (tuple): Centro da explosão
        count (int): Número de partículas
    
    Returns:
        list: Lista de partículas
    """
    particles = []
    for _ in range(count):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(50, 150)
        velocity = (math.cos(angle) * speed, math.sin(angle) * speed)
        
        particle = {
            'pos': list(center),
            'velocity': velocity,
            'life': random.uniform(0.5, 1.5),
            'max_life': random.uniform(0.5, 1.5),
            'color': random.choice([(255, 255, 0), (255, 165, 0), (255, 69, 0)])
        }
        particles.append(particle)
    
    return particles
