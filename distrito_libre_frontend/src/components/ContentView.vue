<script setup>
import PostCard from "./PostCard.vue";
import { store } from "../store";
import { ref } from "vue";
import { APIBASEURL } from "../constants";

const posts = ref(null);

fetchBooks();

async function fetchBooks() {
    try {
        const reqUrl = new URL("posts/", APIBASEURL);
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
</script>

<template>
    <div v-if="posts" class="posts-container">
        <PostCard v-for="post in posts" :key="post.title" :post="post" />
    </div>
</template>

<style scoped>
.posts-container {
    display: flex;
    flex-direction: column;
    margin-left: auto;
    margin-right: auto;
    padding: 1rem;
}
</style>
