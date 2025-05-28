<script setup lang="ts">
import { APIBASEURL } from "../constants";
import type { UserInfo } from "../types";
import { ref } from "vue";

const userinfo = ref<UserInfo>({
    username: "",
    email: "",
});

const url = new URL("/api/auth/userinfo/", APIBASEURL);
fetch(url, {
    method: "GET",
    credentials: "include",
})
    .then((response) => response.json())
    .then((data) => {
        userinfo.value = data;
    });
</script>

<template>
    <form>
        <h2>{{ userinfo.username }}</h2>
        <label for="username">Username: </label>
        <input
            v-model="userinfo.username"
            disabled="true"
            type="text"
            name="username"
        />
        <label for="email">Email: </label>
        <input
            v-model="userinfo.email"
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
