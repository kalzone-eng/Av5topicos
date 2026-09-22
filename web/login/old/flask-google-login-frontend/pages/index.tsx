// pages/index.js
"use client";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  const handleLogin = () => {
    // Redirect to Flask backend to start Google OAuth
    window.location.href = "http://localhost:5000/login";
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-2xl font-bold mb-4">Login Demo</h1>
      <button
        onClick={handleLogin}
        className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
      >
        Login with Google
      </button>
    </main>
  );
}
