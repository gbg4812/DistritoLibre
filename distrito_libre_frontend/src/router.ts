import { createWebHistory, createRouter } from "vue-router";

import PagePlanesMap from "./components/pages/PagePlanesMap.vue";
import PageBuildingMap from "./components/pages/PageBuildingMap.vue";
import PagePostList from "./components/pages/PagePostList.vue";
import { store } from "./store";
import PagePostDetail from "./components/pages/PagePostDetail.vue";
import PagePostManagement from "./components/pages/PagePostManagement.vue";
import PagePostEditor from "./components/pages/PagePostEditor.vue";

const routes = [
    {
        path: "/",
        component: PagePlanesMap,
        beforeEnter: () => {
            store.tags = [];
        },
    },
    { path: "/buildings", component: PageBuildingMap },
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
