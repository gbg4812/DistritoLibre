<script setup>
import BuildingCard from "./BuildingCard.vue";
import { APIBASEURL } from "../constants";
import { store } from "../store";
import { ref } from "vue";
const buildingsWithIcons = ref([]);

const reqUrl = new URL("posts/buildings/", APIBASEURL);
reqUrl.searchParams.append("tag", store.tags[0]);
fetch(reqUrl)
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        buildingsWithIcons.value = data.buildings;
    });
</script>

<template>
    <div id="build-cont">
        <RouterLink v-for="b in buildingsWithIcons" :key="b.name" to="/posts">
            <BuildingCard :name="b.name" :svg-img="b.iconUrl"></BuildingCard>
        </RouterLink>
    </div>
</template>

<style scoped>
#build-cont {
    display: grid;
    gap: 2rem;
    margin: 2rem;
    grid-template-columns: repeat(4, 1fr);
}

a {
    color: black;
}
</style>
