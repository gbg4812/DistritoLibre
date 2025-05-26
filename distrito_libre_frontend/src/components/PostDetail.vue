<script setup>
import { marked } from "marked";
import { useRoute, useRouter } from "vue-router";
import { APIBASEURL } from "../constants";
import { ref } from "vue";

const content = ref("");
const route = useRoute();
const url = new URL("/api/posts/detail/" + route.params.name + "/", APIBASEURL);
console.log(route.params.id);
fetch(url, { credentials: "include" })
    .then((response) => response.json())
    .then((data) => marked.parse(data.content))
    .then((res) => (content.value = res));
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
