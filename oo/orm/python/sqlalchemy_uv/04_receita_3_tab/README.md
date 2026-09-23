# 🍰 03-receita

Exemplo didático de utilização do **SQLAlchemy ORM** com **MySQL**, demonstrando como representar receitas, ingredientes e seus relacionamentos utilizando classes Python.

O projeto utiliza o **uv** para gerenciamento do ambiente virtual, dependências e execução da aplicação.

## 📚 Sobre o projeto

O exemplo possui três entidades principais:

* **Receita** — representa uma receita culinária.
* **Ingrediente** — representa um ingrediente.
* **IngredienteNaReceita** — representa a associação entre uma receita e um ingrediente, armazenando também quantidade e unidade.

O modelo pode ser representado da seguinte forma:

```text
Receita
   │
   │ 1:N
   ▼
IngredienteNaReceita
   ▲
   │ N:1
   │
Ingrediente
```

`IngredienteNaReceita` funciona como uma **tabela associativa**, permitindo representar o relacionamento entre receitas e ingredientes e, ao mesmo tempo, armazenar informações adicionais sobre esse relacionamento.

Por exemplo:

```text
Bolo de milho
    ├── 1 lata de milho
    ├── 1 lata de leite
    ├── 1 kg de açúcar
    ├── 3 ovos
    ├── 1 colher de café de fermento
    └── 0,5 lata de óleo
```

---

## 🛠️ Tecnologias utilizadas

* **Python >= 3.12**
* **SQLAlchemy** — mapeamento objeto-relacional (ORM)
* **PyMySQL** — driver para conexão com MySQL
* **MySQL** — banco de dados
* **uv** — gerenciamento de ambiente e dependências

---

## 📦 Gerenciamento do projeto com `uv`

Este projeto utiliza o **uv** para gerenciar o ambiente virtual e as dependências Python.

As dependências do projeto estão declaradas no arquivo `pyproject.toml`:

```toml
[project]
name = "03-receita"
version = "0.1.0"
requires-python = ">=3.12"

dependencies = [
    "pymysql>=1.1.0",
    "sqlalchemy>=2.0.0",
]
```

O `uv` também mantém o arquivo `uv.lock`, que registra as versões resolvidas das dependências.

### Instalando o `uv`

Caso ainda não tenha o `uv` instalado, consulte a documentação oficial:

https://docs.astral.sh/uv/

Depois de instalado, verifique a instalação com:

```bash
uv --version
```

---

## 📥 Instalando as dependências

Depois de clonar o projeto, entre no diretório e execute:

```bash
uv sync
```

O comando `uv sync` irá:

1. criar o ambiente virtual `.venv`, caso ainda não exista;
2. instalar as dependências definidas no `pyproject.toml`;
3. utilizar o `uv.lock` para reproduzir as versões registradas.

Não é necessário executar `pip install` manualmente.

---

## 🐬 Configuração do MySQL

O código utiliza a seguinte URL de conexão:

```python
mysql+pymysql://root:root@localhost:3306/meubanco
```

Isso corresponde a:

| Configuração | Valor       |
| ------------ | ----------- |
| Banco        | MySQL       |
| Usuário      | `root`      |
| Senha        | `root`      |
| Host         | `localhost` |
| Porta        | `3306`      |
| Database     | `meubanco`  |

Antes de executar o programa, crie o banco de dados:

```sql
CREATE DATABASE meubanco;
```

### ⚠️ Credenciais

As credenciais utilizadas no exemplo são apenas para fins didáticos.

Em uma aplicação real, evite deixar usuário e senha diretamente no código-fonte. Prefira utilizar variáveis de ambiente ou outra forma segura de configuração.

---

## ▶️ Executando o projeto

Depois de instalar as dependências:

```bash
uv sync
```

o projeto pode ser executado utilizando o `uv`.

### Utilizando o script do projeto

O `pyproject.toml` define o seguinte comando de entrada:

```toml
[project.scripts]
03-receita = "03_receita:main"
```

Isso permite executar o projeto através de:

```bash
uv run 03-receita
```

Para que esse comando funcione, o módulo `03_receita` precisa possuir uma função `main()`.

Por exemplo:

```python
def main():
    # código da aplicação
    ...


if __name__ == "__main__":
    main()
```

### Executando diretamente o módulo

Também é possível executar o arquivo Python diretamente:

```bash
uv run python 03_receita.py
```

---

## 🗄️ Criação das tabelas

O programa utiliza:

```python
Base.metadata.create_all(engine)
```

para criar as tabelas definidas pelos modelos caso elas ainda não existam.

As tabelas criadas são:

```text
tabela_receitas
tabela_ingredientes
tabela_ingrediente_na_receita
```

---

## 🧱 Modelo de dados

### `Receita`

Representa uma receita:

