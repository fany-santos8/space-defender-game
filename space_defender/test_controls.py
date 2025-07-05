#!/usr/bin/env python3
"""
Teste de controles para Space Defender
Este script testa se todas as teclas estão funcionando corretamente
"""

import pygame
import sys

def test_controls():
    """Testa todos os controles do jogo"""
    pygame.init()
    
    # Configuração da tela
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Teste de Controles - Space Defender")
    clock = pygame.time.Clock()
    
    # Fonte
    font = pygame.font.Font(None, 24)
    
    # Posição do "jogador" de teste
    player_x = 300
    player_y = 200
    
    # Mensagens
    messages = []
    
    print("=== TESTE DE CONTROLES ===")
    print("Teste todas as teclas:")
    print("- Setas do teclado")
    print("- WASD")
    print("- Numpad (2,4,6,8)")
    print("- Espaço, Ctrl, X (para atirar)")
    print("- ESC para sair")
    print("")
    
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Verifica teclas pressionadas
        keys = pygame.key.get_pressed()
        
        # Movimento
        speed = 200
        moved = False
        
        # Horizontal
        if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_KP4]:
            player_x -= speed * dt
            moved = True
            if "Esquerda OK" not in messages:
                messages.append("Esquerda OK")
                print("✓ Movimento para esquerda funcionando")
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_KP6]:
            player_x += speed * dt
            moved = True
            if "Direita OK" not in messages:
                messages.append("Direita OK")
                print("✓ Movimento para direita funcionando")
        
        # Vertical
        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_KP8]:
            player_y -= speed * dt
            moved = True
            if "Cima OK" not in messages:
                messages.append("Cima OK")
                print("✓ Movimento para cima funcionando")
        
        if keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_KP2]:
            player_y += speed * dt
            moved = True
            if "Baixo OK" not in messages:
                messages.append("Baixo OK")
                print("✓ Movimento para baixo funcionando")
        
        # Tiro
        if (keys[pygame.K_SPACE] or keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL] or 
            keys[pygame.K_KP0] or keys[pygame.K_x]):
            if "Tiro OK" not in messages:
                messages.append("Tiro OK")
                print("✓ Teclas de tiro funcionando")
        
        # Mantém na tela
        player_x = max(20, min(player_x, 580))
        player_y = max(20, min(player_y, 380))
        
        # Desenha
        screen.fill((0, 0, 50))
        
        # Desenha "jogador"
        pygame.draw.circle(screen, (0, 255, 0), (int(player_x), int(player_y)), 15)
        pygame.draw.polygon(screen, (255, 255, 255), [
            (int(player_x), int(player_y - 15)),
            (int(player_x - 10), int(player_y + 10)),
            (int(player_x + 10), int(player_y + 10))
        ])
        
        # Instruções
        instructions = [
            "Teste os controles movendo a nave:",
            "Setas, WASD, Numpad (2,4,6,8) - Movimento",
            "Espaço, Ctrl, X - Tiro",
            "ESC - Sair do teste"
        ]
        
        y = 10
        for instruction in instructions:
            text = font.render(instruction, True, (255, 255, 255))
            screen.blit(text, (10, y))
            y += 25
        
        # Status dos testes
        y = 150
        status_text = font.render("Status dos testes:", True, (255, 255, 0))
        screen.blit(status_text, (10, y))
        y += 25
        
        for message in messages:
            text = font.render(f"✓ {message}", True, (0, 255, 0))
            screen.blit(text, (10, y))
            y += 20
        
        # Contador de testes
        total_tests = 5  # Esquerda, Direita, Cima, Baixo, Tiro
        completed = len(messages)
        progress_text = font.render(f"Progresso: {completed}/{total_tests} testes", True, (200, 200, 200))
        screen.blit(progress_text, (10, 350))
        
        if completed == total_tests:
            success_text = font.render("TODOS OS CONTROLES FUNCIONANDO!", True, (0, 255, 0))
            screen.blit(success_text, (10, 370))
        
        pygame.display.flip()
    
    pygame.quit()
    
    # Relatório final
    print("\n=== RELATÓRIO FINAL ===")
    if len(messages) == 5:
        print("✓ SUCESSO: Todos os controles estão funcionando!")
    else:
        print("⚠ ATENÇÃO: Alguns controles podem não estar funcionando:")
        expected = ["Esquerda OK", "Direita OK", "Cima OK", "Baixo OK", "Tiro OK"]
        for test in expected:
            if test in messages:
                print(f"  ✓ {test}")
            else:
                print(f"  ✗ {test.replace(' OK', '')} - NÃO TESTADO")
    
    print("\nSe algum controle não funcionou, verifique:")
    print("- Se o teclado está funcionando corretamente")
    print("- Se não há conflitos com outros programas")
    print("- Se o pygame está atualizado")

if __name__ == "__main__":
    test_controls()
