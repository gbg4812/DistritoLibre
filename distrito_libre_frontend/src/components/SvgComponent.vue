<script setup>
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

let promise = fetch(props.url);

const content = ref("");

promise
    .then((resp) => resp.text())
    .then((svgcode) => {
        content.value = ref(svgcode);
    });

function onClick(event) {
    if (event.target.id != "svg-cont" && event.target.localName != "svg") {
        if (props.name) emit("svg-click", props.name);
        else emit("svg-click", event.target.id);
    }
}
</script>

<template>
    <g
        id="svg-cont"
        class="svg-cont"
        @click="onClick"
        v-html="content.value"
    ></g>
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
