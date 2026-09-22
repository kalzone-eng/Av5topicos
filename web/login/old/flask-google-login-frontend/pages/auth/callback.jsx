// pages/auth/callback.js
"use client";
import { useRouter, useSearchParams } from "next/navigation";
import { useEffect } from "react";

export default function AuthCallback() {
  const router = useRouter();
  const params = useSearchParams();

  useEffect(() => {
    const token = params.get("token");
    if (token) {
      localStorage.setItem("jwt", token);
      router.push("/dashboard");
    }
  }, [params, router]);

  return <p>Signing you in...</p>;
}
