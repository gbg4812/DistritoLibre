<script setup lang="ts">
import PostCard from "./PostCard.vue";
import { store } from "../store.ts";
import type { PostOverview } from "../types.ts";
import { useDistritoFetch } from "../distritoBackend.ts";

const parms = new URLSearchParams();
for (const tag of store.tags) {
    parms.append("tag", tag);
}

const { isFinished, data } = useDistritoFetch<PostOverview[]>(
    "/posts/?" + parms.toString(),
)
    .get()
    .json();
</script>

<template>
    <div v-if="isFinished" id="posts-cont">
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
