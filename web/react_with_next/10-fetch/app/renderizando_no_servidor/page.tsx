export default async function PostsPage() {

  // busca dados na internet
  const res = await fetch('https://jsonplaceholder.typicode.com/posts', {
    cache: 'no-store', // sempre busca dados frescos
  });

  if (!res.ok) {
    throw new Error('Falha ao buscar os posts');
  }

  // espera a resposta da API e converte a resposta para JSON
  const posts = await res.json();

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