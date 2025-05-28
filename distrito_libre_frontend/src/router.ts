import { createWebHistory, createRouter } from "vue-router";

import PagePlanesMap from "./components/PagePlanesMap.vue";
import PageSectionMap from "./components/PageSectionMap.vue";
import PageBuildingsMaps from "./components/PageBuildingsMaps.vue";
import PagePostList from "./components/PagePostList.vue";
import { store } from "./store";
import PagePostDetail from "./components/PagePostDetail.vue";
import PagePostManagement from "./components/PagePostManagement.vue";

const routes = [
    {
        path: "/",
        component: PagePlanesMap,
        beforeEnter: () => {
            store.tags = [];
        },
    },
    {
        path: "/sections",
        component: PageSectionMap,
        beforeEnter: () => {
            store.tags = [];
        },
    },
    { path: "/sections/buildings", component: PageBuildingsMaps },
    { path: "/posts", component: PagePostList },
    { path: "/posts/post/:name", component: PagePostDetail },
    { path: "/posts/manager", component: PagePostManagement },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
