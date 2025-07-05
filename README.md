# Space Defender - Demo de Jogo 2D

Um jogo de defesa espacial desenvolvido em Python usando Pygame, onde o jogador controla uma nave espacial para defender a Terra de asteroides que caem do espaço.

## 🎮 Sobre o Jogo

**Space Defender** é um jogo arcade 2D inspirado nos clássicos jogos de nave espacial. O objetivo é destruir o máximo de asteroides possível para proteger a Terra e conseguir a maior pontuação.

### Características:
- **Gênero**: Arcade/Shooter 2D
- **Plataforma**: Windows (executável .exe)
- **Linguagem**: Python 3.x
- **Biblioteca**: Pygame
- **Gráficos**: 2D com sprites simples
- **Audio**: Efeitos sonoros e música de fundo

## 🕹️ Como Jogar

### Controles:
- **Setas direcionais** ou **WASD**: Mover a nave
- **Espaço**: Atirar
- **ESC**: Sair do jogo
- **R**: Reiniciar (quando game over)

### Objetivo:
- Destrua asteroides para ganhar pontos
- Evite colisões com asteroides
- Sobreviva o máximo de tempo possível
- Tente bater seu recorde!

### Sistema de Pontuação:
- Asteroides pequenos: Mais pontos
- Asteroides grandes: Menos pontos, mas se dividem quando destruídos
- Asteroides divididos: Pontos extras

### Sistema de Vidas:
- Você começa com 3 vidas
- Perde uma vida ao colidir com asteroide
- Fica invulnerável por 2 segundos após ser atingido
- Game over quando todas as vidas acabam

## 🚀 Como Executar

### Opção 1: Executável Windows (Recomendado)
1. Baixe o arquivo `SpaceDefender.exe`
2. Execute diretamente (não precisa instalar nada)

### Opção 2: Código Fonte Python
1. Instale Python 3.7 ou superior
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o jogo:
   ```bash
   python main.py
   ```

## 🛠️ Desenvolvimento

### Estrutura do Projeto:
```
space_defender/
├── main.py              # Arquivo principal
├── game/                # Módulos do jogo
│   ├── __init__.py
│   ├── player.py        # Classe do jogador
│   ├── asteroid.py      # Classe dos asteroides
│   ├── bullet.py        # Classe dos projéteis
│   ├── game_state.py    # Gerenciamento de estados
│   └── utils.py         # Funções utilitárias
├── assets/              # Recursos do jogo
│   ├── images/          # Sprites (opcional)
│   └── sounds/          # Efeitos sonoros (opcional)
├── requirements.txt     # Dependências Python
├── build_exe.py        # Script de compilação
└── README.md           # Este arquivo
```

### Tecnologias Utilizadas:
- **Python 3.x**: Linguagem principal
- **Pygame**: Biblioteca para jogos 2D
- **PyInstaller**: Compilação para executável

### Compilar para Executável:
```bash
python build_exe.py
```

## 🎨 Assets

O jogo funciona sem assets externos, criando sprites simples programaticamente. Para melhorar a experiência visual e sonora, você pode adicionar:

### Imagens (Opcional):
- `assets/images/ship.png` - Sprite da nave
- `assets/images/asteroid.png` - Sprite do asteroide
- `assets/images/bullet.png` - Sprite do projétil

### Sons (Opcional):
- `assets/sounds/shoot.wav` - Som do tiro
- `assets/sounds/explosion.wav` - Som da explosão
- `assets/sounds/hit.wav` - Som de colisão
- `assets/sounds/background_music.ogg` - Música de fundo

## 🎯 Funcionalidades Implementadas

### ✅ Mecânicas Básicas:
- [x] Movimento da nave em 8 direções
- [x] Sistema de tiro com cooldown
- [x] Asteroides com movimento e rotação
- [x] Detecção de colisões
- [x] Sistema de vidas e invulnerabilidade
- [x] Sistema de pontuação

### ✅ Interface:
- [x] Menu principal
- [x] HUD com pontuação e vidas
- [x] Tela de game over
- [x] Sistema de recorde

### ✅ Efeitos Visuais:
- [x] Partículas de explosão
- [x] Rotação dos asteroides
- [x] Efeito de piscar quando invulnerável
- [x] Sprites criados programaticamente

### ✅ Audio:
- [x] Suporte a efeitos sonoros
- [x] Música de fundo
- [x] Sistema de fallback (funciona sem audio)

### ✅ Gameplay:
- [x] Dificuldade progressiva (asteroides mais frequentes)
- [x] Asteroides grandes se dividem
- [x] Wrap horizontal dos asteroides
- [x] Controles responsivos

## 🏆 Requisitos Atendidos

Este projeto atende todos os requisitos da atividade:

- ✅ **Jogo 2D**: Interface gráfica com Pygame
- ✅ **Não é console**: Interface gráfica completa
- ✅ **Linguagem Python**: 100% Python
- ✅ **Jogável**: Mecânicas completas e funcionais
- ✅ **Assets da internet**: Suporte a imagens e sons externos
- ✅ **Código próprio**: Implementação original
- ✅ **Executável Windows**: Compilação com PyInstaller
- ✅ **Arquivo ZIP**: Pronto para distribuição

## 👨‍💻 Autor

Desenvolvido como projeto acadêmico para demonstração de habilidades em:
- Programação orientada a objetos em Python
- Desenvolvimento de jogos com Pygame
- Gerenciamento de estados e eventos
- Detecção de colisões e física básica
- Interface gráfica e experiência do usuário

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais. Sinta-se livre para usar como referência ou base para seus próprios projetos.

---

**Divirta-se defendendo a Terra! 🌍🚀**
