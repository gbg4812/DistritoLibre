<script setup lang="ts">
import type { Post } from "../types.ts";
import { ref } from "vue";
import IconifyPicker from "./reusable/IconifyPicker.vue";
import { getPost, isString, postPost } from "../distritoBackend.ts";
import EditorWraper from "./EditorWraper.vue";
import { useRoute } from "vue-router";
const newPost = ref<Post>({
    id: 0,
    title: "",
    icon: "",
    description: "",
    content: "",
    tags: [],
});

const route = useRoute();
if (isString(route.params.id)) {
    getPost(Number(route.params.id)).then((post) => (newPost.value = post));
}

function onPost() {
    postPost(newPost.value);
}
</script>

<template>
    <form @submit.prevent="onPost">
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
        <EditorWraper v-model="newPost.content" name="content"></EditorWraper>

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
