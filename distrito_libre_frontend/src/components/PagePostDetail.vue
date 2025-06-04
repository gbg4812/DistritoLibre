<script setup lang="ts">
import { marked } from "marked";
import { useRoute } from "vue-router";
import { useDistritoFetch } from "../distritoBackend";
import { ref } from "vue";

const route = useRoute();
const url = "/posts/detail/" + route.params.name + "/";
const content = ref("");
useDistritoFetch(url)
    .get()
    .json()
    .then(({ data }) => {
        return marked.parse(data.value.content);
    })
    .then((code) => (content.value = code));
</script>

<template>
    <div id="content-wrap" v-html="content"></div>
</template>

<style scoped>
#content-wrap {
    margin: auto;
    width: 60rem;
}

#content-wrap > * {
    margin: 0.5rem;
    text-align: justify;
}

#content-wrap :deep(pre) {
    background-color: #afafff;
    padding: 0.5em;
}
#content-wrap :deep(img) {
    max-width: 100%;
}

#content-wrap :deep(a) {
    text-decoration: underline;
    color: var(--color-sea-blue);
}
</style>
