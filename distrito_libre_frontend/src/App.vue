<script setup>
import NavBar from "./components/NavBar.vue";
</script>

<template>
    <NavBar />
    <div class="content">
        <RouterView />
    </div>
</template>

<style scoped>
.content {
    display: flex;
    flex-direction: column;
    margin-top: 4rem;
}
</style>
