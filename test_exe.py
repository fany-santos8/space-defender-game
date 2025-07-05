#!/usr/bin/env python3
"""
Teste simples para verificar se o PyInstaller está funcionando
"""

import sys
import os

def main():
    print("=== TESTE DE EXECUTÁVEL ===")
    print(f"Python: {sys.version}")
    print(f"Executável: {sys.executable}")
    print(f"Diretório atual: {os.getcwd()}")
    print(f"Argumentos: {sys.argv}")
    
    # Testa importação do pygame
    try:
        import pygame
        print(f"Pygame: {pygame.version.ver} - OK")
        
        # Testa inicialização básica
        pygame.init()
        print("Pygame.init() - OK")
        
        # Testa mixer com fallback
        try:
            pygame.mixer.init()
            print("Pygame.mixer.init() - OK")
        except Exception as e:
            print(f"Pygame.mixer.init() - FALHOU: {e}")
        
        # Testa criação de surface
        try:
            os.environ['SDL_VIDEODRIVER'] = 'dummy'
            screen = pygame.display.set_mode((100, 100))
            print("Pygame.display.set_mode() - OK")
        except Exception as e:
            print(f"Pygame.display.set_mode() - FALHOU: {e}")
            
    except ImportError as e:
        print(f"ERRO: Não foi possível importar pygame: {e}")
        return 1
    
    print("=== TESTE CONCLUÍDO COM SUCESSO ===")
    return 0

if __name__ == "__main__":
    sys.exit(main())
