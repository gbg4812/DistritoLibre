<script setup lang="ts">
import type { Post } from "../backend_types.ts";
import { ref, watch } from "vue";
import IconifyPicker from "./reusable/IconifyPicker.vue";
import SearchList from "./reusable/SearchList.vue";
import { getPost, postPost } from "../distrito_backend.ts";
import { isString } from "../type_utils.ts";
import EditorWraper from "./EditorWraper.vue";
import { useRoute, useRouter } from "vue-router";
import { politicalMap } from "../constants.ts";
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

const sectionTag = ref<string>();
const route = useRoute();
const router = useRouter();

watch(sectionTag, (value) => {
    console.log(value);
});

const sections = [
    ...politicalMap.CENTER,
    ...politicalMap.CENTER_LEFT,
    ...politicalMap.CENTER_RIGHT,
];

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
        <SearchList
            v-model="sectionTag"
            name="sectionserch"
            :data="sections"
        ></SearchList>
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
