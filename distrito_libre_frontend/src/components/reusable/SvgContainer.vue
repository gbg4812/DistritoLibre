<script setup lang="ts">
const props = defineProps({
    viewBox: {
        type: String,
        default: "0 0 500 500",
    },
});
</script>

<template>
    <svg :viewBox="props.viewBox">
        <slot />
    </svg>
</template>

<style scoped></style>
