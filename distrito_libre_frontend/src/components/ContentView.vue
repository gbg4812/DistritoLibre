<script setup>
import PostCard from "./PostCard.vue";
import { ref } from "vue";

const posts = ref(null);

fetchBooks();

async function fetchBooks() {
    try {
        const response = await fetch(
            "http://127.0.0.1:8000/preguteca/api/posts/"
        );
        if (!response.ok) {
            throw new Error("Network connection error!");
        }
        const data = await response.json();
        console.log(data);
        posts.value = data;
    } catch (error) {
        console.error("problem fetching the Post!");
    }
}
</script>

<template>
    <div v-if="posts" class="posts-container">
        <PostCard v-for="post in posts" :key="post.id" :post="post" />
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
