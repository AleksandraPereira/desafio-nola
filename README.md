![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

🛒 *Desafio Nola*

Este projeto foi desenvolvido como parte de um desafio técnico com o objetivo de criar uma aplicação que facilite o gerenciamento de pedidos, cadastros de clientes e controle de estoque.
A API permite:
- 📌 Cadastro e consulta de clientes
- 📦 Gerenciamento de produtos e estoque
- 🧾 Criação e acompanhamento de pedidos
- 📊 Relatórios analíticos para apoiar a tomada de decisão
A arquitetura foi pensada para ser modular, escalável e de fácil manutenção, utilizando boas práticas de separação em camadas (controllers, services, models e schemas).

🚀 *Tecnologias*
- Python 3.x
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (banco padrão para desenvolvimento)
- Uvicorn (servidor ASGI)
- Pytest (testes automatizados)
  
📂 *Estrutura do projeto*

<img width="684" height="195" alt="Image" src="https://github.com/user-attachments/assets/bf1dd2ef-dff0-4f5c-983e-f3ad6d3c15fe" />


⚙️ *Como rodar o projeto*
- Clone o repositório:
git clone https://github.com/seu-usuario/desafio-nola.git
cd desafio-nola
- Crie e ative o ambiente virtual:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
- Instale as dependências:
pip install -r requirements.txt
- Configure as variáveis de ambiente (crie um arquivo .env na raiz do projeto):
DB_URL=sqlite:///./app.db
- Isso cria o banco app.db dentro da pasta app/.
- Rode a aplicação:
uvicorn app.main:app --reload


📖 *Documentação*
Acesse a documentação interativa em:
- Swagger UI: http://localhost:8000/docs
  
🧪 Testes
Execute os testes com:
pytest


📌 *Endpoints principais*
- Clientes
- POST /customers – Criar cliente
- GET /customers/{id} – Buscar cliente
- Pedidos
- POST /orders – Criar pedido
- GET /orders/{id} – Buscar pedido
- Produtos
- GET /products – Listar produtos
- POST /products – Criar produto
- Lojas
- GET /stores – Listar lojas
- POST /stores – Criar loja
- Analytics
- GET /analytics/sales – Relatórios de vendas

  











