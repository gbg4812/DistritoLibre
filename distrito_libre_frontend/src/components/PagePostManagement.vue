<script setup lang="ts">
import PostCard from "./PostCard.vue";
import { store } from "../store.ts";
import type { PostOverview } from "../types.ts";
import { useDistritoFetch } from "../distritoBackend.ts";
import { APIBASEURL } from "../constants.ts";

const parms = new URLSearchParams();
for (const tag of store.tags) {
    parms.append("tag", tag);
}

const { execute, isFinished, data } = useDistritoFetch<PostOverview[]>(
    "/posts/?" + parms.toString(),
)
    .get()
    .json();

function deletePost(postId: number) {
    const url = new URL(
        "/api/posts/detail/" + postId.toString() + "/",
        APIBASEURL,
    );
    fetch(url, { method: "DELETE" }).then(() => {
        execute();
    });
}
</script>

<template>
    <div v-if="isFinished" id="posts-cont">
        <div v-for="post in data" id="postitem" :key="post.id" class="hflex">
            <RouterLink :to="'/posts/post/' + post.id" style="flex-grow: 1">
                <PostCard :post="post"></PostCard>
            </RouterLink>
            <div class="vflex">
                <button @click="deletePost(post.id)">Delete</button>
                <RouterLink class="clickable" :to="'/posts/editor/' + post.id"
                    >Edit</RouterLink
                >
            </div>
        </div>
    </div>
</template>

<style scoped>
#posts-cont {
    display: flex;
    flex-direction: column;
    width: 100%;
}
</style>
