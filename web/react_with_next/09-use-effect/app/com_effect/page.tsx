"use client";

import { useEffect, useState } from "react";

type User = {
  id: number;
  name: string;
  email: string;
};

export default function UsersPage() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Este código será executado quando o componente
    // for montado no navegador.

    const data: User[] =
      [
        {
          "id": 1,
          "name": "Leanne Graham",
          "email": "Sincere@april.biz",
        },
        {
          "id": 2,
          "name": "Ervin Howell",
          "email": "Shanna@melissa.tv",
        }
      ];

      setUsers(data);
      setLoading(false);

  }, []);

  if (loading) {
    return <p>Carregando...</p>;
  }

  return (
    <main>
      <h1>Usuários</h1>

      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <strong>{user.name}</strong>
            <br />
            {user.email}
          </li>
        ))}
      </ul>
    </main>
  );
}