/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/static/**/*.{html,js}", "./app/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
