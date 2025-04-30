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
    top: 0%;
    left: 0%;
    width: 100vw;
    height: 100vh;
}

#content {
    display: flex;
    margin: 10%;
    flex-direction: column;
    border: var(--pixel-border);
    z-index: 2;
}

button {
    align-self: end;
}
</style>
