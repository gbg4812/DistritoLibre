<script setup lang="ts">
import { logout } from "../distrito_backend";
import { store } from "../store";
const emit = defineEmits(["logout"]);
function onLogout() {
    logout();
    store.user = null;
    emit("logout");
}
</script>

<template>
    <form v-if="store.user" @submit.prevent="onLogout">
        <h2>{{ store.user.username }}</h2>
        <label for="username">Username: </label>
        <input
            v-model="store.user.username"
            disabled="true"
            type="text"
            name="username"
        />
        <label for="email">Email: </label>
        <input
            v-model="store.user.email"
            disabled="true"
            type="text"
            name="email"
        />
        <button type="submit">Logout</button>
    </form>
</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    padding: 10%;
}

h2 {
    text-align: center;
}

button,
label {
    margin-top: 1rem;
}
</style>
