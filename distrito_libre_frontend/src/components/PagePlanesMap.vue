<script setup lang="ts">
import { onMounted, onUnmounted } from "vue";
import PlanesMenu from "./PlanesMenu.vue";
// onMounted(() => {
//     document.body.style.backgroundImage =
//         'url("../../public/assets/ChatGPT Image 2 de jul. del 2025, 00_55_38.png")';
//     document.body.style.backgroundSize = "100%";
// });
//
// onUnmounted(() => {
//     document.body.style.backgroundImage = "none";
//     document.body.style.backgroundSize = "none";
// });
</script>

<template>
    <div id="cont">
        <h1>Distrito Libre</h1>
        <h2>Explore Your Convictions</h2>
        <PlanesMenu></PlanesMenu>
    </div>
</template>

<style scoped>
h1 {
    font-size: 4rem;
    padding: 2rem;
    color: var(--color-cream);
}
h2 {
    color: var(--color-cream);
}
#cont {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 100%;
}
.background {
    background-image: url();
    background-size: 100%;
}
</style>

<style>
body {
    background-image: url("/assets/ChatGPT Image 2 de jul. del 2025, 00_55_38.png");
    background-size: 100%;
}
</style>
