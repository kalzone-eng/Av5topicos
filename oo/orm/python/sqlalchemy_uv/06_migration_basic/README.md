# Pessoa com SQLAlchemy 2.x

A classe `Pessoa` mapeia a tabela `tabela_pessoa` e define `nome`, `email` e
`telefone` como `String(250)`. O Alembic gerencia o schema por meio de migrations.
Por padrão, as migrations usam SQLite no arquivo `pessoas.db` do diretório atual.

```bash
uv sync
uv run alembic upgrade head
uv run python teste_pessoa.py
```

O script `teste_pessoa.py` insere três pessoas no banco configurado. Execute
primeiro a migration para criar a tabela. Cada execução adiciona mais três
registros.

Para usar MySQL, defina `DATABASE_URL` com o esquema `mysql+pymysql`
e os dados da sua conexão antes de executar as migrations:

```bash
DATABASE_URL='mysql+pymysql://usuario:senha@localhost:3306/meubanco' \
  uv run alembic upgrade head
```

O banco MySQL informado precisa existir antes de executar as migrations.

Para criar uma migration depois de alterar os modelos:

```bash
uv run alembic revision --autogenerate -m "descricao da alteracao"
uv run alembic upgrade head
```

Revise sempre a migration gerada antes de aplicá-la. Para reverter a migration
mais recente, use `uv run alembic downgrade -1`.
