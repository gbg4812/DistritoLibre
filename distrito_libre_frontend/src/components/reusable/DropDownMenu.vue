<script setup lang="ts">
import { ref, watch } from "vue";
import { Icon } from "@iconify/vue/dist/iconify.js";

const show_menu = ref(false);
const props = defineProps({
    title: {
        type: String,
        required: true,
    },
});

const icon = ref("tabler:chevron-down");

watch(show_menu, (value) => {
    if (!value) icon.value = "tabler:chevron-right";
    else icon.value = "tabler:chevron-down";
});
</script>

<template>
    <div
        id="wraper"
        @mouseenter="show_menu = true"
        @mouseleave="show_menu = false"
    >
        <div id="title" class="clickable text-m">
            <Icon :icon="icon" />
            <h3>{{ props.title }}</h3>
        </div>
        <div v-if="show_menu" id="content" class="white-text">
            <slot></slot>
        </div>
    </div>
</template>

<style scoped>
#title {
    padding: 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

h3 {
    padding: 0.1em;
}

#wraper {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 100%;
    position: relative;
}

#content {
    position: absolute;
    display: flex;
    flex-direction: column;
    width: 20rem;
    top: 100%;
    right: 0px;

    box-sizing: border-box;
    border-top: 1px solid white;
    padding: 1rem;
}
</style>
