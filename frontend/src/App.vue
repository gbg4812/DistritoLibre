<template>
    <NavBar />
    <MapIndex />
    <ContentView />
</template>

<script>
import MapIndex from "./components/MapIndex.vue";
import ContentView from "./components/ContentView.vue";
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
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
  font-size: 12pt;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: grid;
  grid-template-columns: 1fr 1fr;
}

</style>
