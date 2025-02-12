# Conversor de Imagens BMP para PGM 🖼️➡️⚫⚪

[![DIO Badge](https://hermes.digitalinnovation.one/assets/diome/logo.svg)](https://web.dio.me)

Projeto desenvolvido como desafio técnico da **Digital Innovation One (DIO)**, implementando conversão de imagens **sem uso de bibliotecas ou ferramentas externas**.

## 🛠️ Funcionalidades

### **Implementação Principal (Python Puro)**

- ✅ Leitura direta de arquivos BMP 24 bits
- 
- ✅ Conversão matemática para escala de cinza (PGM P5)
- 
- ✅ Binarização por limiarização (PGM P2)
- 
- ✅ Processamento 100% em código nativo Python

### **Conversão Opcional para PNG**

- ⚙️ Requer ImageMagick instalado
- 
- ⚙️ Gera arquivos PNG para visualização facilitada

## 📋 Pré-requisitos

### **Mínimos**
- Python 3.8+ (interpretador padrão)
- 
- Qualquer editor de texto/IDE

### **Opcional**
- ImageMagick (apenas para conversão final)
- 
  - [Download oficial](https://imagemagick.org/script/download.php)

⚙️ Como Usar

### Passo a Passo
1. **Preparar a imagem**:
   - Converta sua imagem para BMP 24 bits (usando Paint, Photoshop, etc)
   - Renomeie para `entrada.bmp` e coloque na pasta do projeto

2. **Conversão para PGM**:
   ```cmd
   python tira_cor.py
   
Saídas geradas:

cinza.pgm (tons de cinza)

binario.pgm (preto e branco)

Conversão para PNG (Opcional):

cmd
Copy
python converter_imagem.py
Saídas geradas:

cinza.png

binario.png

### Passo a Passo
1. **Preparar a imagem**:
   - Converta sua imagem para BMP 24 bits (usando Paint, Photoshop, etc)
   - Renomeie para `entrada.bmp` e coloque na pasta do projeto

2. **Conversão para PGM**:
   ```cmd
   python tira_cor.py
Saídas geradas:

cinza.pgm (tons de cinza)

binario.pgm (preto e branco)

Conversão para PNG (Opcional):

cmd
Copy
python converter_imagem.py
Saídas geradas:

cinza.png

binario.png

⚙️ Configuração do ImageMagick

Edite converter_imagem.py com o caminho da sua instalação:

caminho_magick = r"C:\SEU\CAMINHO\ImageMagick-7.1.1-Q16-HDRI\magick.exe" # ← Atualize aqui!

🏆 Contexto do Desafio
Este projeto foi desenvolvido como parte do Bootcamp [Nome do Bootcamp] da Digital Innovation One, com os seguintes requisitos principais:

Implementar conversão de cores usando apenas Python padrão

Manipulação manual de pixels

Proibição total de bibliotecas externas

Entregar solução autossuficiente

<p align="center"> <img src="https://hermes.digitalinnovation.one/assets/diome/logo-full.svg" width="200" alt="Logo DIO"> </p> ```
