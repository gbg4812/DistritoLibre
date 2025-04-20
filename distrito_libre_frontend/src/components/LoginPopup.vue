<script setup lang="ts">
const emit = defineEmits(["loged-in"]);
function login() {
    const form = document.querySelector<HTMLFormElement>("#login-form");
    const data = new FormData(form);
    fetch("http://127.0.0.1:8000/login/", { method: "post", body: data }).then(
        () => {
            emit("loged-in");
        },
    );
}
</script>

<template>
    <div id="popup">
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
#popup {
    position: absolute;
    width: 75%;
    height: 75%;
    background-color: white;
    border: 1px solid balck;
}

form {
    display: flex;
    flex-direction: column;
}
</style>
