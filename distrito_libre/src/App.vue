<template>
    <NavBar />
    <div class="content">
        <MapIndex />
        <ContentView />
    </div>
</template>

<script>
import ContentView from "./components/ContentView.vue";
import MapIndex from "./components/MapIndex.vue";
import NavBar from "./components/NavBar.vue";
import { store } from "./store.js";

export default {
    name: "App",
    data() {
        return {
            store,
        };
    },
    components: {
        ContentView,
        MapIndex,
        NavBar,
    },
};
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

.content {
    display: grid;
    grid-template-columns: 1fr 1fr;
}
</style>
