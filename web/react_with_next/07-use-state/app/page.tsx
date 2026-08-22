'use client';

// vamos usar ESTADO nesta página
import { useState } from "react";

export default function Home() {

  // uma variável de estado do tipo "número"
  const [contador, setContador] = useState(0);

  // código para aumentar o contador
  function handleContador() {
    setContador(contador + 1);
  }

  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">

        <p>
          Contador: {contador}
        </p>

        <button onClick={handleContador}
          className="cursor-rounded-lg bg-blue-600 py-3 font-semibold text-white transition active:scale-95 hover:bg-blue-700">
          Somar!
        </button>

      </main>
    </div>
  );
}