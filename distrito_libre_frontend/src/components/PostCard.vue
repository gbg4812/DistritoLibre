<script setup>
import { Icon } from "@iconify/vue";

const props = defineProps({
    post: {
        required: true,
        type: Object,
    },
});
</script>

<template>
    <div v-if="props.post" class="post-container">
        <Icon class="coverimg-container" :icon="props.post.icon" width="none" />
        <div class="article-container">
            <h1 class="title">{{ props.post.title }}</h1>
            <h2 class="subtitle">{{ props.post.author.username }}</h2>
            <p>{{ props.post.description }}</p>
        </div>
        <div class="lupa"></div>
        <div class="tags">
            <a v-for="tag of props.post.tags" :key="tag">{{ tag }}</a>
        </div>
    </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.post-container {
    --img-width: 15rem;
    --article-width: 30rem;
    --black-border: 1px solid black;
    background: white;
    margin: 1rem;
    display: grid;
    grid-template-areas:
        "coverimg summary"
        "tags tags";
    grid-template-columns: 15rem 45rem;
    grid-template-rows: 15rem 1fr;
    border: var(--black-border);
    box-shadow: 5px 5px black;
}

.post-container:hover {
    translate: -5px -5px;
    box-shadow: 10px 10px black;
}

.coverimg-container {
    grid-area: coverimg;
    min-height: 0;
    height: 100%;
    border-right: var(--black-border);
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
    border-top: var(--black-border);
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
    color: gray;
}

.article-container h1 {
    text-align: left;
    flex-grow: 0;
}

.article-container p {
    text-align: justify;
    flex-grow: 1;
}
</style>
