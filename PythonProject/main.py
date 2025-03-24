import sqlite3
import praw
import time
import datetime


REDDIT_CLIENT_ID = "D_9gaIrfqnm6fZtq-tkZJA"
REDDIT_CLIENT_SECRET = "132RiPA5o9ZQm9Q4Xh3pGrKVPZV9XA"
REDDIT_USER_AGENT = "SEU_USER_AGENT"


reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)


DB_PATH = "src/novo_reddit_data.db"

def conectar_banco():
    """Cria e conecta ao banco de dados"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            subreddit TEXT,
            url TEXT UNIQUE,
            data_publicacao TEXT,
            conteudo TEXT,
            upvotes INTEGER
        );
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_url TEXT,
            autor TEXT,
            data_comentario TEXT,
            conteudo TEXT,
            FOREIGN KEY (post_url) REFERENCES posts (url)
        );
    """)

    conn.commit()
    return conn, cursor

def coletar_dados():
    """Coleta e insere dados do Reddit no banco"""
    try:
        conn, cursor = conectar_banco()
        print("🔄 Coletando posts...")
        subreddit = reddit.subreddit("Python")
        posts_salvos = 0

        for post in subreddit.hot(limit=10):
            cursor.execute("SELECT 1 FROM posts WHERE url = ?", (post.url,))
            if cursor.fetchone():
                print(f"✅ Post já salvo: {post.title}")
                continue


            data_publicacao = datetime.datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')

            print(f"📝 Inserindo no banco: {post.title}")
            cursor.execute("""
                INSERT INTO posts (titulo, autor, subreddit, url, data_publicacao, conteudo, upvotes) 
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (post.title, post.author.name if post.author else "Desconhecido",
                  subreddit.display_name, post.url, data_publicacao, post.selftext, post.score))
            posts_salvos += 1

            post.comments.replace_more(limit=0)
            comentarios = post.comments.list()[:5]
            for comment in comentarios:
                data_comentario = datetime.datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("""
                    INSERT INTO comentarios (post_url, autor, data_comentario, conteudo) 
                    VALUES (?, ?, ?, ?);
                """, (post.url, comment.author.name if comment.author else "Desconhecido",
                      data_comentario, comment.body))

        conn.commit()
        print(f"✅ {posts_salvos} posts salvos no banco de dados")

    except Exception as e:
        print(f"⚠️ Erro durante a coleta: {e}")

    finally:
        conn.close()
        print("🔒 Conexão com o banco de dados fechada.")

if __name__ == "__main__":
    while True:
        coletar_dados()
        print("⏳ Aguardando 10 minutos para a próxima coleta...\n")
        time.sleep(600)
