<script setup lang="ts">
import type { Post } from "../types.ts";
import { APIBASEURL } from "../constants.ts";
import { ref } from "vue";
const newPost = ref<Post>({
    title: "",
    icon: "",
    description: "",
    content: "",
    tags: [],
});

const postpost = () => {
    if (newPost.value == undefined) {
        return;
    }
    const url = new URL("/api/posts/new/", APIBASEURL);
    const data = new FormData();
    for (const [key, value] of Object.entries(newPost.value)) {
        data.set(key, String(value));
    }
    fetch(url, {
        method: "POST",
        body: data,
        credentials: "include",
    })
        .then(
            (resp) => {
                return resp.json();
            },
            (reason) => {
                console.log(reason);
            },
        )
        .then((rsp) => {
            console.log(rsp);
        });
};
</script>

<template>
    <form @submit.prevent="postpost">
        <label for="title">Title</label>
        <input v-model="newPost.title" required type="text" name="title" />
        <label for="description">Description</label>
        <input
            v-model="newPost.description"
            required
            type="text"
            name="description"
        />
        <label for="content">Content</label>
        <textarea
            v-model="newPost.content"
            required
            cols="100"
            rows="10"
            type="text"
            name="content"
        />
        <label for="icon">Icon</label>
        <input v-model="newPost.icon" required type="text" name="icon" />

        <button type="submit">Post</button>
    </form>
</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: stretch;
    padding: 1rem;
}

h2 {
    text-align: center;
}

button,
label {
    margin-top: 1rem;
}

textarea {
    display: block;
    resize: none;
}
</style>
