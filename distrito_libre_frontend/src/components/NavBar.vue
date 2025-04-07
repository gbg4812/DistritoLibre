<script setup>
import router from "../router";
import ContentMenu from "./ContentMenu.vue";
import { RouterLink } from "vue-router";
</script>

<template>
    <div class="nav-container">
        <RouterLink to="/">Distrito Libre</RouterLink>
        <h2>{{ router.currentRoute.value.fullPath }}</h2>
        <ContentMenu class="content-menu"></ContentMenu>
    </div>
</template>

<style scoped>
.nav-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    color: white;
    background: black;
    position: fixed;
    top: 0px;
    width: 100%;
    z-index: 1;
    height: 4rem;
}

.nav-container a {
    font-size: 2em;
    color: white;
    font-weight: 800;
    text-decoration: none;
    margin-left: 1rem;
    margin-right: 1rem;
}

.content-menu {
    flex-grow: 1;
}
</style>
