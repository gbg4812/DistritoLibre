<script setup lang="ts">
defineEmits(["close"]);
</script>

<template>
    <div id="wraper">
        <div id="content" class="black-text">
            <button class="white-text" type="button" @click="$emit('close')">
                Close
            </button>
            <slot></slot>
        </div>
    </div>
</template>

<style scoped>
#wraper {
    position: fixed;
    top: 4rem;
    left: 0%;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(40px);
    z-index: 1;
}

#content {
    display: flex;
    flex-direction: column;
    border: var(--pixel-border);
}

button {
    align-self: end;
}
</style>
