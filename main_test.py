#!/usr/bin/env python3
"""
Space Defender - Versão de Teste
Versão modificada para testar o executável
"""

import pygame
import sys
import os
from game.game_state import GameState
from game.utils import load_image, load_sound

# Configurações do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TITLE = "Space Defender - Test"

class SpaceDefenderTest:
    def __init__(self):
        """Inicializa o jogo"""
        print("Inicializando Space Defender Test...")
        
        # Configura ambiente para teste
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        
        pygame.init()
        
        # Inicializa mixer de forma segura
        try:
            pygame.mixer.init()
            print("✓ Áudio inicializado")
        except pygame.error as e:
            print(f"⚠ Áudio não disponível: {e}")
        
        # Configuração da tela
        try:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption(TITLE)
            print("✓ Tela criada")
        except Exception as e:
            print(f"❌ Erro ao criar tela: {e}")
            raise
        
        # Clock para controlar FPS
        self.clock = pygame.time.Clock()
        
        # Estado do jogo
        try:
            self.game_state = GameState(self.screen)
            print("✓ Estado do jogo criado")
        except Exception as e:
            print(f"❌ Erro ao criar estado do jogo: {e}")
            raise
        
        # Carrega recursos
        self.load_assets()
        
        # Variáveis de controle
        self.running = True
        self.test_mode = True
        self.frame_count = 0
        self.max_frames = 300  # Executa por 5 segundos a 60 FPS
        
    def load_assets(self):
        """Carrega todos os assets do jogo"""
        try:
            # Música de fundo (só tenta se mixer foi inicializado)
            if pygame.mixer.get_init() and os.path.exists("assets/sounds/background_music.ogg"):
                pygame.mixer.music.load("assets/sounds/background_music.ogg")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)  # Loop infinito
                print("✓ Música carregada")
        except pygame.error:
            print("⚠ Música não carregada")
    
    def handle_events(self):
        """Processa eventos do pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Passa eventos para o estado do jogo
            self.game_state.handle_event(event)
    
    def update(self):
        """Atualiza a lógica do jogo"""
        self.game_state.update()
        
        # Verifica se o jogo deve ser encerrado
        if self.game_state.should_quit:
            self.running = False
        
        # Modo teste - para após um tempo
        if self.test_mode:
            self.frame_count += 1
            if self.frame_count >= self.max_frames:
                print(f"✓ Teste concluído após {self.frame_count} frames")
                self.running = False
    
    def draw(self):
        """Desenha tudo na tela"""
        self.screen.fill((0, 0, 20))  # Fundo azul escuro (espaço)
        self.game_state.draw()
        pygame.display.flip()
    
    def run(self):
        """Loop principal do jogo"""
        print("Iniciando loop do jogo...")
        print("Controles:")
        print("- Setas ou WASD: Mover nave")
        print("- Espaço: Atirar")
        print("- ESC: Sair")
        print("- R: Reiniciar (quando game over)")
        
        try:
            while self.running:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(FPS)
                
                # Mostra progresso a cada segundo
                if self.frame_count % 60 == 0:
                    print(f"Frame {self.frame_count}/{self.max_frames}")
            
            print("✓ Loop do jogo finalizado normalmente")
            
        except Exception as e:
            print(f"❌ Erro no loop do jogo: {e}")
            import traceback
            traceback.print_exc()
        finally:
            pygame.quit()

def main():
    """Função principal"""
    print("=== SPACE DEFENDER TEST ===")
    
    try:
        game = SpaceDefenderTest()
        game.run()
        print("✅ TESTE CONCLUÍDO COM SUCESSO!")
        return 0
    except Exception as e:
        print(f"❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        pygame.quit()
        return 1

if __name__ == "__main__":
    sys.exit(main())
