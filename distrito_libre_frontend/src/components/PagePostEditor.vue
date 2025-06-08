<script setup lang="ts">
import type { Post, StateResponse } from "../types.ts";
import { ref } from "vue";
import IconifyPicker from "./reusable/IconifyPicker.vue";
import { useDistritoFetch } from "../distritoBackend.ts";
import MilkdownWraper from "./MilkdownWraper.vue";
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

    const { data, error } = useDistritoFetch<StateResponse>("/posts/new/")
        .post(newPost)
        .json();
    console.log(data.value);
    console.log(error.value);
};
</script>

<template>
    <form @submit.prevent="postpost">
        <h1>Create New Post</h1>
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
        <MilkdownWraper
            v-model="newPost.content"
            name="content"
        ></MilkdownWraper>

        <label for="icon">Icon</label>
        <IconifyPicker v-model="newPost.icon" name="icon"></IconifyPicker>
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
    width: 100%;
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
