def ler_imagem_colorida(arquivo_bmp):
    """Lê imagens BMP 24 bits diretamente, retornando largura, altura e pixels RGB"""
    with open(arquivo_bmp, 'rb') as f:
        if f.read(2) != b'BM':
            raise ValueError("Arquivo não é um BMP válido")
        
        f.seek(10)
        offset = int.from_bytes(f.read(4), 'little')
        
        f.seek(18)
        largura = int.from_bytes(f.read(4), 'little')
        altura = int.from_bytes(f.read(4), 'little')
        
        f.seek(28)
        bits_por_pixel = int.from_bytes(f.read(2), 'little')
        if bits_por_pixel != 24:
            raise ValueError("Suportado apenas BMP 24 bits")
        
        f.seek(offset)
        
        bytes_por_linha = largura * 3
        padding = (4 - (bytes_por_linha % 4)) % 4
        
        pixels = []
        for _ in range(altura):
            linha = []
            for _ in range(largura):
                b = ord(f.read(1))
                g = ord(f.read(1))
                r = ord(f.read(1))
                linha.append((r, g, b))
            f.read(padding) 
            pixels.append(linha)
    
    return largura, altura, pixels

def converter_para_cinza(pixels):
    """Converte matriz RGB para escala de cinza usando coeficientes ITU-R BT.601"""
    return [
        [int(0.299*r + 0.587*g + 0.114*b) for (r, g, b) in linha]
        for linha in pixels
    ]

def binarizar_imagem(cinza, limiar=128):
    """Aplica limiarização simples para converter em preto e branco"""
    return [
        [0 if pixel < limiar else 255 for pixel in linha]
        for linha in cinza
    ]

def salvar_pgm(nome_arquivo, dados, largura, altura, modo='P5'):
    """Salva imagem em formato PGM binário (P5) ou texto (P2)"""
    with open(nome_arquivo, 'wb') as f:
        header = f"{modo}\n{largura} {altura}\n255\n"
        f.write(header.encode('ascii'))
        
        if modo == 'P5':
            bytes_dados = bytes([p for linha in dados for p in linha])
            f.write(bytes_dados)
        else:
            for linha in dados:
                f.write(' '.join(map(str, linha)).encode('ascii'))
                f.write(b'\n')

if __name__ == "__main__":
    largura, altura, pixels = ler_imagem_colorida('entrada.bmp')
    
    img_cinza = converter_para_cinza(pixels)
    
    img_binaria = binarizar_imagem(img_cinza)
    
    salvar_pgm('cinza.pgm', img_cinza, largura, altura, 'P5')
    salvar_pgm('binario.pgm', img_binaria, largura, altura, 'P2')