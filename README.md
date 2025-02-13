# Conversor de Imagens   🖼️➡️⚫⚪

[![DIO Badge](https://hermes.digitalinnovation.one/assets/diome/logo.svg)](https://web.dio.me)


## 🏆 Contexto do Desafio
Este projeto foi desenvolvido como parte do **Bootcamp BairesDev - Machine Learning Practitioner da Digital Innovation One (DIO)**, com os seguintes requisitos principais:

Implementar conversão de cores usando apenas Python padrão

Manipulação manual de pixels

Proibição total de bibliotecas externas

Entregar solução autossuficiente


## 🛠️ Funcionalidades

### **Implementação Principal (Python Puro)**

- ✅ Leitura direta de arquivos BMP 24 bits
  
- ✅ Conversão matemática para escala de cinza (PGM P5)
  
- ✅ Binarização por limiarização (PGM P2)
  
- ✅ Processamento 100% em código nativo Python

### **Conversão Opcional para PNG**

- ⚙️ Requer ImageMagick instalado
  
- ⚙️ Gera arquivos PNG para visualização facilitada

## 📋 Pré-requisitos

### **Mínimos**
- Python
  
- Qualquer editor de texto/IDE

### **Opcional**
- ImageMagick (apenas para conversão final)

  - [Download oficial](https://imagemagick.org/script/download.php)


### Passo a Passo

1. **Preparar a imagem**:
   - Converta sua imagem para BMP 24 bits (usando Paint, Photoshop, etc)
   - Renomeie para `entrada.bmp` e coloque na pasta do projeto

2. **Conversão para PGM**:
   ```cmd
   python tira_cor.py
   
**Saídas geradas**:

cinza.pgm (tons de cinza)

binario.pgm (preto e branco)


3. **Conversão para PNG (Opcional)**:
   ```cmd
   python converter_imagem.py

**Saídas geradas**:

cinza.png

binario.png


## ⚙️ Configuração do ImageMagick

Edite converter_imagem.py com o caminho da sua instalação:

caminho_magick = r"C:\SEU\CAMINHO\ImageMagick-7.1.1-Q16-HDRI\magick.exe" # ← Atualize aqui!

