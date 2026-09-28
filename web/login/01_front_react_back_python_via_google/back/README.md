# Configurações

Crie um arquivo .env com o seguinte conteúdo:

```
GOOGLE_CLIENT_ID=yyy
JWT_SECRET=xxx
```

O ID do cliente Google deverá ser obtido a partir do [Google Cloud](https://console.cloud.google.com).

A frase secreta JWT pode ser uma frase qualquer; sugere-se que seja uma frase longa e não trivial.

# Execução

Para executar o backend:

```
uv run flask --app src/app run
```