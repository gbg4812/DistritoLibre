<script setup>
import { useRouter } from "vue-router";
import { Icon } from "@iconify/vue/dist/iconify.js";
const router = useRouter();
</script>

<template>
    <div id="pathnav">
        <Icon
            class="clickable"
            icon="tabler:chevron-left"
            width="1.75rem"
            @click="router.back()"
        />
        <Icon
            class="clickable"
            icon="tabler:chevron-right"
            width="1.75rem"
            @click="router.forward()"
        />
        <h3>{{ $route.path }}</h3>
    </div>
</template>

<style scoped>
#pathnav {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
}

h3,
.clickable {
    margin: 0.2rem;
}
</style>
