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

desafio-nola/
 ├── app/
 │   ├── controllers/   # Endpoints da API
 │   ├── models/        # Modelos do banco
 │   ├── schemas/       # Validação e serialização
 │   ├── services/      # Regras de negócio
 │   ├── database.py    # Configuração do banco
 │   └── main.py        # Ponto de entrada
 └── venv/              # Ambiente virtual


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

  📌 *Exemplo de requisição e resposta*
GET /api/PeopleApi/GetAllPeople
Requisição (via cURL):
curl -X 'GET' \
  'https://localhost:7067/api/PeopleApi/GetAllPeople' \
  -H 'accept: application/json'


Resposta (200 OK):
[
  {
    "firstName": "Tanasha Fode",
    "lastName": "Tildenbaum",
    "age": 33
  },
  {
    "firstName": "Tanasha Fode",
    "lastName": "Tildenbaum",
    "age": 33
  }
]








