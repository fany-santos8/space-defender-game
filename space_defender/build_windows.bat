@echo off
echo ========================================
echo  Space Defender - Build para Windows
echo  VERSAO 2.0 - Controles Melhorados
echo ========================================

echo Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado!
    pause
    exit /b 1
)

echo.
echo Instalando/Atualizando dependencias...
python -m pip install --upgrade pip
python -m pip install pygame
python -m pip install pyinstaller

echo.
echo Testando controles antes da compilacao...
echo Execute 'python test_controls.py' se quiser testar os controles
echo.

echo Compilando o jogo com melhorias...
python -m PyInstaller --onefile --windowed --name SpaceDefender main.py

echo.
echo ========================================
echo  Compilacao concluida!
echo ========================================
echo.
echo MELHORIAS DA VERSAO 2.0:
echo - Controles multiplos (setas/WASD/numpad)
echo - Tiro multiplo (espaco/ctrl/x)
echo - Movimento mais rapido e suave
echo - Tiro mais rapido
echo.
echo O executavel foi criado em: dist\SpaceDefender.exe
echo.
echo Para testar:
echo 1. Execute: dist\SpaceDefender.exe
echo 2. Teste todos os controles
echo 3. Verifique se as setas funcionam agora!
echo.
pause
