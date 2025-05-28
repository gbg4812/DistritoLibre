<script setup lang="ts">
import { Icon } from "@iconify/vue/dist/iconify.js";
import NavBar from "./components/NavBar.vue";
import FloatButton from "./components/reusable/FloatButton.vue";
import PostManagement from "./components/PostManagement.vue";
import CenteredPopup from "./components/reusable/CenteredPopup.vue";
import { ref } from "vue";

const postmanpopup = ref(false);
</script>

<template>
    <NavBar />
    <div class="content">
        <RouterView />
    </div>
    <FloatButton
        class="white-text text-m"
        bottom="2rem"
        right="2rem"
        @click="postmanpopup = true"
    >
        <Icon icon="tabler:plus"></Icon>
    </FloatButton>

    <CenteredPopup v-if="postmanpopup" @close="postmanpopup = false">
        <PostManagement></PostManagement
    ></CenteredPopup>
</template>

<style scoped>
.content {
    display: flex;
    flex-direction: column;
    margin-top: 4rem;
}
</style>
