<script setup lang="ts">
import { APIBASEURL } from "../../constants.ts";
import { store } from "../../store.ts";
import { ref } from "vue";
import type { BTag } from "../../backend_types.ts";

import TagsBar from "../TagsBar.vue";
import BuildingCard from "../BuildingCard.vue";
import { isElement } from "../../type_utils.ts";
import { useRouter } from "vue-router";

const router = useRouter();

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

function onSelect(event: MouseEvent) {
    if (isElement(event.currentTarget)) {
        console.log(event.currentTarget);
        const name = event.currentTarget.getAttribute("name");
        if (name) store.tags.push(name);
        console.log(store.tags);
        router.push("/posts");
    }
}
</script>

<template>
    <div>
        <TagsBar></TagsBar>
        <div id="build-grid">
            <div
                v-for="b in buildingsWithIcons"
                :key="b.name"
                class="text-black"
            >
                <BuildingCard
                    :name="b.name"
                    :icon="b.icon"
                    @click="onSelect"
                ></BuildingCard>
            </div>
        </div>
    </div>
</template>

<style scoped>
#main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
}
#build-grid {
    display: grid;
    gap: 2rem;
    margin: 2rem;
    grid-template-columns: repeat(4, 1fr);
}
</style>
