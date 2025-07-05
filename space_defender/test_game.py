#!/usr/bin/env python3
"""
Script de teste para verificar se o jogo Space Defender funciona corretamente
"""

import sys
import os
import traceback

def test_imports():
    """Testa se todos os módulos podem ser importados"""
    print("Testando imports...")
    
    try:
        import pygame
        print(f"✓ Pygame {pygame.version.ver} importado com sucesso")
    except ImportError as e:
        print(f"✗ Erro ao importar pygame: {e}")
        return False
    
    try:
        from game.player import Player
        print("✓ Módulo Player importado")
    except ImportError as e:
        print(f"✗ Erro ao importar Player: {e}")
        return False
    
    try:
        from game.asteroid import Asteroid, AsteroidManager
        print("✓ Módulo Asteroid importado")
    except ImportError as e:
        print(f"✗ Erro ao importar Asteroid: {e}")
        return False
    
    try:
        from game.bullet import Bullet
        print("✓ Módulo Bullet importado")
    except ImportError as e:
        print(f"✗ Erro ao importar Bullet: {e}")
        return False
    
    try:
        from game.game_state import GameState
        print("✓ Módulo GameState importado")
    except ImportError as e:
        print(f"✗ Erro ao importar GameState: {e}")
        return False
    
    try:
        from game.utils import create_ship_sprite, create_asteroid_sprite
        print("✓ Módulo Utils importado")
    except ImportError as e:
        print(f"✗ Erro ao importar Utils: {e}")
        return False
    
    return True

def test_pygame_init():
    """Testa se o pygame pode ser inicializado"""
    print("\nTestando inicialização do Pygame...")
    
    try:
        import pygame
        pygame.init()
        
        # Testa criação de display (modo headless)
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        screen = pygame.display.set_mode((800, 600))
        print("✓ Pygame inicializado com sucesso")
        
        pygame.quit()
        return True
    except Exception as e:
        print(f"✗ Erro ao inicializar pygame: {e}")
        return False

def test_game_objects():
    """Testa se os objetos do jogo podem ser criados"""
    print("\nTestando criação de objetos do jogo...")
    
    try:
        import pygame
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        
        # Testa Player
        from game.player import Player
        player = Player(400, 500, 800, 600)
        print("✓ Player criado com sucesso")
        
        # Testa Asteroid
        from game.asteroid import Asteroid, AsteroidManager
        asteroid = Asteroid(100, 100, 800, 600)
        asteroid_manager = AsteroidManager(800, 600)
        print("✓ Asteroid e AsteroidManager criados com sucesso")
        
        # Testa Bullet
        from game.bullet import Bullet
        bullet = Bullet(400, 300, 0, -100)
        print("✓ Bullet criado com sucesso")
        
        # Testa GameState
        from game.game_state import GameState
        game_state = GameState(screen)
        print("✓ GameState criado com sucesso")
        
        pygame.quit()
        return True
    except Exception as e:
        print(f"✗ Erro ao criar objetos do jogo: {e}")
        traceback.print_exc()
        return False

def test_game_logic():
    """Testa lógica básica do jogo"""
    print("\nTestando lógica do jogo...")
    
    try:
        import pygame
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        
        from game.player import Player
        from game.asteroid import Asteroid
        from game.bullet import Bullet
        
        # Cria objetos
        player = Player(400, 500, 800, 600)
        asteroid = Asteroid(400, 100, 800, 600)
        
        # Testa movimento do player
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, 
                pygame.K_UP: False, pygame.K_DOWN: False,
                pygame.K_a: False, pygame.K_d: False,
                pygame.K_w: False, pygame.K_s: False,
                pygame.K_SPACE: False}
        
        player.update(1/60, keys)
        print("✓ Player.update() funcionando")
        
        # Testa movimento do asteroide
        asteroid.update(1/60)
        print("✓ Asteroid.update() funcionando")
        
        # Testa tiro
        player.shoot()
        print("✓ Player.shoot() funcionando")
        
        # Testa colisão
        collision = asteroid.collides_with(player.rect, 15)
        print(f"✓ Detecção de colisão funcionando (resultado: {collision})")
        
        pygame.quit()
        return True
    except Exception as e:
        print(f"✗ Erro na lógica do jogo: {e}")
        traceback.print_exc()
        return False

def main():
    """Função principal de teste"""
    print("=" * 60)
    print("TESTE DO JOGO SPACE DEFENDER")
    print("=" * 60)
    
    # Verifica se está no diretório correto
    if not os.path.exists("main.py"):
        print("✗ Erro: Execute este script no diretório do jogo")
        return False
    
    # Executa testes
    tests = [
        ("Imports", test_imports),
        ("Pygame Init", test_pygame_init),
        ("Game Objects", test_game_objects),
        ("Game Logic", test_game_logic)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        if test_func():
            passed += 1
            print(f"✓ {test_name}: PASSOU")
        else:
            print(f"✗ {test_name}: FALHOU")
    
    print("\n" + "=" * 60)
    print(f"RESULTADO: {passed}/{total} testes passaram")
    print("=" * 60)
    
    if passed == total:
        print("🎉 Todos os testes passaram! O jogo está pronto para ser executado.")
        print("Execute: python main.py")
        return True
    else:
        print("❌ Alguns testes falharam. Verifique os erros acima.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
