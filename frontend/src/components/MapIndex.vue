<script setup>
function importAll(r) {
    r.keys().forEach(r);
}
importAll(require.context('../assets/index-map/', false, /.jpg$/));
</script>

<template>
    <div class="image-container">
    <img src="../assets/index-map/index-map.svg">
    </div>
</template>

<style scoped>
 .image-container {
     width: 100%;
 }
</style>
