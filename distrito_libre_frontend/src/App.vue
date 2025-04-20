<script setup>
import { ref } from "vue";
import NavBar from "./components/NavBar.vue";
import LoginPopup from "./components/LoginPopup.vue";
const loginpopup = ref(false);
</script>

<template>
    <NavBar @login-start="loginpopup = true" />
    <LoginPopup v-if="loginpopup" @loged-in="loginpopup = false"></LoginPopup>
    <div class="content">
        <RouterView />
    </div>
</template>

<style>
:root {
    --hover-color: #3a3d3b;
    --background-color: #111211;
}

* {
    margin: 0px;
    padding: 0px;
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
    color: #2c3e50;
}

.content {
    display: flex;
    flex-direction: column;
    margin-top: 4rem;
}
</style>
