<script setup lang="ts">
import { APIBASEURL } from "../constants";
import { store } from "../store.ts";
import { ref } from "vue";
import type { BTag } from "../types.ts";

import BuildingCard from "./BuildingCard.vue";

const buildingsWithIcons = ref<BTag[]>([]);

const reqUrl = new URL("/api/posts/btags/", APIBASEURL);
reqUrl.searchParams.append("tag", store.tags[0]);
fetch(reqUrl)
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        buildingsWithIcons.value = data.btags;
    });
</script>

<template>
    <div id="build-cont">
        <RouterLink
            v-for="b in buildingsWithIcons"
            :key="b.name"
            class="text-black"
            to="/posts"
        >
            <BuildingCard :name="b.name" :icon="b.icon"></BuildingCard>
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
</style>
