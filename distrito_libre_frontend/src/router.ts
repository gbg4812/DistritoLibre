import { createWebHistory, createRouter } from "vue-router";

import PagePlanesMap from "./components/PagePlanesMap.vue";
import PageSectionMap from "./components/PageSectionMap.vue";
import PageBuildingMap from "./components/PageBuildingMap.vue";
import PagePostList from "./components/PagePostList.vue";
import { store } from "./store";
import PagePostDetail from "./components/PagePostDetail.vue";
import PagePostManagement from "./components/PagePostManagement.vue";
import PagePostEditor from "./components/PagePostEditor.vue";

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
    { path: "/sections/buildings", component: PageBuildingMap },
    { path: "/posts", component: PagePostList },
    { path: "/posts/post/:id", component: PagePostDetail },
    { path: "/posts/manager", component: PagePostManagement },
    { path: "/posts/editor/:id", component: PagePostEditor },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
