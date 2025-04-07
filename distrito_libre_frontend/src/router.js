import { createWebHistory, createRouter } from "vue-router";

import PlanesMap from "./components/PlanesMap.vue";
import SectionMap from "./components/SectionMap.vue";
import BuildingsMaps from "./components/BuildingsMaps.vue";
import ContentView from "./components/ContentView.vue";

const routes = [
    { path: "/", component: PlanesMap },
    { path: "/sections", component: SectionMap },
    { path: "/buildings", component: BuildingsMaps },
    { path: "/buildings/:name", component: ContentView },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
