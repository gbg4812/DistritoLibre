<script setup lang="ts">
import { watch } from "vue";
import { onMounted, ref, useTemplateRef } from "vue";
import { isElement } from "../../type_utils.ts";

const props = defineProps<{
    name: string;
    data: string[];
}>();

const emit = defineEmits<{
    (e: "input", value: string): void;
    (e: "change", value: string): void;
}>();

const model = defineModel<string>({ default: "" });

const searching = ref(false);
const searchbar = useTemplateRef("searchbar");

watch(searching, (value, old) => {
    console.log("searching was ", old, "now is ", value);
});

onMounted(() => {
    if (searchbar.value) {
        searchbar.value.value = model.value;
    }
});

function onInput() {
    if (searchbar.value) {
        console.log("firing input!");
        emit("input", searchbar.value.value);
        if (searchbar.value.value.length > 0) {
            searching.value = true;
        } else {
            searching.value = false;
        }
    }
}

function onSelect(event: Event) {
    if (searchbar.value) {
        const target = event.target as HTMLOptionElement;
        searchbar.value.value = target.value;
        model.value = searchbar.value.value;
        emit("change", searchbar.value.value);
        searching.value = false;
    }
}

function onFocusOut(event: FocusEvent) {
    if (!isElement(event.relatedTarget)) {
        searching.value = false;
        return;
    }

    if (
        event.relatedTarget.id != "searchbar" &&
        event.relatedTarget.id != "menuoption"
    )
        searching.value = false;
}
</script>

<template>
    <div id="barsearch">
        <div class="search-wraper">
            <input
                id="searchbar"
                ref="searchbar"
                v-model="model"
                tabindex="0"
                :name="props.name"
                type="text"
                @input="onInput"
                @focusout="onFocusOut"
                @focusin="searching = true"
            />
            <div v-if="searching && props.data" id="options">
                <option
                    v-for="item in props.data"
                    id="menuoption"
                    :key="item"
                    tabindex="0"
                    class="clickable"
                    :value="item"
                    @click="onSelect"
                    @focusout="onFocusOut"
                >
                    {{ item }}
                </option>
            </div>
        </div>
    </div>
</template>

<style setup>
#barsearch {
    display: flex;
    align-items: center;
    justify-content: space-around;
    width: 100%;
}

.search-wraper {
    width: 100%;
    position: relative;
}

input {
    width: 100%;
}

#options {
    position: absolute;
    background-color: var(--color-white);
    border: var(--pixel-border);
    width: 100%;
    z-index: 2;
}

option {
    padding: 0.2rem;
    border-top: 1px solid var(--color-light-cream);
}
</style>
