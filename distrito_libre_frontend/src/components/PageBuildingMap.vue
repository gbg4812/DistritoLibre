<script setup lang="ts">
import { APIBASEURL } from "../constants.ts";
import { store } from "../store.ts";
import { ref } from "vue";
import type { BTag } from "../backend_types.ts";

import TagsBar from "./TagsBar.vue";
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
        <TagsBar></TagsBar>
        <div id="build-grid">
            <RouterLink
                v-for="b in buildingsWithIcons"
                :key="b.name"
                class="text-black"
                to="/posts"
            >
                <BuildingCard :name="b.name" :icon="b.icon"></BuildingCard>
            </RouterLink>
        </div>
    </div>
</template>

<style scoped>
#build-cont {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
#build-grid {
    display: grid;
    gap: 2rem;
    margin: 2rem;
    grid-template-columns: repeat(4, 1fr);
}
</style>
