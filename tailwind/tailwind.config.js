/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../templates/base/*.html',
    '../templates/base/base.html',
    '../tailwind/*.js',
    "./node_modules/flowbite/**/*.js",
    "../tailwind/node_modules/flowbite/*/.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

