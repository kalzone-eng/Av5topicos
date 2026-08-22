// esta página será um componente de CLIENTE
// isso é necessário para poder armazenar estado
'use client';

import { useEffect, useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const [login, setLogin] = useState("");
  const [senha, setSenha] = useState("");
  const [error, setError] = useState("");
  const [token, setToken] = useState<string | null>(null);

  const router = useRouter();
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;

  {/* useEffect serve para executar um código
    depois que o React renderiza a página.
    Isso é importante pois o localStorage só
    vai ser acessado depois que a página
    estiver toda "desenhada", garantindo
    que o acesso ao localStorage vai
    ser realizado com sucesso */}

  useEffect(() => {
    setToken(localStorage.getItem("token"));
  }, []);

  const handleLogin = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError("");

    try {
      // faz a chamada ao backend, para obter a TOKEN
      const resposta = await fetch(apiUrl + '/login', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ login, senha }),
      });

      // recebe a resposta em json
      const dados = await resposta.json();

      // se a resposta "não deu certo" ...
      if (!resposta.ok) {
        throw new Error(dados.detalhes || "Algo deu errado!");
      }

      //console.log(dados.resultado);
      //console.log(dados.detalhes);

      // se chegou até aqui, armazena a 
      // token no localStorage
      const novoToken = dados.detalhes.token
      localStorage.setItem("token", novoToken);
      setToken(novoToken);

      // encaminha a página para a "raiz" (home)
      router.replace("/");

    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Algo deu errado!");
    }
  }

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  return (
    <div style={{ maxWidth: "300px", margin: "50px auto", textAlign: "center" }}>
      <h1
        className="text-4xl font-bold tracking-tight text-gray-900 mb-4"
      >Login</h1>

      {error &&
        <p style={{ color: "red" }}>{error}</p>
      }

      {/* se hover token, 
      mostra o "logout" */}

      {token && (
        <div>
          <p>Você está logado!!</p>

          <button
            onClick={handleLogout}
            className="cursor-pointer text-blue-600 underline hover:text-blue-900"
          >
            Logout
          </button>
        </div>
      )}

      {/* se não houver token, 
      não está logado, 
      daí mostra o formulário */}

      {!token && 
      <form onSubmit={handleLogin}
        className="flex flex-col gap-4 w-full rounded-xl bg-white p-6 shadow-lg border border-gray-200"
      >
        <input
          type="text"
          placeholder="Login"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          required
          className="rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
        />
        <input
          type="password"
          placeholder="Password"
          value={senha}
          onChange={(e) => setSenha(e.target.value)}
          required
          className="rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
        />
        <button
          type="submit"
          className="cursor-pointer rounded-lg bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700 active:scale-95"
        >
          Entrar
        </button>
      </form>}
    </div>
  );
}