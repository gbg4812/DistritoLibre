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
    left: 0%;
    top: 0%;
    width: 100%;
    height: 100%;
    display: block;
    backdrop-filter: blur(40px);
    padding: 4rem;
    z-index: 1;
}

#content {
    display: grid;
    grid-template-rows: 2rem calc(100%-2rem);
    max-height: 100%;
    max-width: 100%;
}

#customcont {
    grid-row: 2;
    border: var(--pixel-border);
    overflow: scroll;
}

button {
    grid-row: 1;
    align-self: end;
}
</style>
