# Web Scraping ANS

Este projeto em Python realiza o web scraping dos Anexos I e II do site da ANS (https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos), baixando os arquivos PDF e compactando-os em um arquivo ZIP.

## Instalação

1. Clone este repositório:

   ```bash
   git clone [https://github.com/sarahtalentotech/web-scraping-ans.git](https://github.com/sarahtalentotech/web-scraping-ans.git)

2. Navegue até o diretório do projeto:

Bash

cd web_scraping

3. Instale as dependências:

Bash

pip install requests beautifulsoup4 python-dotenv tqdm

Execução
1. Crie um arquivo .env com as seguintes variáveis:

ANS_URL=[https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
OUTPUT_DIR=downloads

2. Execute o script:

Bash

python ans_scraper.py

3. O arquivo ZIP Anexos_ANS.zip será criado no diretório downloads.

Estrutura do Projeto
ans_scraper/
├── ans_scraper.py
├── utils.py
├── README.md
└── .env
ans_scraper.py: Script principal para realizar o web scraping.
utils.py: Funções auxiliares para download e compactação de arquivos.
README.md: Este arquivo, com instruções sobre o projeto.
.env: Arquivo com variáveis de ambiente.