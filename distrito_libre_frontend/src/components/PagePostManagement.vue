<script setup lang="ts">
import PostCard from "./PostCard.vue";
import { store } from "../store.ts";
import type { PostOverview } from "../types.ts";
import { getPostList } from "../distritoBackend.ts";
import { APIBASEURL } from "../constants.ts";
import { ref } from "vue";

const mp = new Map();
mp.set("tag", store.tags);

const data = ref<PostOverview[]>();
getPostList(mp).then((res) => (data.value = res));

function deletePost(postId: number) {
    const url = new URL(
        "/api/posts/detail/" + postId.toString() + "/",
        APIBASEURL,
    );
    fetch(url, { method: "DELETE" }).then(() => {
        getPostList(mp).then((res) => (data.value = res));
    });
}
</script>

<template>
    <div v-if="data" id="posts-cont">
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
