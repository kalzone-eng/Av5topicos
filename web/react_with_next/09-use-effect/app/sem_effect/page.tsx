"use client";

import { useState } from "react";

type User = {
  id: number;
  name: string;
  email: string;
};

export default function UsersPage() {
  
  const [users, setUsers] = useState<User[]>([]);
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