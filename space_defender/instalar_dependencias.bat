@echo off
echo ========================================
echo  Space Defender - Instalacao Windows
echo ========================================

echo Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado!
    echo Instale Python de: https://python.org
    pause
    exit /b 1
)

echo.
echo Atualizando pip...
python -m pip install --upgrade pip

echo.
echo Instalando dependencias...
python -m pip install pygame
python -m pip install pyinstaller

echo.
echo Verificando instalacao...
python -c "import pygame; print('Pygame:', pygame.version.ver)"
python -m PyInstaller --version

echo.
echo ========================================
echo  Instalacao concluida!
echo ========================================
echo.
echo Agora voce pode compilar o jogo com:
echo   python build_exe.py
echo.
pause
