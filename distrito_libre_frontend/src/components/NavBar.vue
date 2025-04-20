<script setup>
import router from "../router";
import ContentMenu from "./ContentMenu.vue";
import { RouterLink } from "vue-router";
defineEmits(["login-start"]);
</script>

<template>
    <div class="nav-container">
        <RouterLink to="/">Distrito Libre</RouterLink>
        <h2>{{ router.currentRoute.value.fullPath }}</h2>
        <button @click="$emit('login-start')">Login</button>
        <ContentMenu></ContentMenu>
    </div>
</template>

<style scoped>
.nav-container {
    display: flex;

    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    width: 100%;
    height: 4rem;
    position: fixed;
    top: 0px;
    z-index: 1;
    box-sizing: border-box;

    color: white;
    background: black;
    border: 1px solid white;
}

.nav-container a {
    font-size: 2em;
    color: white;
    font-weight: 800;
    text-decoration: none;
    margin-left: 1rem;
    margin-right: 1rem;
}
</style>
