self.__BUILD_MANIFEST = {
  "/": [
    "./static/chunks/pages/index.js"
  ],
  "/auth/callback": [
    "./static/chunks/pages/auth/callback.js"
  ],
  "/dashboard": [
    "./static/chunks/pages/dashboard.js"
  ],
  "__rewrites": {
    "afterFiles": [],
    "beforeFiles": [],
    "fallback": []
  },
  "sortedPages": [
    "/",
    "/_app",
    "/_error",
    "/api/hello",
    "/auth/callback",
    "/dashboard"
  ]
};self.__BUILD_MANIFEST_CB && self.__BUILD_MANIFEST_CB()