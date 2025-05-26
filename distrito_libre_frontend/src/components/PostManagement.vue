<script setup>
import { APIBASEURL } from "../constants";
import { ref } from "vue";

const newPost = ref({});

const postpost = () => {
    const url = new URL("/api/posts/new/", APIBASEURL);
    const data = new FormData();
    for (const [key, value] of Object.entries(newPost.value)) {
        data.set(key, value);
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
    <form>
        <label for="title">Title</label>
        <input v-model="newPost.title" type="text" name="title" />
        <label for="description">Description</label>
        <input v-model="newPost.descritpion" type="text" name="description" />
        <label for="content">Content</label>
        <input
            v-model="newPost.content"
            type="text"
            aria-multiline="true"
            name="content"
        />
        <label for="icon">Icon</label>
        <input
            v-model="newPost.icon"
            type="text"
            aria-multiline="true"
            name="icon"
        />

        <button type="button" @click="postpost">Post</button>
    </form>
</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    padding: 10%;
}

h2 {
    text-align: center;
}

button,
label {
    margin-top: 1rem;
}
</style>
