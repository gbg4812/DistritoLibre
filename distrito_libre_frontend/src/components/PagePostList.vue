<script setup lang="ts">
import PostCard from "./PostCard.vue";
import { store } from "../store.ts";
import type { PostOverview } from "../backend_types.ts";
import { getPostList } from "../distrito_backend.ts";
import TagsBar from "./TagsBar.vue";
import { ref } from "vue";

const mp = new Map();
mp.set("tag", store.tags);

const data = ref<PostOverview[]>();
getPostList(mp).then((res) => (data.value = res));
</script>

<template>
    <div id="cont">
        <TagsBar></TagsBar>
        <div v-if="data" id="posts-cont">
            <RouterLink
                v-for="post in data"
                :key="post.id"
                :to="'/posts/post/' + post.id"
            >
                <PostCard :post="post"></PostCard>
            </RouterLink>
        </div>
    </div>
</template>

<style scoped>
#posts-cont {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
}

#cont {
    background-color: white;
    width: 100%;
    height: 100%;
}
</style>
