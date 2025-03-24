# Reddit Scraper

Este projeto é um scraper para coletar postagens do Reddit e armazená-las em um banco de dados SQLite.

## Requisitos

Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas necessárias (instaláveis via `pip install -r requirements.txt`)
- Conta no Reddit com credenciais de API

## Configuração

1. **Crie um aplicativo no Reddit:**
   - Acesse [Reddit Apps](https://www.reddit.com/prefs/apps)
   - Clique em **Create App**
   - Escolha "script"
   - Preencha os campos necessários e anote `client_id` e `client_secret`

2. **Configure as credenciais:**
   - No arquivo `config.py` (ou diretamente no código), defina as variáveis:
     ```python
     REDDIT_CLIENT_ID = "SEU_CLIENT_ID"
     REDDIT_CLIENT_SECRET = "SEU_CLIENT_SECRET"
     REDDIT_USER_AGENT = "SEU_USER_AGENT"
     ```

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script:
   ```bash
   python main.py
   ```

## Estrutura do Banco de Dados

O banco de dados `reddit_data.db` contém duas tabelas: `posts` e `comentarios`.

### Tabela `posts`

| Coluna          | Tipo  | Descrição |
|----------------|-------|-----------|
| id             | INT   | Identificador único |
| titulo         | TEXT  | Título da postagem |
| autor          | TEXT  | Nome do autor |
| subreddit      | TEXT  | Nome do subreddit |
| url            | TEXT  | Link da postagem (chave única) |
| data_publicacao | TEXT  | Data de criação da postagem |
| conteudo       | TEXT  | Conteúdo da postagem |
| upvotes        | INT   | Quantidade de votos positivos |

### Tabela `comentarios`

| Coluna         | Tipo  | Descrição |
|---------------|-------|-----------|
| id            | INT   | Identificador único |
| post_url      | TEXT  | URL da postagem referenciada |
| autor         | TEXT  | Nome do autor do comentário |
| data_comentario | TEXT | Data do comentário |
| conteudo      | TEXT  | Texto do comentário |

## Como Consultar os Dados

Rode o arquivo vizualizar.py na pasta src.






