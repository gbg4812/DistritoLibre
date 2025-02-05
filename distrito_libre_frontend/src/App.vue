<script setup>
// import ContentView from "./components/ContentView.vue";
import NavBar from "./components/NavBar.vue";
import { store } from "./store.js";
import SectionMap from "./components/SectionMap.vue";
import PlanesMap from "./components/PlanesMap.vue";
import { selectionStage } from "./constants.js";
</script>

<template>
    <NavBar />
    <div class="content">
        <PlanesMap v-if="store.sel_stage == selectionStage.PLANE" />
        <SectionMap v-if="store.sel_stage == selectionStage.SECTION" />

        <!-- debug begin -->
        <p>{{ store.sel_stage }}</p>
        <p>{{ store.plane }}</p>
        <p>{{ store.section }}</p>
        <!-- debug end -->

        <!-- <ContentView /> -->
    </div>
</template>

<style>
:root {
    --hover-color: #3a3d3b;
    --background-color: #111211;
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
