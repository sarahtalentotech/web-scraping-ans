import os
import requests
import zipfile
from tqdm import tqdm

def download_pdf(url, output_dir):
    """Baixa um PDF da URL fornecida e salva no diretório de saída."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        filename = os.path.join(output_dir, url.split("/")[-1])
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")
        return None

def compress_files(file_list, output_dir):
    """Compacta uma lista de arquivos em um arquivo ZIP."""
    zip_filename = os.path.join(output_dir, "Anexos_ANS.zip")
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in tqdm(file_list, desc="Compactando arquivos"):
            zipf.write(file, os.path.basename(file))
    return zip_filename