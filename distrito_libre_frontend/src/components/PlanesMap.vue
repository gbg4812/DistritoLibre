<script setup>
import SvgComponent from "./SvgComponent.vue";
import SvgContainer from "./SvgContainer.vue";
import { Planes, selectionStage } from "../constants.js";
import { store } from "../store";
import router from "../router.js";

function setPlane(plane) {
    store.plane = plane;
    router.push("/sections");
}
</script>

<template>
    <div>
        <SvgContainer>
            <SvgComponent
                url="./assets/planes.0.svg"
                @svg-click="setPlane(Planes.CENTER_RIGHT)"
            />
            <SvgComponent
                url="./assets/planes.1.svg"
                @svg-click="setPlane(Planes.CENTER)"
            />
            <SvgComponent
                url="./assets/planes.2.svg"
                @svg-click="setPlane(Planes.CENTER_LEFT)"
            />
        </SvgContainer>
    </div>
</template>

<style scoped></style>
