<script setup>
import { ref } from "vue";
import router from "../router";
import ContentMenu from "./ContentMenu.vue";
import { RouterLink } from "vue-router";
import LoginPopup from "./LoginPopup.vue";
import { store } from "../store";
import CenteredPopup from "./CenteredPopup.vue";

const loginpopup = ref(false);
const username = ref("");
const userpopup = ref(false);

function loginHandler(name) {
    loginpopup.value = false;
    username.value = name;
}
</script>

<template>
    <div class="nav-container white-text">
        <RouterLink to="/">Distrito Libre</RouterLink>

        <h3>{{ router.currentRoute.value.fullPath }}</h3>

        <span></span>

        <h3
            v-if="store.authenticated"
            class="clickable"
            @click="userpopup = true"
        >
            {{ username }}
        </h3>
        <h3 v-else class="clickable" @click="loginpopup = true">Login</h3>
        <CenteredPopup v-if="loginpopup" @close="loginpopup = false">
            <LoginPopup @loged-in="loginHandler"></LoginPopup>
        </CenteredPopup>

        <ContentMenu></ContentMenu>
    </div>
</template>

<style scoped>
.nav-container {
    display: flex;

    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    width: 100%;
    height: 4rem;
    position: fixed;
    top: 0px;
    z-index: 1;
    box-sizing: border-box;

    border: 1px solid white;
}

.nav-container a {
    font-size: 2em;
    color: white;
    font-weight: 800;
    margin-left: 1rem;
    margin-right: 1rem;
}

h3 {
    padding: 1rem;
}

span {
    flex-grow: 1;
}
</style>
