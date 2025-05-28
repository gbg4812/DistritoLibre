<script setup lang="ts">
defineEmits(["close"]);
</script>

<template>
    <div id="wraper">
        <div id="content" class="black-text">
            <button class="white-text" type="button" @click="$emit('close')">
                Close
            </button>
            <div id="customcont">
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<style scoped>
#wraper {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
    padding: 5rem;
}

#content {
    display: grid;
    grid-template-rows: min-content 1fr;
    max-width: 100%;
    max-height: 100%;
}

#customcont {
    grid-row: 2;
    border: var(--pixel-border);
    overflow: auto;
}

button {
    grid-row: 1;
}
</style>
