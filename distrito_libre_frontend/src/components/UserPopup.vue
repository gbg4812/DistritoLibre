<script setup lang="ts">
import { store } from "../store";
</script>

<template>
    <form v-if="store.user">
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
