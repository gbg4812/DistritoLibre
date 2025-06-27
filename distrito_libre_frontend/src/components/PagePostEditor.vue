<script setup lang="ts">
import type { Post } from "../types.ts";
import { ref } from "vue";
import IconifyPicker from "./reusable/IconifyPicker.vue";
import { getPost, isString, postPost } from "../distritoBackend.ts";
import EditorWraper from "./EditorWraper.vue";
import { useRoute, useRouter } from "vue-router";
const mode = ref<"create" | "update">("create");
const isReady = ref(true);
const newPost = ref<Post>({
    id: 0,
    title: "",
    icon: "",
    description: "",
    content: "",
    tags: [],
});

const route = useRoute();
const router = useRouter();
console.log(route.params.id);
if (route.params.id != "new") {
    mode.value = "update";
    isReady.value = false;
    if (isString(route.params.id)) {
        getPost(Number(route.params.id)).then((post) => {
            newPost.value = post;
            isReady.value = true;
        });
    }
}
function onPost() {
    postPost(newPost.value);
    router.push("/posts/manager/");
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
        <EditorWraper
            v-if="isReady"
            v-model="newPost.content"
            name="content"
        ></EditorWraper>

        <label for="icon">Icon</label>
        <IconifyPicker
            v-if="isReady"
            v-model="newPost.icon"
            name="icon"
        ></IconifyPicker>
        <button type="submit">{{ mode }}</button>
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
