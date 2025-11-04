🧩 Contexto

O projeto tem como objetivo construir uma API RESTful para cadastro, consulta e importação de produtos, com foco em clareza, escalabilidade e facilidade de manutenção. A aplicação não possui frontend, mas precisa ser facilmente integrável com qualquer interface externa.

🧠 Decisões Tomadas
1. Framework: FastAPI
- Escolhido por sua performance, simplicidade e suporte nativo à documentação Swagger.
- Permite validação automática com Pydantic e tipagem explícita nos endpoints.
2. Estrutura de Pastas Modular
- Separação clara entre responsabilidades:
- controllers/: define os endpoints da API
- services/: contém a lógica de negócio
- models/: define os modelos de dados e schemas
- database.py: gerencia a conexão com o banco
- Essa organização facilita testes, manutenção e escalabilidade.
3. ORM: SQLAlchemy
- Usado para abstrair operações no banco de dados.
- Permite manipulação de dados com segurança e flexibilidade.
4. Documentação: Swagger UI
- Gerada automaticamente pelo FastAPI.
- Permite testes diretos dos endpoints via navegador.
- Elimina a necessidade de frontend durante a fase de validação.
5. Execução: Docker
- Utilização de Dockerfile e docker-compose.yml para padronizar o ambiente.
- Facilita a execução em qualquer máquina, sem dependências locais.

🔍 Alternativas Consideradas
- Frameworks: Flask, Django REST Framework
- Banco de dados: PostgreSQL, MySQL
- Execução local sem Docker

✅ Justificativas
- FastAPI oferece melhor performance e documentação automática.
- Docker garante portabilidade e consistência de ambiente.
- A estrutura modular permite evolução futura com mínima refatoração.

📌 Conclusão
A arquitetura adotada prioriza clareza, organização e escalabilidade. Cada decisão foi tomada com foco em entregar uma API funcional, testável e pronta para evoluir. O projeto está preparado para crescer com segurança e facilidade de manutenção.



🗂️ Banco de Dados: SQLite (com observação sobre Postgres)
Decisão original: O banco de dados planejado para este projeto era o PostgreSQL, por ser mais robusto e adequado para ambientes de produção.

Decisão aplicada: Durante o desenvolvimento, foi utilizado o SQLite por engano. No entanto, essa escolha se mostrou funcional para o escopo do desafio, permitindo prototipagem rápida e persistência local sem dependências externas.

Justificativa complementar:

- SQLite é leve e fácil de configurar
- Ideal para testes e desenvolvimento local
- Permite foco na estrutura da API sem overhead de infraestrutura
Consequência: A troca para PostgreSQL pode ser feita facilmente, já que o projeto utiliza SQLAlchemy, que abstrai o banco de dados. Basta ajustar a string de conexão e configurar o ambiente.

Nota: Em um ambiente de produção ou com múltiplos usuários, o ideal é substituir o SQLite por PostgreSQL, conforme previsto originalmente.

