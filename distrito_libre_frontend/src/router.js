import { createWebHistory, createRouter } from "vue-router";

import PlanesMap from "./components/PlanesMap.vue";
import SectionMap from "./components/SectionMap.vue";
import BuildingsMaps from "./components/BuildingsMaps.vue";
import ContentView from "./components/ContentView.vue";
import { store } from "./store";
import PostDetail from "./components/PostDetail.vue";

const routes = [
    {
        path: "/",
        component: PlanesMap,
        beforeEnter: () => {
            store.tags = [];
        },
    },
    {
        path: "/sections",
        component: SectionMap,
        beforeEnter: () => {
            store.tags = [];
        },
    },
    { path: "/sections/buildings", component: BuildingsMaps },
    { path: "/posts", component: ContentView },
    { path: "/posts/post/:name", component: PostDetail },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
