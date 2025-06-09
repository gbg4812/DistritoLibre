<script setup lang="ts">
import PostCard from "./PostCard.vue";
import { store } from "../store.ts";
import type { PostOverview } from "../types.ts";
import { useDistritoFetch } from "../distritoBackend.ts";
import TagsBar from "./TagsBar.vue";

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
    <TagsBar></TagsBar>
    <div v-if="isFinished" id="posts-cont">
        <RouterLink
            v-for="post in data"
            :key="post.id"
            :to="'/posts/post/' + post.id"
        >
            <PostCard :post="post"></PostCard>
        </RouterLink>
    </div>
</template>

<style scoped>
#posts-cont {
    display: flex;
    flex-direction: column;
    width: 100%;
}
</style>
