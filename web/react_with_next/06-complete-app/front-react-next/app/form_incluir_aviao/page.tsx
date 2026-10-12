
'use client';

import { FormEvent, useEffect, useState } from 'react';
import { useRouter } from "next/navigation";

export default function FormIncluirAviao() {

  const [modelo, setModelo] = useState<string>("");
  const [piloto, setPiloto] = useState<string>("");
  const [copiloto, setCopiloto] = useState<string>("");
  const [passageiros, setPassageiros] = useState<string>("");
  const [companhia, setCompanhia] = useState<string>("");

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const [token, setToken] = useState<string | null>(null);

  const router = useRouter();

  // obtém da variável de ambiente o endereço do backend (API)
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;

  useEffect(() => {
    // tenta buscar o token
    const savedToken = localStorage.getItem("token");

    // se não houver token
    if (!savedToken) {
      // encaminha para o login
      router.replace("/form_login");
      return;
    }

    // persiste o token
    setToken(savedToken);

  }, [router]);

  useEffect(() => {
    // se não houver mensagem, encerra
    if (!message) return;

    // exibe a mensagem por 5 segundos
    const timer = setTimeout(() => {
      setMessage("");
    }, 5000);

    return () => clearTimeout(timer);

  }, [message]);

  useEffect(() => {
    if (!error) return;

    const timer = setTimeout(() => {
      setError("");
    }, 5000);

    return () => clearTimeout(timer);

  }, [error]);

  const enviar = async (e?: FormEvent<HTMLFormElement>) => {
    e?.preventDefault();

    setMessage("");
    setError("");
    setLoading(true);

    try {

      const resposta = await fetch(apiUrl + '/aviao', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          modelo,
          piloto,
          copiloto,
          passageiros,
          companhia
        })
      });

      switch (resposta.status) {
        case 200:
        case 201:
          setMessage("Avião cadastrado com sucesso!");

          // limpa os campos
          setModelo("");
          setPiloto("");
          setCopiloto("");
          setPassageiros("");
          setCompanhia("");
          break;

        case 400:
          setError("Dados inválidos. Confira os campos preenchidos.");
          break;

        case 401:
          setError("A sessão expirou. Por favor, faça login novamente!");
          break;

        case 403:
          setError("Você não tem permissão para realizar esta ação.");
          break;

        case 500:
          setError("Erro interno no servidor backend.");
          break;

        default:
          const resultado = await resposta.json();
          setError(resultado.message || resultado.detalhes || "Um erro inesperado ocorreu.");
      }

    } catch (error) {
      console.log('error', error);
      setError("Não foi possível conectar-se ao backend");
    } finally {
      setLoading(false);
    }
  };

  // se não houver token, encerra a página
  if (!token) {
    return null;
  }

  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">

      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">

        <h1 className="text-4xl font-bold tracking-tight text-gray-900 mb-4">
          Cadastrar Avião
        </h1>

        {message && (
          <p className="text-green-600 font-medium">
            {message}
          </p>
        )}

        {error && (
          <p className="text-red-600 font-medium">
            {error}
          </p>
        )}

        <form className="flex flex-col gap-4 w-full" onSubmit={enviar}>

          <input
            type="text"
            name="modelo"
            placeholder="Modelo do avião"
            value={modelo}
            onChange={(e) => setModelo(e.target.value)}
            className="rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
            required
          />

          <input
            type="text"
            name="Piloto"
            placeholder="Piloto"
            value={piloto}
            onChange={(e) => setPiloto(e.target.value)}
            className="rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
            required
          />

          <input
            type="text"
            name="Copiloto"
            placeholder="Copiloto"
            value={copiloto}
            onChange={(e) => setCopiloto(e.target.value)}
            required
            className="rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          />

          <input
            type="number"
            name="Passageiros"
            placeholder="Capacidade de passageiros"
            value={passageiros}
            onChange={(e) => setPassageiros(e.target.value)}
            min="1"
            required
            className="rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          />

          <input
            type="text"
            name="Companhia"
            placeholder="Companhia aérea"
            value={companhia}
            onChange={(e) => setCompanhia(e.target.value)}
            required
            className="rounded-lg border border-gray-300 px-4 py-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          />

          <button
            type="submit"
            disabled={loading}
            className="cursor-pointer bg-blue-600 text-white px-4 py-2 rounded disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "Cadastrando..." : "Cadastrar"}
          </button>

        </form>

      </main>

    </div>
  );
}
