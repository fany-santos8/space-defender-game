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
        pygame.init()

        # Inicializa mixer de forma segura
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Aviso: Não foi possível inicializar o áudio: {e}")
            print("O jogo continuará sem som.")
        
        # Configuração da tela
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        
        # Clock para controlar FPS
        self.clock = pygame.time.Clock()
        
        # Estado do jogo
        self.game_state = GameState(self.screen)
        
        # Carrega recursos
        self.load_assets()
        
        # Variáveis de controle
        self.running = True
        
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
        
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
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
