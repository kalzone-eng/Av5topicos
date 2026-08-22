'use client';

// vamos usar ESTADO nesta página
import { useState } from "react";

export default function Home() {

  // uma variável de estado do tipo "número"
  const [contador, setContador] = useState(0);

  // código para aumentar o contador
  function handleContador() {
    setContador(Number(contador)+1);
  }

  function handleValorDigitado(e) {
    // pega o valor digitado
    const valor = Number(e.target.value);
    // se não for um número (is not a number -> isNaN)
    if (Number.isNaN(valor)) {
      // avisa ao usuário que fez besteira :-)
      alert("Só pode digitar números!");
    } else {
      // atualiza o valor do contador conforme o que foi digitado
      setContador(valor);  
    }
  }

  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">

        <p>
          Contador:
          <input type="text" value={contador}
            onChange={handleValorDigitado}
          />
        </p>

        <button onClick={handleContador}
          className="cursor-rounded-lg bg-blue-600 py-3 font-semibold text-white transition active:scale-95 hover:bg-blue-700">
          Somar!
        </button>

      </main>
    </div>
  );
}