<script setup>
import SvgComponent from "./SvgComponent.vue";
import SvgContainer from "./SvgContainer.vue";
import { Planes, selectionStage } from "../constants.js";
import { store } from "../store";

function setPlane(plane) {
    console.log("clicked!");
    store.plane = plane;
    store.sel_stage = selectionStage.SECTION;
    window.scrollTo(0, 0);
}
</script>

<template>
    <div>
        <SvgContainer v-if="store.sel_stage == selectionStage.PLANE">
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
