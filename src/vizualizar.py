import sqlite3

DB_PATH = r"C:\Users\Jean\Desktop\ferramenta\PythonProject\src\novo_reddit_data.db"


def exibir_dados():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()


    cursor.execute("SELECT titulo, autor, subreddit, url, data_publicacao, conteudo, upvotes FROM posts LIMIT 10;")
    posts = cursor.fetchall()

    print("\n📌 POSTS NO BANCO DE DADOS:")
    for post in posts:
        titulo, autor, subreddit, url, data_publicacao, conteudo, upvotes = post
        print(
            f"\n📝 {titulo}\n👤 Autor: {autor} | 🌍 Subreddit: {subreddit}\n🔗 URL: {url}\n📅 Publicado em: {data_publicacao}\n👍 Upvotes: {upvotes}\n📝 Conteúdo: {conteudo[:200]}...")


    cursor.execute("SELECT post_url, autor, data_comentario, conteudo FROM comentarios LIMIT 10;")
    comentarios = cursor.fetchall()

    print("\n💬 COMENTÁRIOS NO BANCO DE DADOS:")
    for comentario in comentarios:
        post_url, autor, data_comentario, conteudo = comentario
        print(
            f"\n🔗 Post: {post_url}\n👤 Autor: {autor}\n📅 Comentado em: {data_comentario}\n💬 {conteudo[:200]}...")

    conn.close()


if __name__ == "__main__":
    exibir_dados()
