@echo off
title Build - Silence Rill
echo ============================================
echo   BUILD: Silence Rill - Gerando .exe
echo ============================================
echo.

:: Verifica Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado. Instale em https://python.org
    pause
    exit /b 1
)

echo [1/3] Instalando dependencias...
pip install pyinstaller climage nava pillow colorama --quiet
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias.
    pause
    exit /b 1
)

echo [2/3] Compilando o executavel...
pyinstaller SilenceRill.spec --noconfirm
if errorlevel 1 (
    echo [ERRO] Falha na compilacao.
    pause
    exit /b 1
)

echo [3/3] Concluido!
echo.
echo O arquivo SilenceRill.exe foi gerado em: dist\SilenceRill.exe
echo.
echo Pressione qualquer tecla para abrir a pasta dist...
pause >nul
explorer dist
