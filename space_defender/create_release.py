#!/usr/bin/env python3
"""
Script para criar uma versão de release completa do Space Defender
"""

import os
import sys
import subprocess
import shutil
import zipfile
from datetime import datetime

def check_requirements():
    """Verifica se todos os requisitos estão instalados"""
    print("Verificando requisitos...")
    
    try:
        import pygame
        print(f"✓ Pygame {pygame.version.ver} encontrado")
    except ImportError:
        print("✗ Pygame não encontrado. Instale com: pip install pygame")
        return False
    
    try:
        import PyInstaller
        print(f"✓ PyInstaller encontrado")
    except ImportError:
        print("✗ PyInstaller não encontrado. Instale com: pip install pyinstaller")
        return False
    
    return True

def create_executable():
    """Cria o executável do jogo"""
    print("\nCriando executável...")
    
    # Remove builds anteriores
    for folder in ["build", "dist", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Removido: {folder}")
    
    # Remove arquivos spec
    for file in ["SpaceDefender.spec", "main.spec"]:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removido: {file}")
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=SpaceDefender",
        "--distpath=release",
        "main.py"
    ]
    
    try:
        print("Executando PyInstaller...")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Executável criado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Erro ao criar executável: {e}")
        if e.stderr:
            print("Erro detalhado:")
            print(e.stderr)
        return False

def create_documentation():
    """Cria documentação adicional"""
    print("\nCriando documentação...")

    try:
        # Cria arquivo de instruções
        instructions = """SPACE DEFENDER - INSTRUÇÕES DE JOGO

COMO JOGAR:
1. Execute SpaceDefender (ou SpaceDefender.exe no Windows)
2. No menu principal, pressione ESPAÇO para começar
3. Use as setas ou WASD para mover a nave
4. Pressione ESPAÇO para atirar
5. Destrua asteroides para ganhar pontos
6. Evite colisões - você tem 3 vidas
7. Tente bater seu recorde!

CONTROLES:
- Setas ou WASD: Mover nave
- Espaço: Atirar
- ESC: Sair do jogo
- R: Reiniciar (quando game over)

DICAS:
- Asteroides grandes se dividem quando destruídos
- Asteroides menores dão mais pontos
- Você fica invulnerável por 2 segundos após ser atingido
- A dificuldade aumenta com o tempo

REQUISITOS DO SISTEMA:
- Windows 7 ou superior (para .exe)
- Linux (executável nativo)
- Não requer instalação
- Não requer Python instalado

DESENVOLVIDO EM PYTHON COM PYGAME
Projeto acadêmico - Generation Brasil
"""

        with open("release/INSTRUÇÕES.txt", "w", encoding="utf-8") as f:
            f.write(instructions)

        print("✓ Arquivo de instruções criado")
        return True
    except Exception as e:
        print(f"✗ Erro ao criar documentação: {e}")
        return False

def create_zip_package():
    """Cria pacote ZIP para distribuição"""
    print("\nCriando pacote ZIP...")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"SpaceDefender_v1.0_{timestamp}.zip"
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona executável (verifica ambos os nomes)
        if os.path.exists("release/SpaceDefender.exe"):
            zipf.write("release/SpaceDefender.exe", "SpaceDefender.exe")
            print("✓ Executável Windows adicionado ao ZIP")
        elif os.path.exists("release/SpaceDefender"):
            zipf.write("release/SpaceDefender", "SpaceDefender")
            print("✓ Executável Linux adicionado ao ZIP")

        # Adiciona instruções
        if os.path.exists("release/INSTRUÇÕES.txt"):
            zipf.write("release/INSTRUÇÕES.txt", "INSTRUÇÕES.txt")
            print("✓ Instruções adicionadas ao ZIP")

        # Adiciona README
        if os.path.exists("README.md"):
            zipf.write("README.md", "README.md")
            print("✓ README adicionado ao ZIP")
    
    print(f"✓ Pacote criado: {zip_name}")
    return zip_name

def cleanup():
    """Limpa arquivos temporários"""
    print("\nLimpando arquivos temporários...")
    
    for folder in ["build", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    
    for file in ["SpaceDefender.spec"]:
        if os.path.exists(file):
            os.remove(file)
    
    # Limpa cache Python em subpastas
    for root, dirs, files in os.walk("."):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                shutil.rmtree(os.path.join(root, dir_name))
    
    print("✓ Limpeza concluída")

def main():
    """Função principal"""
    print("=" * 60)
    print("SPACE DEFENDER - CRIAÇÃO DE RELEASE")
    print("=" * 60)
    
    # Verifica se está no diretório correto
    if not os.path.exists("main.py"):
        print("✗ Erro: Execute este script no diretório do jogo")
        return False
    
    # Verifica requisitos
    if not check_requirements():
        return False
    
    # Cria pasta de release
    if not os.path.exists("release"):
        os.makedirs("release")
        print("✓ Pasta release criada")
    
    # Executa etapas
    steps = [
        ("Criar executável", create_executable),
        ("Criar documentação", create_documentation),
    ]
    
    for step_name, step_func in steps:
        print(f"\n{'='*20} {step_name} {'='*20}")
        if not step_func():
            print(f"✗ Falha em: {step_name}")
            return False
    
    # Cria ZIP
    zip_name = create_zip_package()
    
    # Limpeza
    cleanup()
    
    print("\n" + "=" * 60)
    print("RELEASE CRIADA COM SUCESSO!")
    print("=" * 60)
    print(f"Executável: release/SpaceDefender.exe")
    print(f"Pacote ZIP: {zip_name}")
    print("\nPara distribuir:")
    print(f"1. Envie o arquivo {zip_name}")
    print("2. O usuário deve extrair e executar SpaceDefender.exe")
    print("3. Não requer instalação ou Python")
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 Release pronta para distribuição!")
    else:
        print("\n❌ Erro na criação da release")
    
    input("\nPressione Enter para sair...")
    sys.exit(0 if success else 1)
