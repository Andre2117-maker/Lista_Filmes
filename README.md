🎬 Projeto Django – Lista de Filmes

Este é um projeto simples desenvolvido com Django, que permite adicionar, listar e remover filmes, além de atribuir uma nota e descrição para cada um.

🚀 Funcionalidades

✅ Adicionar filmes com título, descrição e nota

🗑️ Remover filmes da lista

💬 Mensagens automáticas de sucesso/erro

🎨 Interface estilizada com HTML + CSS

💾 Banco de dados SQLite (padrão do Django)

🧠 Tecnologias Utilizadas

Python 3.12

Django 5

HTML5 + CSS3

SQLite (banco padrão do Django)

⚙️ Como Rodar o Projeto Localmente
1️⃣ Clonar o repositório
git clone https://github.com/Andre2117-maker/Lista_Filmes.git
cd project-django

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate # no Windows
ou
source venv/bin/activate # (Linux/Mac)

3️⃣ Instalar as dependências
pip install -r requirements.txt

4️⃣ Aplicar as migrações do banco de dados
python manage.py migrate

5️⃣ Rodar o servidor
python manage.py runserver

6️⃣ Acessar no navegador

👉 http://127.0.0.1:8000/

🧩 Estrutura de Pastas
project-django/
│
├── app/
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│ └── filmes.html
│
├── project_django/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

✨ Autor

André Henrique De Almeida Lima — Engenharia da Computação
💼 Projeto desenvolvido para fins de aprendizado e prática com Django.
