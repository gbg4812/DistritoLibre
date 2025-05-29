<script setup lang="ts">
import PostCard from "./PostCard.vue";
import { store } from "../store.ts";
import type { PostOverview } from "../types.ts";
import { getPathData, paramValues } from "../distritoBackend.ts";

const parms = paramValues("tag", store.tags);
console.log(parms);

const { data, error } = getPathData<PostOverview[]>("/posts/", parms);
console.log(error);
</script>

<template>
    <div v-if="data" id="posts-cont">
        <div id="tags-cont">
            <a v-for="tag in store.tags" :key="tag">{{ tag }}</a>
        </div>
        <RouterLink
            v-for="post in data"
            :key="post.title"
            :to="'/posts/post/' + post.title"
        >
            <PostCard :post="post"></PostCard>
        </RouterLink>
    </div>
</template>

<style scoped>
#posts-cont {
    display: flex;
    flex-direction: column;
    margin-left: auto;
    margin-right: auto;
    padding: 1rem;
}
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
    margin: 0.5rem;
}
</style>
