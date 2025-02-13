import subprocess
from pathlib import Path

caminho_magick = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"
pasta_base = Path(r"C:\Users\User\Desktop\Desafio")

arquivos_pgm = [
    pasta_base / "cinza.pgm",
    pasta_base / "binario.pgm"
]

for pgm_path in arquivos_pgm:
    if pgm_path.exists():
        png_path = pgm_path.with_suffix(".png")
        resultado = subprocess.run(
            [caminho_magick, str(pgm_path), str(png_path)],
            capture_output=True,
            text=True
        )
        if resultado.returncode == 0:
            print(f"Arquivo convertido: {png_path}")
        else:
            print(f"Erro ao converter {pgm_path}: {resultado.stderr}")
    else:
        print(f"Arquivo não encontrado: {pgm_path}")



