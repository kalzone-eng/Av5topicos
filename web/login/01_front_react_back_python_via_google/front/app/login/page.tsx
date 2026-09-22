'use client';

import { useState } from 'react';
import { GoogleLogin, CredentialResponse } from '@react-oauth/google';

interface UserProfile {
  email: string;
  name: string;
  picture: string;
}

export default function LoginPage() {

  const [user, setUser] = useState<UserProfile | null>(null);

  const handleSuccess = async (credentialResponse: CredentialResponse) => {
    try {
      const response = await fetch('http://localhost:5000/api/auth/google', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          credential: credentialResponse.credential,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem('token', data.token);
        console.log('Authenticated User:', data.user);
        setUser(data.user);
      } else {
        console.error('Authentication failed:', data.error);
      }
    } catch (error) {
      console.error('Network or server error:', error);
    }
  };

  const handleError = () => {
    console.error('Google Sign-In failed');
  };

  const handleLogout = () => {
    // Limpar o token e o estado do utilizador
    localStorage.removeItem('token');
    setUser(null);
  };

  return (
    <div style={{ display: 'grid', placeItems: 'center', minHeight: '100vh' }}>
      <h1>Sign in to App</h1>

{user ? (
        // --- VISÃO APÓS LOGIN (Sinalização) ---
        <div style={{ textAlign: 'center' }}>
          <img
            src={user.picture}
            alt={user.name}
            style={{ borderRadius: '50%', width: '80px', height: '80px' }}
          />
          <h2>Bem-vindo(a), {user.name}!</h2>
          <p>{user.email}</p>

          <button
            onClick={handleLogout}
            style={{
              padding: '8px 16px',
              backgroundColor: '#e53e3e',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              marginTop: '12px'
            }}
          >
            Terminar Sessão
          </button>
        </div>
      ) : (
        // --- VISÃO DE LOGIN ---
        <div style={{ textAlign: 'center' }}>
          <h2>Iniciar Sessão</h2>
          <GoogleLogin
            onSuccess={handleSuccess}
            onError={() => console.error('Erro no Google Sign-In')}
          />
        </div>
      )}

      <GoogleLogin
        onSuccess={handleSuccess}
        onError={handleError}
      />
    </div>
  );
}