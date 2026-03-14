import subprocess
import os
import shutil

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
    print(f"Baixando capítulo {chapter}...")
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
                    print(f"Removido: {file_path}")
        print(f"Pasta renomeada para {dst}")
    else:
        print(f"Pasta de origem {src} não encontrada para o capítulo {chapter}.")