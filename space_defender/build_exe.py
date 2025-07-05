#!/usr/bin/env python3
"""
Script para compilar o jogo Space Defender em um executável Windows
"""

import os
import sys
import subprocess
import shutil

def build_executable():
    """Compila o jogo em um executável"""
    print("Compilando Space Defender para Windows...")
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",                    # Um único arquivo executável
        "--windowed",                   # Sem console (para jogos)
        "--name=SpaceDefender",         # Nome do executável
        "--icon=assets/icon.ico",       # Ícone (se existir)
        "--add-data=assets;assets",     # Inclui pasta assets
        "main.py"
    ]
    
    try:
        # Remove builds anteriores
        if os.path.exists("build"):
            shutil.rmtree("build")
        if os.path.exists("dist"):
            shutil.rmtree("dist")
        if os.path.exists("SpaceDefender.spec"):
            os.remove("SpaceDefender.spec")
        
        # Executa PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print("Compilação concluída com sucesso!")
        print("Executável criado em: dist/SpaceDefender.exe")
        
        # Cria pasta para distribuição
        if not os.path.exists("release"):
            os.makedirs("release")
        
        # Copia executável
        if os.path.exists("dist/SpaceDefender.exe"):
            shutil.copy2("dist/SpaceDefender.exe", "release/SpaceDefender.exe")
            print("Executável copiado para: release/SpaceDefender.exe")
        
        # Copia assets se necessário (PyInstaller já inclui)
        print("\nPara distribuir o jogo:")
        print("1. Comprima a pasta 'release' em um arquivo ZIP")
        print("2. O arquivo SpaceDefender.exe pode ser executado diretamente")
        
    except subprocess.CalledProcessError as e:
        print(f"Erro durante a compilação: {e}")
        print("Saída do erro:")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("PyInstaller não encontrado. Instale com: pip install pyinstaller")
        return False
    
    return True

def create_batch_file():
    """Cria arquivo batch para facilitar a compilação"""
    batch_content = """@echo off
echo Compilando Space Defender...
python build_exe.py
pause
"""
    
    with open("build.bat", "w") as f:
        f.write(batch_content)
    
    print("Arquivo build.bat criado. Execute-o para compilar o jogo.")

def main():
    """Função principal"""
    if len(sys.argv) > 1 and sys.argv[1] == "--create-batch":
        create_batch_file()
        return
    
    # Verifica se está no diretório correto
    if not os.path.exists("main.py"):
        print("Erro: Execute este script no diretório do jogo (onde está main.py)")
        return
    
    # Verifica se pygame está instalado
    try:
        import pygame
        print(f"Pygame versão {pygame.version.ver} encontrado")
    except ImportError:
        print("Erro: Pygame não está instalado. Execute: pip install pygame")
        return
    
    # Compila o executável
    success = build_executable()
    
    if success:
        print("\n" + "="*50)
        print("COMPILAÇÃO CONCLUÍDA COM SUCESSO!")
        print("="*50)
        print("O jogo foi compilado para Windows.")
        print("Arquivo executável: release/SpaceDefender.exe")
        print("\nPara distribuir:")
        print("1. Comprima a pasta 'release' em um ZIP")
        print("2. Distribua o arquivo ZIP")
        print("3. O usuário pode extrair e executar SpaceDefender.exe")
    else:
        print("\n" + "="*50)
        print("ERRO NA COMPILAÇÃO")
        print("="*50)
        print("Verifique as mensagens de erro acima.")

if __name__ == "__main__":
    main()
