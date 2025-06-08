<script setup lang="ts">
import { Crepe } from "@milkdown/crepe";
import { onMounted, onUnmounted, useTemplateRef } from "vue";
import "@milkdown/crepe/theme/common/style.css";
import "@milkdown/crepe/theme/frame.css";

const editor = useTemplateRef("editor");
let crepe: Crepe | null = null;

onMounted(() => {
    crepe = new Crepe({
        root: editor.value,
    });
    crepe.create();
});

onUnmounted(() => {
    crepe?.destroy();
});
</script>

<template lang="html">
    <div id="editor" ref="editor"></div>
</template>

<style>
/* Basic styling example */
.milkdown .editor {
    border: var(--pixel-border);
    margin: 0;
    padding: 1rem;
    box-shadow: 5px 5px black;
}
</style>
