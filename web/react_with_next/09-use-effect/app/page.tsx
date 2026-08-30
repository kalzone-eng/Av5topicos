import Link from "next/link";

export default function Home() {

  return (
    <main>
      <h1>useEffect</h1>

      <ul>
        <li>
          <Link href="/sem_effect">Sem useEffect</Link>
        </li>
        <li>
          <Link href="/com_effect">Com useEffect</Link>
        </li>
      </ul>
      
      

    </main>
  );
}