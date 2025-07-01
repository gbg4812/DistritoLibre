<script setup lang="ts">
import { ref } from "vue";
import SearchBar from "./SearchBar.vue";
import { similarity } from "../../algorithms";
const props = defineProps<{
    name: string;
    data: string[];
}>();

const model = defineModel<string>({ default: "" });

const sorted_data = ref(props.data);
sorted_data.value.sort();

function onInput(value: string) {
    console.log("Sorting!");
    sorted_data.value = sorted_data.value.sort((a, b) => {
        const asim = similarity(value.toLowerCase(), a.toLowerCase());
        const bsim = similarity(value.toLowerCase(), b.toLowerCase());
        return bsim - asim;
    });
}
</script>
<template>
    <div>
        <SearchBar
            v-model="model"
            :name="props.name"
            :data="sorted_data"
            @input="onInput"
        >
        </SearchBar>
    </div>
</template>
