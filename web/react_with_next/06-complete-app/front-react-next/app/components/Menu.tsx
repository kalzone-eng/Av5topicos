import Link from "next/link";

export default function Menu() {

  return (
    <nav className="bg-blue-600 text-white p-4">
      <ul className="flex gap-6">

        {/* links para as páginas do sistema: menu de opções */}
        <li><Link href="/">Home</Link></li>
        <li><Link href="/listar_pessoas">Listar pessoas</Link></li>
        <li><Link href="/form_login">Login</Link></li>
        <li><Link href="/form_incluir_pessoa">Nova Pessoa</Link></li>
        <li><Link href="/listar_avioes">Listar aviões</Link></li>
        <li><Link href="/form_incluir_aviao">Novo Avião</Link></li>

      </ul>
    </nav>
  );
}