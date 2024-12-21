<script setup>
import { Icon } from "@iconify/vue";
</script>

<template>
    <div class="nav-container">
        <h1>Distrito Libre</h1>
        <Icon icon="mingcute:menu-fill" class="menu-symbol" />
    </div>
</template>

<style scoped>
.nav-container {
    display: flex;
    flex-direction: row;
    color: white;
    background: black;
    position: sticky;
    top: 0px;
}

.menu-symbol {
    font-size: 32pt;
    margin: auto;
    margin-right: 0.5em;
}
.nav-container h1 {
    margin: 0.5em;
    margin-right: auto;
}
</style>
