import os
import requests
from bs4 import BeautifulSoup
import zipfile
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

# URL do site da ANS
ANS_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
# Diretório para salvar os PDFs e o arquivo ZIP
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "downloads")

def download_pdf(url, output_dir):
    """
    Baixa um PDF da URL fornecida e salva no diretório de saída.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        filename = os.path.join(output_dir, url.split("/")[-1])
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")
        return None

def compress_files(file_list, output_dir):
    """
    Compacta uma lista de arquivos em um arquivo ZIP.
    """
    zip_filename = os.path.join(output_dir, "Anexos_ANS.zip")
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in tqdm(file_list, desc="Compactando arquivos"):
            zipf.write(file, os.path.basename(file))
    return zip_filename

def scrape_ans_pdfs(url, output_dir):
    """
    Realiza o web scraping dos PDFs dos Anexos I e II do site da ANS.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        pdf_links = []
        # Encontra todos os links que terminam com ".pdf" e contêm "Anexo I" ou "Anexo II"
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if href.endswith(".pdf") and ("Anexo I" in link.text or "Anexo II" in link.text):
                pdf_links.append(href)
        if not pdf_links:
            print("Nenhum link de PDF encontrado.")
            return
        pdf_files = []
        for link in tqdm(pdf_links, desc="Baixando PDFs"):
            pdf_path = download_pdf(link, output_dir)
            if pdf_path:
                pdf_files.append(pdf_path)
        if pdf_files:
            zip_filename = compress_files(pdf_files, output_dir)
            print(f"Arquivos compactados em: {zip_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    scrape_ans_pdfs(ANS_URL, OUTPUT_DIR)