import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import { fileURLToPath, URL } from "node:url";

export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
    server: {
        proxy: {
            "/api": {
                // Adjust '/api' to match the base URL of your Django API endpoints
                target: "http://127.0.0.1:8000",
                changeOrigin: true, // For virtual hosted sites
                rewrite: (path) => path.replace(/^\/api/, ""), // Remove the '/api' prefix when forwarding to Django
            },
        },
    },
});
