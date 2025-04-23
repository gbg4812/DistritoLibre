<script setup>
import NavBar from "./components/NavBar.vue";
</script>

<template>
    <NavBar />
    <div class="content">
        <RouterView />
    </div>
</template>

<style>
:root {
    --color-black: #000000ff;
    --color-gray: #d1d1d1ff;
    --color-white: #ffffffff;
    --color-light-cream: #f1efecff;
    --color-cream: #d4c9beff;
    --color-sea-blue: #123458ff;
    --color-bluish-dark: #030303ff;

    --pixel-border: 1px solid black;
}

* {
    margin: 0px;
}

input,
button {
    font-size: 1rem;
    border: var(--pixel-border);
    border-radius: 0px;
    background-color: var(--color-white);
    color: var(--color-black);
    padding: 1rem;
}

label,
p,
a {
    font-size: 1rem;
    text-decoration: none;
}

a,
.clickable {
    cursor: pointer;
}

a:hover,
.clickable:hover {
    color: var(--color-light-cream);
}

button:hover {
    background-color: var(--color-light-cream);
}

input:focus {
    outline: 1px solid var(--color-sea-blue);
}

#app {
    font-family: "DM Sans", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    font-family: "DM Sans", serif;
    font-optical-sizing: auto;
    font-weight: 400;
    font-style: normal;
    color: var(--color-black);
}
</style>

<style scoped>
.content {
    display: flex;
    flex-direction: column;
    margin-top: 4rem;
}
</style>
