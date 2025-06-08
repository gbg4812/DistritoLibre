<script setup lang="ts">
import SvgComponent from "./reusable/SvgComponent.vue";
import SvgContainer from "./reusable/SvgContainer.vue";
import { store } from "../store.ts";
import { politicalMap } from "../constants.ts";
import { useRouter } from "vue-router";
const router = useRouter();

const nextStep = (id: string) => {
    store.tags.push(id);
    router.push("sections/buildings");
};
</script>

<template>
    <div id="secmap">
        <SvgContainer id="svgcont" viewBox="0 0 1920 1080">
            <SvgComponent url="./assets/sectors/sectors.context.svg" />
            <SvgComponent
                v-for="index in 9"
                :key="index"
                or
                :url="`./assets/sectors/sectors.${index}.svg`"
                :name="politicalMap.get(store.plane)[index - 1]"
                @svg-click="nextStep"
            />
        </SvgContainer>
    </div>
</template>

<style scoped>
#svgcont {
    height: calc(100vh - 4rem);
}

#secmap {
    align-self: center;
}
</style>
