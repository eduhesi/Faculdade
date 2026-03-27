import subprocess
import os
import shutil
from printer import printer as p, PrinterType
from concurrent.futures import ThreadPoolExecutor

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

def baixar_volume(url_template: str, i: int, retries: str = "3"):
    url = url_template.format(i)
    cmd = [
        "gallery-dl",
        "--user-agent", "browser",
        "--cookies-from-browser", "firefox",
        # "--retries", retries,
        url
    ]
    print(f"Baixando {f'v{i:03d}'}...")
    subprocess.run(cmd, check=True)

def downloader_thread(url_template: str, items, retries: str = "3", max_workers: int = 4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(baixar_volume, url_template, i, retries)
            for i in items
        ]
        # Aguarda todos terminarem (opcional, para capturar exceções)
        for future in futures:
            future.result()

if __name__ == '__main__':
    downloader_thread(
        "https://mangafire.to/read/the-disastrous-life-of-saiki-kk.kjp9/en/volume-{}", 
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26],
        max_workers=4
    )