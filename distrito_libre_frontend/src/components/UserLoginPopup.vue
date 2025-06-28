<script setup lang="ts">
import { store } from "../store.ts";
import { login } from "../distrito_backend.ts";
const emit = defineEmits(["loged-in"]);
function onLogin() {
    const form = document.querySelector<HTMLFormElement>("#login-form")!;
    login(form["username"].value, form["password"].value).then((data) => {
        emit("loged-in");
        store.user = data;
    });
}
</script>

<template>
    <div>
        <form id="login-form">
            <label for="username" class="black-text">Username: </label>
            <input type="text" name="username" />

            <label for="password" class="black-text">Password: </label>
            <input type="password" name="password" />

            <button
                id="login-bttn"
                class="white-text"
                type="button"
                @click="onLogin"
            >
                Login
            </button>
        </form>
    </div>
</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    padding: 10%;
}

button,
label {
    margin-top: 1rem;
}
</style>
