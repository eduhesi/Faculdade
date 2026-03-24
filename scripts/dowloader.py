import subprocess
import os
import shutil
from printer import printer as p, PrinterType

def downloader(url: str, items, retries: str):
    for i in items:
        url = url.format(i)
        cmd = [
            "gallery-dl",
            "--user-agent", "browser",
            "--cookies-from-browser", "firefox",
            "--retries", retries,
            url
        ]
        print(f"Baixando {f'v{i:03d}'}...")
        subprocess.run(cmd, check=True)
    
def specific_downloader(): 
    min = 147
    max = 163

    base_url = "https://www.mgeko.cc/reader/en/the-daily-life-of-the-immortal-king-chapter-{}-eng-li/"
    download_dir = "./teste"


    for chapter in range(min, max):
        url = base_url.format(chapter)
        cmd = [
            "gallery-dl",
            f"r:{url}",
            "-d", download_dir
        ]
        p(f"Baixando capítulo {chapter}...")
        subprocess.run(cmd, check=True)

        src = os.path.join(download_dir, "directlink")
        dst = os.path.join(download_dir, f"ch{chapter}")

        if os.path.exists(src):
            shutil.move(src, dst)
            for filename in os.listdir(dst):
                if "the-daily-life-of-the-immortal-king" not in filename:
                    file_path = os.path.join(dst, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        p(f"Removido: {file_path}", PrinterType.ALERT)
            p(f"Pasta renomeada para {dst}", PrinterType.SUCCESS)
        else:
            p(f"Pasta de origem {src} não encontrada para o capítulo {chapter}.", PrinterType.ERROR)