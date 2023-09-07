import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: "0.0.0.0",
    proxy: {
      "/api": {
        target: "http://backend:8000/api/",
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});