```python
class Receita(Base):
    __tablename__ = "tabela_receitas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(Text)
```

Cada receita possui:

* identificador;
* nome;
* tempo de preparo;
* modo de preparo.

Além disso, possui uma relação com `IngredienteNaReceita`:

```python
ingredientes: Mapped[List["IngredienteNaReceita"]]
```

---

### `Ingrediente`

Representa um ingrediente:

```python
class Ingrediente(Base):
    __tablename__ = "tabela_ingredientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
```

Um ingrediente também possui uma relação reversa com as receitas:

```python
receitas: Mapped[List["IngredienteNaReceita"]]
```

---

### `IngredienteNaReceita`

Representa a associação entre uma receita e um ingrediente:

```python
class IngredienteNaReceita(Base):
    __tablename__ = "tabela_ingrediente_na_receita"
```

Possui duas chaves estrangeiras:

```python
ingrediente_id
receita_id
```

que também formam uma **chave primária composta**.

Além disso, a associação possui informações próprias:

```python
quantidade
unidade
```

Isso é importante porque a quantidade de um ingrediente depende da receita.

Por exemplo:

```text
Bolo de milho      → 3 ovos
Bolo de chocolate  → 2 ovos
Omelete            → 3 ovos
```

Portanto, `quantidade` não pertence à tabela `Ingrediente`. Ela pertence ao relacionamento entre ingrediente e receita.

---

## 🔗 `relationship()` e `back_populates`

O projeto também demonstra como criar relacionamentos bidirecionais utilizando o SQLAlchemy.

Em `Receita`:

```python
ingredientes = relationship(
    back_populates="receita"
)
```

Em `IngredienteNaReceita`:

```python
receita = relationship(
    back_populates="ingredientes"
)
```

O `back_populates` informa ao SQLAlchemy qual é o atributo correspondente no outro lado da relação.

O mesmo acontece entre `Ingrediente` e `IngredienteNaReceita`.

Assim, podemos navegar pelos objetos:

```python
r1.ingredientes
```

e:

```python
item.ingrediente
```

Por exemplo:

```python
for item in r1.ingredientes:
    print(
        item.ingrediente.nome,
        item.quantidade,
        item.unidade
    )
```

---

## 💾 Persistindo os dados

Depois de criar os objetos e estabelecer os relacionamentos:

```python
ir1 = IngredienteNaReceita(
    ingrediente=i1,
    receita=r1,
    quantidade=1,
    unidade="lata"
)
```

é possível adicionar a receita à sessão:

```python
session.add(r1)
```

e confirmar a transação:

```python
session.commit()
```

O SQLAlchemy acompanha os objetos relacionados e realiza a persistência necessária.

---

## 📁 Estrutura do projeto

Uma estrutura simples pode ser:

```text
03-receita/
├── .venv/
├── 03_receita.py
├── pyproject.toml
├── uv.lock
└── README.md
```

O diretório `.venv` é criado e gerenciado pelo `uv`, mas **não deve ser versionado no Git**.

Recomenda-se adicionar ao `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
```

---

## 🚀 Fluxo rápido

Depois de clonar o projeto, o fluxo básico é:

```bash
# entrar no projeto
cd 03-receita

# instalar/sincronizar dependências
uv sync

# executar
uv run 03-receita
```

Se o banco MySQL estiver configurado e disponível, o programa poderá criar as tabelas e inserir os dados de exemplo.

---

## 🧪 O que este exemplo demonstra

Este projeto pode ser utilizado como exemplo para estudar:

* [x] Python e orientação a objetos
* [x] SQLAlchemy ORM
* [x] `DeclarativeBase`
* [x] `Mapped`
* [x] `mapped_column`
* [x] chaves primárias
* [x] chaves estrangeiras
* [x] chave primária composta
* [x] `relationship()`
* [x] `back_populates`
* [x] relacionamentos `1:N`
* [x] tabelas associativas
* [x] `Session`
* [x] `session.add()`
* [x] `session.commit()`
* [x] `Base.metadata.create_all()`
* [x] gerenciamento de dependências com `uv`
* [x] `pyproject.toml`
* [x] `uv.lock`

---

## ⚠️ Observações

Este projeto possui finalidade principalmente **didática**.

Em uma aplicação real, alguns aspectos poderiam ser aprimorados:

* utilizar variáveis de ambiente para as credenciais do banco;
* utilizar migrations com **Alembic**;
* adicionar validações;
* tratar exceções e realizar `rollback` quando necessário;
* separar modelos, configuração do banco e regras de negócio;
* configurar adequadamente `cascade` nos relacionamentos;
* adicionar testes automatizados;
* evitar dados de exemplo diretamente no código de produção.

---

## 📄 Licença

Este projeto é um exemplo educacional e pode ser utilizado livremente para estudos.
