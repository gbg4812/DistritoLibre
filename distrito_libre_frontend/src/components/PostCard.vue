<script setup lang="ts">
import PushButton from "./reusable/PushButton.vue";
import { Icon } from "@iconify/vue";
import type { PostOverview } from "../types.ts";

const props = defineProps<{
    post: PostOverview;
}>();
</script>

<template>
    <PushButton v-if="props.post" class="post-container" :padding="false">
        <Icon class="coverimg-container" :icon="props.post.icon" width="auto" />
        <div class="article-container">
            <h1 class="text-l">{{ props.post.title }}</h1>
            <h2 v-if="props.post.author" class="text-m">
                {{ props.post.author.username }}
            </h2>
            <p v-if="props.post.author" class="text-s">
                {{ props.post.creationd }}
            </p>
            <p>{{ props.post.description }}</p>
        </div>
        <div class="lupa"></div>
        <div class="tags">
            <a v-for="tag of props.post.tags" :key="tag.name">{{ tag }}</a>
        </div>
    </PushButton>
</template>
<style scoped>
.post-container {
    display: grid;
    grid-template-areas:
        "coverimg summary"
        "tags tags";
    grid-template-columns: 1fr 5fr;
    grid-template-rows: 1fr min-content;
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
    padding: 1rem;

    flex-direction: column;
    justify-content: start;

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
}

.article-container h2 {
    text-align: right;
    color: var(--color-cream);
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
</style>
