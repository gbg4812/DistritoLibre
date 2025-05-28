<script setup lang="ts">
import { ref } from "vue";

const emit = defineEmits(["svg-click"]);

const props = defineProps({
    url: {
        type: String,
        required: true,
    },
    name: {
        type: String,
        required: false,
        default: null,
    },
});

const promise = fetch(props.url);

const content = ref("");

promise
    .then((resp) => resp.text())
    .then((svgcode) => {
        content.value = svgcode;
    })
    .catch(() => console.error("Failed to fetch svg component content!"));

function onClick(event: MouseEvent) {
    const target = event.target as HTMLElement;
    if (target.id != "svg-cont" && target.localName != "svg") {
        if (props.name) emit("svg-click", props.name);
        else emit("svg-click", target.id);
    }
}
</script>

<template>
    <g id="svg-cont" class="svg-cont" @click="onClick" v-html="content"></g>
</template>

<style scoped>
g {
    transform: translate(0px, 0px);
    transition: 0.3s;
}
g:hover {
    transform: translate(0px, -15px);
}
</style>
