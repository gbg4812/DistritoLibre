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
        <div class="coverimg-container">
            <Icon :icon="props.post.icon" />
        </div>
        <div class="article-container">
            <h1 class="title">{{ props.post.title }}</h1>
            <h2 class="subtitle">{{ props.post.author.username }}</h2>
            <p>{{ props.post.content }}</p>
            <div class="lupa"></div>
        </div>
    </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.lupa {
    position: absolute;
    background-image: linear-gradient(to bottom, #ffffff00, #ffffffff 85%);
    bottom: 0px;
    left: 0px;
    height: 3rem;
    width: 100%;
}
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

.coverimg-container {
    width: var(--content-width);
}

.article-container {
    width: var(--article-width);
    border-left: var(--black-border);
    display: flex;
    position: relative;
    flex-direction: column;
    justify-content: start;
    overflow: clip;
    padding: 1rem;
    flex-grow: 0;
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
