<script setup>
import SvgComponent from "./SvgComponent.vue";
import SvgContainer from "./SvgContainer.vue";
import { store } from "../store";
const names = [];
</script>

<template>
    <div>
        <SvgContainer id="svgcont" viewBox="0 0 1920 1080">
            <SvgComponent
                v-for="index in 10"
                :key="index"
                or
                :url="`./assets/sectors/sectors.${index}.svg`"
                :name="names[index]"
                @svg-click="(id) => (store.section = id)"
            />
        </SvgContainer>
    </div>
</template>

<style scoped>
#svgcont {
    height: calc(100vh - 4rem);
}
</style>
