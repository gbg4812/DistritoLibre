<script setup lang="ts">
import PostCard from "../PostCard.vue";
import PushButton from "../reusable/PushButton.vue";
import { store } from "../../store.ts";
import type { PostOverview } from "../../backend_types.ts";
import { getPostList } from "../../distrito_backend.ts";
import { APIBASEURL } from "../../constants.ts";
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
    <div>
        <div v-if="data" id="posts-cont">
            <div
                v-for="post in data"
                id="postitem"
                :key="post.id"
                class="vflex item-cont"
            >
                <RouterLink :to="'/posts/post/' + post.id" style="flex-grow: 1">
                    <PostCard class="postcard" :post="post"></PostCard>
                </RouterLink>
                <div id="controls">
                    <PushButton @click="deletePost(post.id)">Delete</PushButton>
                    <PushButton
                        @click="$router.push('/posts/editor/' + post.id)"
                        >Edit</PushButton
                    >
                </div>
            </div>
            <PushButton @click="$router.push('/posts/editor/new')">
                New Post
            </PushButton>
        </div>
    </div>
</template>

<style scoped>
#posts-cont {
    display: flex;
    flex-direction: column;
    width: 66%;
    height: 100%;
}

#main {
    width: 100%;
    height: 100%;
}
#controls {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: end;
}

#controls > * {
    margin: 0.2rem;
}
a {
    padding: 0px;
}

.postcard {
    margin: 0.2rem;
}

.item-cont {
    margin: 0.3rem;
}
</style>
