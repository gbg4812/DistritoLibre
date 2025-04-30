<script setup>
import { Icon } from "@iconify/vue/dist/iconify.js";
const props = defineProps({
    icon: {
        type: String,
        required: true,
    },

    name: {
        type: String,
        required: true,
    },
});
</script>

<template>
    <div id="cont">
        <Icon :icon="props.icon" width="10rem" />
        <h3>{{ props.name }}</h3>
    </div>
</template>

<style scoped>
#cont {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 2em;
    border: 1px solid black;
    box-shadow: 5px 5px black;
    aspect-ratio: 1;
}

#cont:hover {
    translate: -5px -5px;
    box-shadow: 10px 10px black;
}
</style>
