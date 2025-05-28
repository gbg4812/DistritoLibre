<script setup lang="ts">
import { useRouter } from "vue-router";
import NavBar from "./components/NavBar.vue";
import FloatButton from "./components/reusable/FloatButton.vue";
import { Icon } from "@iconify/vue";
const router = useRouter();
function onPlusClick() {
    router.push("/posts/manager");
}
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
        @click="onPlusClick"
    >
        <Icon icon="tabler:plus"></Icon>
    </FloatButton>
</template>

<style scoped>
.content {
    display: flex;
    flex-direction: column;
    margin-top: 4rem;
}
</style>
