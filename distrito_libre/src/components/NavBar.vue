<script setup>
import { Icon } from "@iconify/vue";
import ContentMenu from "./ContentMenu.vue";
</script>

<template>
    <div class="nav-container">
        <h1>Distrito Libre</h1>

        <ContentMenu class="content-menu"></ContentMenu>
    </div>
</template>

<style scoped>
.nav-container {
    display: flex;
    flex-direction: row;
    align-items: bottom;
    color: white;
    background: black;
    position: fixed;
    top: 0px;
    width: 100%;
    z-index: 1;
    height: 4rem;
}

.nav-container h1 {
    margin-top: auto;
    margin-bottom: auto;
    margin-left: 1rem;
    margin-right: auto;
}
</style>
