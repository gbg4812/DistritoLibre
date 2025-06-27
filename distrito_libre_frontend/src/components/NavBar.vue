<script setup lang="ts">
import { ref } from "vue";
import ContentMenu from "./ContentMenu.vue";
import { RouterLink } from "vue-router";
import UserLoginPopup from "./UserLoginPopup.vue";
import UserPopup from "./UserPopup.vue";
import { store } from "../store.ts";
import CenteredPopup from "./reusable/CenteredPopup.vue";
import NavPath from "./NavPath.vue";

const loginpopup = ref(false);
const userpopup = ref(false);

const isSmall = window.innerWidth < 500;
console.log(window.innerWidth);

function loginHandler() {
    loginpopup.value = false;
}
</script>

<template>
    <div class="nav-container white-text">
        <RouterLink class="text-l" to="/">Distrito Libre</RouterLink>

        <NavPath v-if="!isSmall" />

        <span></span>

        <div v-if="!isSmall">
            <h2 v-if="store.user" class="clickable" @click="userpopup = true">
                {{ store.user.username }}
            </h2>

            <h2 v-else class="clickable" @click="loginpopup = true">Login</h2>
        </div>

        <CenteredPopup v-if="loginpopup" @close="loginpopup = false">
            <UserLoginPopup @loged-in="loginHandler"></UserLoginPopup>
        </CenteredPopup>
        <CenteredPopup v-if="userpopup" @close="userpopup = false">
            <UserPopup></UserPopup>
        </CenteredPopup>

        <ContentMenu />
    </div>
</template>

<style scoped>
.nav-container {
    display: flex;

    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    position: fixed;

    width: 100%;
    height: 4rem;
    top: 0px;
    z-index: 2;
    box-sizing: border-box;

    border: 1px solid white;
}

.nav-container a {
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
