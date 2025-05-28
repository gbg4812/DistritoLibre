<script setup lang="ts">
import DropDownMenu from "./reusable/DropDownMenu.vue";
</script>

<template>
    <DropDownMenu title="Menu">
        <RouterLink class="clickable" to="/">Home</RouterLink>
        <RouterLink class="clickable" to="/posts">Posts</RouterLink>
    </DropDownMenu>
</template>

<style scoped>
a {
    padding: 0.5rem;
}
</style>
