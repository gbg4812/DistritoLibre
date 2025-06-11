<script setup lang="ts">
import { Planes } from "../constants.js";
import { store } from "../store.js";
import { useRouter } from "vue-router";
import PlanesMenu from "./PlanesMenu.vue";

const router = useRouter();

function setPlane(plane: string) {
    store.plane = plane;
    router.push("/sections");
}
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
}
#cont {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 100%;
}
</style>
