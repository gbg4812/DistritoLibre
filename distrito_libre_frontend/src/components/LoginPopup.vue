<script setup lang="ts">
import { store } from "../store";
import { APIBASEURL } from "../constants";
const emit = defineEmits(["loged-in"]);
function login() {
    const form = document.querySelector<HTMLFormElement>("#login-form");
    const data = new FormData(form);
    fetch(APIBASEURL.href + "login/", { method: "post", body: data })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            emit("loged-in", data.username);
            store.authenticated = true;
        });
}
</script>

<template>
    <div>
        <form id="login-form">
            <label for="username">Username: </label>
            <input type="text" name="username" />

            <label for="password">Password: </label>
            <input type="password" name="password" />

            <button id="login-bttn" type="button" @click="login">Login</button>
        </form>
    </div>
</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    padding: 10%;
}
</style>
