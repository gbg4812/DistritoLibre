<script setup lang="ts">
const emit = defineEmits(["click"]);
const props = withDefaults(
    defineProps<{
        padding?: boolean;
    }>(),
    { padding: true },
);
</script>
<template lang="html">
    <div
        :class="{ container: true, padding: props.padding }"
        @click="emit('click')"
    >
        <slot></slot>
    </div>
</template>

<style lang="css">
.container {
    margin: 1rem;
    border: var(--pixel-border);
    box-shadow: 2px 2px black;
    cursor: pointer;
}

.padding {
    padding: 0.5em;
}

.container:hover {
    translate: -2px -2px;
    box-shadow: 4px 4px black;
}
</style>
