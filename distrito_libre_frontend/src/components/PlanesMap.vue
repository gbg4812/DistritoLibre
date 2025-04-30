<script setup>
import SvgComponent from "./reusable/SvgComponent.vue";
import SvgContainer from "./reusable/SvgContainer.vue";
import { Planes } from "../constants.js";
import { store } from "../store";
import { useRouter } from "vue-router";

const router = useRouter();

function setPlane(plane) {
    store.plane = plane;
    router.push("/sections");
}
</script>

<template>
    <div id="cont">
        <h1>Distrito Libre</h1>
        <h2>Explore Your Convictions</h2>
        <SvgContainer>
            <SvgComponent
                url="assets/planes.0.svg"
                @svg-click="setPlane(Planes.CENTER_RIGHT)"
            />
            <SvgComponent
                url="assets/planes.1.svg"
                @svg-click="setPlane(Planes.CENTER)"
            />
            <SvgComponent
                url="assets/planes.2.svg"
                @svg-click="setPlane(Planes.CENTER_LEFT)"
            />
        </SvgContainer>
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
}
</style>
