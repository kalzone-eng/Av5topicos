# 🍰 03-receita

Exemplo didático de utilização do **SQLAlchemy ORM** com **MySQL** para representar a relação entre receitas, insumos e o vínculo de cada insumo dentro de uma receita.

O projeto utiliza o **uv** para gerenciar o ambiente virtual e as dependências.

## 📚 Sobre o projeto

O modelo atual possui três entidades principais:

* **Receita** — representa uma receita culinária.
* **Insumo** — representa um item que pode ser usado em diversas receitas.
* **Ingrediente** — representa a associação entre uma receita e um insumo, incluindo quantidade e unidade.

A estrutura do relacionamento é:

```text
Receita
   │
   │ 1:N
   ▼
Ingrediente
   ▲
   │ N:1
   │
Insumo
```

A classe `Ingrediente` funciona como uma **entidade de associação** com chave composta:

* `receita_id` → identifica a receita;
* `insumo_id` → identifica o insumo;
* `quantidade` → quantidade usada na receita;
* `unidade` → unidade de medida, como "lata", "kg" ou "colher de café".

Esse desenho permite reutilizar o mesmo insumo em várias receitas e, ao mesmo tempo, guardar informações específicas de cada relação.

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
* **uv** — gerenciamento do ambiente e dependências

---

## 📦 Gerenciamento do projeto com `uv`

Este projeto usa o `uv` para criar o ambiente virtual e instalar as dependências.

As dependências estão definidas em `pyproject.toml`:

```toml
[project]
name = "03-receita"
version = "0.1.0"
requires-python = ">=3.12"

dependencies = [
    "pymysql>=1.2.3",
    "sqlalchemy>=2.0.54",
]
```

### Instalando o `uv`

Se o `uv` ainda não estiver instalado, consulte:

https://docs.astral.sh/uv/

Depois de instalar, confirme com:

```bash
uv --version
```

---

## 📥 Instalando as dependências

No diretório do projeto, execute:

```bash
uv sync
```

Esse comando cria o ambiente virtual `.venv`, instala as dependências e mantém a reprodução das versões do projeto.

---

## 🐬 Configuração do MySQL

O código usa a seguinte string de conexão:

```python
mysql+pymysql://root:root@localhost:3306/meubanco
```

| Configuração | Valor       |
| ------------ | ----------- |
| Banco        | MySQL       |
| Usuário      | `root`      |
| Senha        | `root`      |
| Host         | `localhost` |
| Porta        | `3306`      |
| Database     | `meubanco`  |

Antes de executar o projeto, crie o banco:

```sql
CREATE DATABASE meubanco;
```

### ⚠️ Credenciais

As credenciais usadas no exemplo são apenas didáticas. Em uma aplicação real, prefira variáveis de ambiente ou arquivos de configuração seguros.

---

## ▶️ Executando o projeto

A execução mais direta do exemplo atual é:

```bash
uv run python receitas.py
```

Esse arquivo cria as tabelas automaticamente e insere uma receita de exemplo com seus insumos e quantidades.

---

## 🗄️ Criação das tabelas

O projeto utiliza:

```python
Base.metadata.create_all(engine)
```

para criar as tabelas caso elas ainda não existam.

As tabelas criadas são:

```text
tabela_receitas
tabela_insumos
tabela_ingredientes
```

---

## 🧱 Modelo de dados

### `Receita`

Representa uma receita culinária:

```python
class Receita(Base):
    __tablename__ = "tabela_receitas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(Text)

    ingredientes: Mapped[List["Ingrediente"]] = relationship(back_populates="receita")
```

Cada receita possui:

* identificador;
* nome;
* tempo de preparo;
* modo de preparo;
* lista de ingredientes associados.

---

### `Insumo`

Representa um material ou item que pode aparecer em várias receitas:

```python
class Insumo(Base):
    __tablename__ = "tabela_insumos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))

    ingredientes: Mapped[List["Ingrediente"]] = relationship(back_populates="insumo")
```

Cada insumo tem:

* identificador;
* nome;
* relacionamento com as receitas em que é usado.

---

### `Ingrediente`

Representa a ligação entre uma receita e um insumo, incluindo os dados específicos do relacionamento:

```python
class Ingrediente(Base):
    __tablename__ = "tabela_ingredientes"

    insumo_id: Mapped[int] = mapped_column(ForeignKey("tabela_insumos.id"), primary_key=True)
    receita_id: Mapped[int] = mapped_column(ForeignKey("tabela_receitas.id"), primary_key=True)

    insumo: Mapped["Insumo"] = relationship(back_populates="ingredientes")
    receita: Mapped["Receita"] = relationship(back_populates="ingredientes")

    unidade: Mapped[str] = mapped_column(String(250))
    quantidade: Mapped[float] = mapped_column(Float())
```

Essa classe consegue representar, por exemplo, que a receita "Bolo de milho" usa:

* 1 lata de milho;
* 1 lata de leite;
* 1 kg de açúcar;
* 3 ovos;
* 1 colher de café de fermento;
* 0,5 lata de óleo.

---

## ✅ Objetivo do exemplo

O objetivo do projeto é demonstrar como modelar:

1. uma relação de muitos para muitos entre receitas e insumos;
2. o uso de uma entidade associativa com atributos próprios;
3. o funcionamento do SQLAlchemy com `relationship()` e `ForeignKey`;
4. a criação automática do esquema no banco de dados.

Esse padrão é muito útil em modelos de culinária, cardápios, estoque e controle de materiais.


Um insumo também possui uma relação reversa com as receitas e com suas associações:

```python
receitas: Mapped[List["Ingrediente"]]
```

---

## 🔗 `relationship()` e `back_populates`

O projeto também demonstra como criar relacionamentos bidirecionais utilizando o SQLAlchemy.

Em `Receita`:

```python
ingredientes = relationship(back_populates="receita")
```

Em `Insumo`:

```python
ingredientes = relationship(back_populates="insumo")
```

Em `Ingrediente`:

```python
insumo = relationship(back_populates="ingredientes")
receita = relationship(back_populates="ingredientes")
```

O `back_populates` informa ao SQLAlchemy qual é o atributo correspondente no outro lado da relação.

Assim, podemos navegar pelos objetos:

```python
r1.ingredientes
```

e:

```python
item.insumo
```

Por exemplo:

```python
for item in r1.ingredientes:
    print(
        item.insumo.nome,
        item.quantidade,
        item.unidade
    )
```

---

## 💾 Persistindo os dados

Depois de criar os objetos e estabelecer os relacionamentos:

```python
ir1 = Ingrediente(
    insumo=i1,
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
