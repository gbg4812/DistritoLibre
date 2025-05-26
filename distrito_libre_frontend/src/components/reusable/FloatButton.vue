<script setup>
defineEmits(["click"]);
defineProps({
    top: {
        type: String,
        default: "none",
    },
    left: {
        type: String,
        default: "none",
    },
    right: {
        type: String,
        default: "none",
    },
    bottom: {
        type: String,
        default: "none",
    },
});
</script>

<template lang="html">
    <button id="bttn-cnt" @click="$emit('click')">
        <slot></slot>
    </button>
</template>

<style scoped>
#bttn-cnt {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: v-bind(top);
    left: v-bind(left);
    bottom: v-bind(bottom);
    right: v-bind(right);
    z-index: 2;
}
</style>
