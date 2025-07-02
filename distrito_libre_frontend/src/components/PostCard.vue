<script setup lang="ts">
import PushButton from "./reusable/PushButton.vue";
import { Icon } from "@iconify/vue";
import type { PostOverview } from "../backend_types.ts";

const props = defineProps<{
    post: PostOverview;
}>();
</script>

<template>
    <PushButton v-if="props.post" class="post-container" :padding="false">
        <Icon class="coverimg-container" :icon="props.post.icon" width="auto" />
        <div class="article-container">
            <article>
                <h1 class="text-l">{{ props.post.title }}</h1>
                <p>{{ props.post.description }}</p>
            </article>
            <article class="vflex flex-start-start">
                <h3 v-if="props.post.creationd" class="text-s">
                    {{ props.post.creationd }}
                </h3>
                <h2 v-if="props.post.author" class="text-s">
                    {{ props.post.author.username }}
                </h2>
            </article>
        </div>
        <div class="lupa"></div>
        <div class="tags">
            <a v-for="tag of props.post.tags" :key="tag.name">{{ tag.name }}</a>
        </div>
    </PushButton>
</template>
<style scoped>
.post-container {
    display: grid;
    grid-template-areas:
        "coverimg summary"
        "tags tags";
    grid-template-columns: 6rem 7fr;
    grid-template-rows: 6rem min-content;
}

.coverimg-container {
    grid-area: coverimg;
    min-height: 0;
    height: 100%;
    width: 100%;
    border-right: var(--pixel-border);
}

.article-container {
    grid-area: summary;
    display: flex;
    position: relative;
    padding: 0.5rem;

    flex-direction: row;
    justify-content: space-between;

    max-height: 100%;
    min-height: 0;
    overflow: clip;
}

.lupa {
    position: relative;
    background-image: linear-gradient(to bottom, #ffffff00, #ffffffff 85%);
    height: 3rem;
    width: 100%;
    grid-area: summary;
    align-self: end;
}

.tags {
    display: flex;
    align-items: center;
    justify-content: start;
    grid-area: tags;
    border-top: var(--pixel-border);
    min-width: 0;
    width: 100%;
    overflow: clip;
}

.tags a {
    background-color: var(--color-sea-blue);
    border: 5px solid var(--color-sea-blue);
    border-radius: 5px;
    color: var(--color-white);
    margin: 0.5rem;
    padding: 0px;
}

.article-container h2 {
    text-align: right;
}

.article-container h1 {
    text-align: left;
    flex-grow: 0;
}

.article-container p {
    text-align: justify;
    flex-grow: 1;
    min-width: 0;
    word-break: break-word;
}

h1,
h2,
p {
    margin: 0px;
    padding: 0px;
}
</style>
