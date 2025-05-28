<script setup lang="ts">
import PostCard from "./PostCard.vue";
import { store } from "../store.ts";
import { ref } from "vue";
import { APIBASEURL } from "../constants.ts";
import type { PostOverview } from "../types.ts";

const posts = ref<PostOverview[]>();

async function fetchPosts() {
    try {
        const reqUrl = new URL("/api/posts/", APIBASEURL);
        for (const tag of store.tags) {
            reqUrl.searchParams.append("tag", tag);
        }

        const response = await fetch(reqUrl);
        if (!response.ok) {
            throw new Error("Network connection error!");
        }
        const data = await response.json();
        posts.value = data;
    } catch (error) {
        console.error("Problem fetching the Post!", error);
    }
}

fetchPosts();
</script>

<template>
    <div v-if="posts" id="posts-cont">
        <div id="tags-cont">
            <a v-for="tag in store.tags" :key="tag">{{ tag }}</a>
        </div>
        <RouterLink
            v-for="post in posts"
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
