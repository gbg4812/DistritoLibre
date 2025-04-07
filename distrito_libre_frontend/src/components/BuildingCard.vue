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
    align-items: stretch;
    justify-content: space-around;
    padding: 2em;
    border: 1px solid black;
    border-radius: 5px;
    margin: 2em;
}
</style>
