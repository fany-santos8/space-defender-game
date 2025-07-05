#!/usr/bin/env python3
"""
Teste headless do jogo Space Defender
Verifica se todas as classes podem ser instanciadas sem erro
"""

import os
import sys

# Configura pygame para modo headless
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame
from game.player import Player
from game.asteroid import Asteroid, AsteroidManager
from game.bullet import Bullet
from game.game_state import GameState
from game.utils import *

def test_pygame_init():
    """Testa inicialização do pygame"""
    print("Testando inicialização do pygame...")
    pygame.init()
    
    try:
        pygame.mixer.init()
        print("✓ Mixer inicializado com sucesso")
    except pygame.error as e:
        print(f"⚠ Mixer não inicializado: {e}")
    
    # Cria tela dummy
    screen = pygame.display.set_mode((800, 600))
    print("✓ Tela criada com sucesso")
    return screen

def test_utils():
    """Testa funções utilitárias"""
    print("\nTestando funções utilitárias...")
    
    # Testa criação de sprites
    ship_sprite = create_ship_sprite()
    print("✓ Sprite da nave criado")
    
    asteroid_sprite = create_asteroid_sprite()
    print("✓ Sprite do asteroide criado")
    
    bullet_sprite = create_bullet_sprite()
    print("✓ Sprite do projétil criado")
    
    # Testa funções matemáticas
    dist = distance((0, 0), (3, 4))
    assert dist == 5.0, f"Distância incorreta: {dist}"
    print("✓ Função distance funcionando")
    
    clamped = clamp(15, 0, 10)
    assert clamped == 10, f"Clamp incorreto: {clamped}"
    print("✓ Função clamp funcionando")

def test_bullet():
    """Testa classe Bullet"""
    print("\nTestando classe Bullet...")
    
    bullet = Bullet(100, 100, 0, -500)
    print("✓ Bullet criado")
    
    bullet.update(0.1)  # 0.1 segundos
    assert bullet.y == 50, f"Posição Y incorreta: {bullet.y}"
    print("✓ Movimento do bullet funcionando")

def test_player():
    """Testa classe Player"""
    print("\nTestando classe Player...")
    
    player = Player(400, 500, 800, 600)
    print("✓ Player criado")
    
    # Simula teclas pressionadas
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, 
            pygame.K_UP: False, pygame.K_DOWN: False,
            pygame.K_a: False, pygame.K_d: False,
            pygame.K_w: False, pygame.K_s: False,
            pygame.K_SPACE: False}
    
    player.update(0.1, keys)
    print("✓ Update do player funcionando")
    
    # Testa tiro - aguarda um pouco para passar do cooldown
    keys[pygame.K_SPACE] = True
    player.update(0.1, keys)

    # Se não atirou ainda, aguarda mais tempo
    if len(player.bullets) == 0:
        import time
        time.sleep(0.3)  # Aguarda mais que o cooldown
        player.update(0.1, keys)

    assert len(player.bullets) > 0, "Tiro não foi criado"
    print("✓ Sistema de tiro funcionando")

def test_asteroid():
    """Testa classe Asteroid"""
    print("\nTestando classe Asteroid...")
    
    asteroid = Asteroid(100, 100, 800, 600)
    print("✓ Asteroid criado")
    
    asteroid.update(0.1)
    print("✓ Update do asteroid funcionando")
    
    # Testa divisão
    fragments = asteroid.split()
    if fragments:
        print(f"✓ Asteroid dividido em {len(fragments)} fragmentos")
    else:
        print("✓ Asteroid pequeno demais para dividir")

def test_asteroid_manager():
    """Testa classe AsteroidManager"""
    print("\nTestando classe AsteroidManager...")
    
    manager = AsteroidManager(800, 600)
    print("✓ AsteroidManager criado")
    
    manager.spawn_asteroid()
    assert len(manager.asteroids) == 1, "Asteroid não foi criado"
    print("✓ Spawn de asteroid funcionando")
    
    manager.update(0.1)
    print("✓ Update do manager funcionando")

def test_game_state():
    """Testa classe GameState"""
    print("\nTestando classe GameState...")
    
    screen = pygame.display.set_mode((800, 600))
    game_state = GameState(screen)
    print("✓ GameState criado")
    
    game_state.update()
    print("✓ Update do game state funcionando")

def main():
    """Executa todos os testes"""
    print("=== TESTE HEADLESS DO SPACE DEFENDER ===\n")
    
    try:
        screen = test_pygame_init()
        test_utils()
        test_bullet()
        test_player()
        test_asteroid()
        test_asteroid_manager()
        test_game_state()
        
        print("\n=== TODOS OS TESTES PASSARAM! ===")
        print("O jogo está funcionando corretamente.")
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    finally:
        pygame.quit()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
