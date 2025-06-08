<script setup lang="ts">
import { ref, useTemplateRef } from "vue";
import { Icon } from "@iconify/vue";
import { useFetch } from "@vueuse/core";

const props = defineProps<{
    name: string;
}>();

const model = defineModel<string>({ default: "" });

const searching = ref(false);
const iconsearch = useTemplateRef("iconsearch");

const baseurl = new URL("search", "https://api.iconify.design");
baseurl.searchParams.set("limit", "32");
baseurl.searchParams.set("prefix", "tabler");
baseurl.searchParams.set("query", "");

const url = ref(baseurl.toString());
const { data } = useFetch(url, { refetch: searching }).get().json();
const previcon = ref("tabler:list-search");

function onInput() {
    if (iconsearch.value) {
        searching.value = iconsearch.value.value.length >= 3;
        if (searching.value) {
            model.value = iconsearch.value.value;
            baseurl.searchParams.set("query", iconsearch.value.value);
            url.value = baseurl.toString();
            previcon.value = "tabler:list-search";
        }
    }
}

function onClick(event: Event) {
    console.log("selected!");
    if (iconsearch.value) {
        const target = event.target as HTMLOptionElement;
        iconsearch.value.value = target.value;
        searching.value = false;
        previcon.value = iconsearch.value.value;
    }
}
</script>

<template lang="html">
    <div id="iconpicker" @focusout="console.log('focused')">
        <Icon id="previcon" width="2rem" :icon="previcon"></Icon>
        <div class="search-wraper">
            <input
                id="iconsearch"
                ref="iconsearch"
                :name="props.name"
                type="text"
                @input="onInput"
                @focusin="searching = true"
            />
            <div v-if="searching && data" id="options">
                <option
                    v-for="icon in data.icons.slice(0, 8)"
                    :key="icon"
                    class="clickable"
                    :value="icon.value"
                    @click="onClick"
                >
                    <Icon :icon="icon"></Icon>
                    {{ icon }}
                </option>
            </div>
        </div>
    </div>
</template>

<style setup>
#iconpicker {
    display: flex;
    position: relative;
    align-items: center;
    justify-content: space-around;
    width: 100%;
}

.search-wraper {
    width: 100%;
}

#previcon {
    margin: 0.5rem;
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
