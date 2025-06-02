<script setup lang="ts">
import { ref, useTemplateRef } from "vue";
import { Icon } from "@iconify/vue";

const props = defineProps<{
    name: string;
}>();

const model = defineModel<string>({ default: "" });

const searching = ref(false);
const iconsearch = useTemplateRef("iconsearch");

const data = ref();

function onInput() {
    if (iconsearch.value) {
        searching.value = iconsearch.value.value.length >= 3;
        model.value = iconsearch.value.value;
    }
}
</script>

<template lang="html">
    <div id="iconpicker">
        <input
            id="iconsearch"
            ref="iconsearch"
            :name="props.name"
            type="text"
            @input="onInput"
            @focusin="onInput"
            @focusout="searching = false"
        />
        <div v-if="searching && data" id="options">
            <option
                v-for="icon in data.icons"
                :key="icon"
                class="clickable"
                :value="icon.value"
            >
                <Icon :icon="icon"></Icon>
                {{ icon }}
            </option>
        </div>
    </div>
</template>

<style setup>
#iconpicker {
    position: relative;
    width: 100%;
}
input {
    width: 100%;
}
#options {
    position: absolute;
    background-color: var(--color-white);
    width: inherit;
    border: var(--pixel-border);
}

option {
    padding: 0.2rem;
    border-top: 1px solid var(--color-light-cream);
}
</style>
