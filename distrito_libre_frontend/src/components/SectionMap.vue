<script setup>
import SvgComponent from "./SvgComponent.vue";
import SvgContainer from "./SvgContainer.vue";
import { store } from "../store";
import { politicalMap } from "../constants";
import router from "../router";

const nextStep = (id) => {
    store.section = id;
    router.push("/buildings");
};
</script>

<template>
    <div>
        <SvgContainer id="svgcont" viewBox="0 0 1920 1080">
            <SvgComponent url="./assets/sectors/sectors.context.svg" />
            <SvgComponent
                v-for="index in 9"
                :key="index"
                or
                :url="`./assets/sectors/sectors.${index}.svg`"
                :name="politicalMap[store.plane][index - 1]"
                @svg-click="nextStep(id)"
            />
        </SvgContainer>
    </div>
</template>

<style scoped>
#svgcont {
    height: calc(100vh - 4rem);
}
</style>
