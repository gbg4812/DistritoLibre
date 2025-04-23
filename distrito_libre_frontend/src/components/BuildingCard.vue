<script setup>
const props = defineProps({
    svgImg: URL,
    name: String,
});
</script>

<template>
    <div id="cont">
        <img :src="props.svgImg" alt="building image" />
        <h3>{{ props.name }}</h3>
    </div>
</template>

<style scoped>
#cont {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 2em;
    border: 1px solid black;
    box-shadow: 5px 5px black;
    aspect-ratio: 1;
}
img {
    width: 10rem;
}

#cont:hover {
    translate: -5px -5px;
    box-shadow: 10px 10px black;
}
</style>
