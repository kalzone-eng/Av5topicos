'use client';

import { GoogleLogin, CredentialResponse } from '@react-oauth/google';

export default function LoginPage() {
  const handleSuccess = async (credentialResponse: CredentialResponse) => {
    try {
      const response = await fetch('http://localhost:5000/api/auth/google', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          credential: credentialResponse.credential, // Send ID token to Flask
        }),
      });

      const data = await response.json();

      if (response.ok) {
        // Save session JWT token to localStorage or HTTP-only cookies
        localStorage.setItem('token', data.token);
        console.log('Authenticated User:', data.user);
        // Redirect to dashboard/home page
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

  return (
    <div style={{ display: 'grid', placeItems: 'center', minHeight: '100vh' }}>
      <h1>Sign in to App</h1>
      <GoogleLogin
        onSuccess={handleSuccess}
        onError={handleError}
        useOneTap
      />
    </div>
  );
}