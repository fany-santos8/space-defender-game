#!/usr/bin/env python3
"""
Space Defender - Demo de Jogo 2D
Desenvolvido em Python com Pygame

Um jogo onde o jogador controla uma nave espacial para defender a Terra
de asteroides que caem do espaço.
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
TITLE = "Space Defender - Demo"

class SpaceDefender:
    def __init__(self):
        """Inicializa o jogo"""
        print("Inicializando Space Defender...")

        # Detecta se está em ambiente headless
        self.headless = self._detect_headless()
        if self.headless:
            print("Ambiente headless detectado - usando driver dummy")
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
            # Tenta com driver dummy como fallback
            os.environ['SDL_VIDEODRIVER'] = 'dummy'
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption(TITLE)
            self.headless = True
            print("✓ Tela criada em modo headless")
        
        # Clock para controlar FPS
        self.clock = pygame.time.Clock()
        
        # Estado do jogo
        self.game_state = GameState(self.screen)
        
        # Carrega recursos
        self.load_assets()
        
        # Variáveis de controle
        self.running = True

    def _detect_headless(self):
        """Detecta se está executando em ambiente headless"""
        # Verifica variáveis de ambiente comuns para headless
        if os.environ.get('DISPLAY') is None and os.name != 'nt':
            return True
        if os.environ.get('SDL_VIDEODRIVER') == 'dummy':
            return True
        # Verifica se está em container ou CI
        if os.environ.get('CI') or os.environ.get('GITHUB_ACTIONS'):
            return True
        return False

    def load_assets(self):
        """Carrega todos os assets do jogo"""
        try:
            # Música de fundo (só tenta se mixer foi inicializado)
            if pygame.mixer.get_init() and os.path.exists("assets/sounds/background_music.ogg"):
                pygame.mixer.music.load("assets/sounds/background_music.ogg")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)  # Loop infinito
        except pygame.error:
            print("Aviso: Não foi possível carregar a música de fundo")
    
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
    
    def draw(self):
        """Desenha tudo na tela"""
        self.screen.fill((0, 0, 20))  # Fundo azul escuro (espaço)
        self.game_state.draw()
        pygame.display.flip()
    
    def run(self):
        """Loop principal do jogo"""
        print("Iniciando Space Defender...")
        print("Controles:")
        print("- Setas ou WASD: Mover nave")
        print("- Espaço: Atirar")
        print("- ESC: Sair")
        print("- R: Reiniciar (quando game over)")

        if self.headless:
            print("Modo headless - executando por 10 segundos para demonstração")
            frame_count = 0
            max_frames = 600  # 10 segundos a 60 FPS

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

            # Em modo headless, para após um tempo
            if self.headless:
                frame_count += 1
                if frame_count % 60 == 0:  # A cada segundo
                    print(f"Frame {frame_count}/{max_frames}")
                if frame_count >= max_frames:
                    print("✓ Demonstração concluída")
                    self.running = False

        pygame.quit()
        sys.exit()

def main():
    """Função principal"""
    try:
        game = SpaceDefender()
        game.run()
    except Exception as e:
        print(f"Erro ao executar o jogo: {e}")
        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
