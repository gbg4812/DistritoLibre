<script setup>
import { Icon } from "@iconify/vue";
import { defineProps } from "vue";

const props = defineProps({
    post: {
        required: true,
        type: Object,
    },
});
</script>

<template>
    <div v-if="props.post" class="post-container">
        <div class="content-container">
            <h2>{{ props.post.title }}</h2>
            <div class="image-holder">
                <Icon :icon="props.post.coverimg" />
            </div>
            <h2>{{ props.post.author.username }}</h2>
        </div>
        <div class="article-container">
            <h1>{{ props.post.title_art }}</h1>
            <h2>{{ props.post.author_art }}</h2>
            <p>{{ props.post.content }}</p>
        </div>
    </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.post-container {
    --content-width: 15rem;
    --article-width: 30rem;
    --black-border: 1px solid black;
    background: white;
    height: calc(calc(var(--content-width) + var(--article-width)) / 3);
    width: calc(var(--content-width) + var(--article-width));
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 2rem;
    display: flex;
    border: var(--black-border);
    box-shadow: 5px 5px black;
}
.post-container * {
    box-sizing: border-box;
}

.content-container {
    width: var(--content-width);
    display: grid;
    grid-template-rows: 1fr 3fr 1fr;
}

.content-container h2 {
    width: 100%;
    margin: auto;
}

.image-holder {
    grid-row: 2;
    display: flex;
    font-size: 10rem;
    margin: auto;
    /*border-top: 1px solid black;
    border-bottom: 1px solid black;*/
}

.article-container {
    width: var(--article-width);
    border-left: var(--black-border);
    overflow: clip;
}

.article-container h1,
h2 {
    margin: 1rem;
    margin-left: 1rem;
    margin-right: 1rem;
}

.article-container h2 {
    text-align: right;
    color: gray;
}

.article-container h1 {
    text-align: left;
}

.article-container p {
    text-align: justify;
    margin: 1rem;
}
</style>
