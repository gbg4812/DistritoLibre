<script setup lang="ts">
import { store } from "../store";
</script>
<template lang="html">
    <div id="tags-cont">
        <a v-for="tag in store.tags" :key="tag">{{ tag }}</a>
    </div>
</template>

<style scoped>
#tags-cont {
    display: flex;
    align-items: center;
    justify-content: start;
    overflow: clip;
}

#tags-cont a {
    background-color: var(--color-sea-blue);
    border: 5px solid var(--color-sea-blue);
    border-radius: 5px;
    color: var(--color-white);
    padding: 0px;
    margin: 0.5rem;
}
</style>
