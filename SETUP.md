# 🛠️ Setup e Instalação - Space Defender

## 📋 Pré-requisitos

### Para Executar o Jogo:
- **Opção 1**: Nenhum (use o executável)
- **Opção 2**: Python 3.7+ e Pygame (para código fonte)

### Para Desenvolvimento:
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para versionamento)

## 🚀 Instalação Rápida

### 1. Download do Repositório
```bash
# Via Git
git clone https://github.com/fany-santos8/space-defender-game.git
cd space-defender-game

# Ou baixe o ZIP do GitHub e extraia
```

### 2. Instalação Automática
```bash
# Execute o script de instalação
python install_and_run.py
```

Este script irá:
- ✅ Verificar a versão do Python
- ✅ Instalar dependências automaticamente
- ✅ Executar o jogo

## 🔧 Instalação Manual

### 1. Verificar Python
```bash
python --version
# Deve ser 3.7 ou superior
```

### 2. Instalar Dependências
```bash
# Instalar pygame
pip install pygame

# Ou instalar todas as dependências
pip install -r requirements.txt
```

### 3. Executar o Jogo
```bash
python main.py
```

## 🧪 Executar Testes

```bash
# Testes automatizados
python test_game.py

# Verificar se tudo está funcionando
python -c "import pygame; print('Pygame OK!')"
```

## 📦 Compilar Executável

### Instalar PyInstaller
```bash
pip install pyinstaller
```

### Compilar
```bash
# Compilação automática
python create_release.py

# Ou manual
pyinstaller --onefile --windowed --name=SpaceDefender main.py
```

## 🐛 Solução de Problemas

### Erro: "pygame not found"
```bash
pip install pygame
```

### Erro: "Python not found"
- Instale Python 3.7+ do site oficial: https://python.org

### Erro: "No audio device"
- Normal em sistemas sem placa de som
- O jogo funciona normalmente sem audio

### Erro de permissão no Windows
- Execute o terminal como administrador
- Ou use: `python -m pip install --user pygame`

### Jogo muito lento
- Feche outros programas
- Verifique se tem pelo menos 256MB RAM livre

## 🎮 Controles e Configuração

### Controles Padrão:
- **Movimento**: Setas ou WASD
- **Atirar**: Espaço
- **Sair**: ESC
- **Reiniciar**: R (game over)

### Configurações:
- FPS: 60 (fixo)
- Resolução: 800x600 (fixo)
- Audio: Automático (com fallback)

## 📁 Estrutura de Arquivos

```
space-defender-game/
├── main.py              # 🎮 Arquivo principal
├── game/                # 📁 Módulos do jogo
│   ├── __init__.py
│   ├── player.py        # 🚀 Classe do jogador
│   ├── asteroid.py      # 🌌 Asteroides
│   ├── bullet.py        # 💥 Projéteis
│   ├── game_state.py    # 🎯 Estados do jogo
│   └── utils.py         # 🛠️ Utilitários
├── assets/              # 📁 Recursos (opcional)
│   ├── images/          # 🖼️ Sprites
│   └── sounds/          # 🔊 Audio
├── release/             # 📁 Executável compilado
├── requirements.txt     # 📋 Dependências
├── test_game.py        # 🧪 Testes
├── install_and_run.py  # 🚀 Instalação automática
├── create_release.py   # 📦 Compilação
├── README.md           # 📖 Documentação
├── SETUP.md            # 🛠️ Este arquivo
├── LICENSE             # 📄 Licença
└── .gitignore          # 🚫 Arquivos ignorados
```

## 🌐 Compatibilidade

### Sistemas Operacionais:
- ✅ **Windows**: 7, 8, 10, 11
- ✅ **Linux**: Ubuntu, Debian, Fedora, etc.
- ✅ **macOS**: 10.12+ (não testado)

### Versões Python:
- ✅ **Python 3.7**
- ✅ **Python 3.8**
- ✅ **Python 3.9**
- ✅ **Python 3.10**
- ✅ **Python 3.11**

### Hardware Mínimo:
- **CPU**: Qualquer processador moderno
- **RAM**: 256 MB disponível
- **GPU**: Integrada (não requer placa dedicada)
- **Espaço**: 50 MB

## 📞 Suporte

### Problemas Comuns:
1. **Jogo não inicia**: Verifique Python e pygame
2. **Sem som**: Normal, jogo funciona sem audio
3. **Lento**: Feche outros programas
4. **Erro de import**: Reinstale dependências

### Onde Buscar Ajuda:
- 📖 Leia este arquivo (SETUP.md)
- 🧪 Execute `python test_game.py`
- 🐛 Abra uma issue no GitHub
- 📧 Entre em contato com o desenvolvedor

---

**🎮 Divirta-se jogando Space Defender!**
