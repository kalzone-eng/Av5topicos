'use client';

import { useEffect, useState } from "react";

export default function Home() {

  // uma variável de estado do tipo "número"
  const [contador, setContador] = useState(0);
  // uma variável de estado do tipo "string"
  const [mensagem, setMensagem] = useState("Valor inicial = zero");
  // uma variável string
  const [titulo, setTitulo] = useState("");

  // só vai executar o código dentro da função
  // depois que a página estiver desenhada
  useEffect(() => {
    setTitulo("Esta é a página do contador");
  }, []);

  // vai executar o código dentro da função
  // toda vez que o contador "mudar"
  useEffect(() => {
    let tmp = mensagem;
    if (contador > 0) {
      setMensagem(tmp + " +1");
    }
    // aqui vai a "lista de dependências"
  }, [contador]);

  // código para aumentar o contador
  function handleContador() {
    setContador(contador + 1);
  }

  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">

          <h1 className="text-2xl">{titulo}</h1>

          <p>Contador: {contador}</p>

          <button onClick={handleContador}
          className="cursor-rounded-lg bg-blue-600 py-3 font-semibold text-white transition active:scale-95 hover:bg-blue-700">
            Somar!
          </button>

          Mensagem: {mensagem}
         
      </main>
    </div>
  );
}