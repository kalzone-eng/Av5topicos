'use client';

import { useEffect, useState } from 'react';

export default function PostsList() {

  // cria uma variável de estado para conter
  // os posts que serão mostrados depois
  const [posts, setPosts] = useState([]);
  
  // primeiro recebe os dados, 
  // depois desenha a tela
  useEffect(() => {
    // busca dados na internet
    fetch('https://jsonplaceholder.typicode.com/posts')
      // quando chegar a resposta...
      .then((res) => {
        if (!res.ok) throw new Error('Erro na requisição');
        // retorna dados em json
        return res.json();
      })
      // coloca os dados na variável de estado "posts"
      .then((data) => setPosts(data))
  }, []);

  
  return (
   <main style={{ padding: '2rem' }}>
      <h1>Lista de Posts</h1>
      <ul>

        {/* percorre os posts...  */}
        {posts.map((post) => (
          
          <li key={post.id} style={{ marginBottom: '1rem' }}>
            <h3>{post.title}</h3>
            <p>{post.body}</p>
          </li>

        ))}
      </ul>
    </main>
  );
}