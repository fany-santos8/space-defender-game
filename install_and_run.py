#!/usr/bin/env python3
"""
Script para instalar dependências e executar o jogo Space Defender
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala as dependências necessárias"""
    print("Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("Erro ao instalar dependências.")
        return False

def check_python_version():
    """Verifica se a versão do Python é adequada"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"Erro: Python 3.7+ é necessário. Versão atual: {version.major}.{version.minor}")
        return False
    print(f"Python {version.major}.{version.minor}.{version.micro} - OK")
    return True

def run_game():
    """Executa o jogo"""
    print("Iniciando Space Defender...")
    try:
        subprocess.run([sys.executable, "main.py"])
    except KeyboardInterrupt:
        print("\nJogo encerrado pelo usuário.")
    except Exception as e:
        print(f"Erro ao executar o jogo: {e}")

def main():
    """Função principal"""
    print("=" * 50)
    print("SPACE DEFENDER - INSTALAÇÃO E EXECUÇÃO")
    print("=" * 50)
    
    # Verifica versão do Python
    if not check_python_version():
        input("Pressione Enter para sair...")
        return
    
    # Verifica se está no diretório correto
    if not os.path.exists("main.py"):
        print("Erro: Execute este script no diretório do jogo.")
        input("Pressione Enter para sair...")
        return
    
    # Instala dependências
    if not install_requirements():
        input("Pressione Enter para sair...")
        return
    
    print("\n" + "=" * 50)
    print("PRONTO PARA JOGAR!")
    print("=" * 50)
    
    # Pergunta se quer executar
    response = input("Deseja executar o jogo agora? (s/n): ").lower().strip()
    if response in ['s', 'sim', 'y', 'yes', '']:
        run_game()
    else:
        print("Para executar o jogo manualmente, use: python main.py")

if __name__ == "__main__":
    main()
