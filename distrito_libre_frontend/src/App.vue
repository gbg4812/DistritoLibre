<script setup lang="ts">
import { useRouter } from "vue-router";
import NavBar from "./components/NavBar.vue";
import FloatButton from "./components/reusable/FloatButton.vue";
import { Icon } from "@iconify/vue";
import { getUserData } from "./distrito_backend";
import { store } from "./store";
import { watch } from "vue";
const router = useRouter();
function onPlusClick() {
    router.push("/posts/editor/new/");
}

getUserData().then((user) => {
    store.user = user;
});

watch(store, (val) => {
    console.log(val);
});
</script>

<template>
    <div id="content">
        <NavBar id="navbar" />
        <RouterView id="main" />
        <FloatButton
            class="white-text text-m"
            bottom="2rem"
            right="2rem"
            @click="onPlusClick"
        >
            <Icon icon="tabler:plus"></Icon>
        </FloatButton>
    </div>
</template>

<style scoped>
#content {
    display: grid;
    grid-template-areas: "navbar" "main";
    grid-template-columns: 4fr;
    grid-template-rows: 4rem 1fr;
    height: 100%;
    width: 100%;
}

#navbar {
    grid-area: navbar;
}
#main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
    grid-area: main;
    overflow: scroll;
}
</style>
