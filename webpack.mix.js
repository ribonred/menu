const mix = require('laravel-mix');

let staticPath = "./static/build";
let resourcesPath = "./resources";

mix.setResourceRoot("./static/build"); // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg
mix.setPublicPath("./static"); // Path where mix-manifest.json is created

// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes("--browser-sync")) {
  mix.browserSync("localhost:8000");
}

// Now you can use full mix api
// Refer the file that was created in Step 2 to be compile
mix.js(`${resourcesPath}/js/djmix.js`, `${staticPath}/`).vue();
mix.sass(`${resourcesPath}/sass/djmix.scss`, `${staticPath}/`);