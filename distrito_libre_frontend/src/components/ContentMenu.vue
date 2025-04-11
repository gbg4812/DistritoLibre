<script setup>
import { ref } from "vue";

const show_menu = ref(false);
</script>

<template>
    <div id="wraper">
        <!-- we need the item before the content to ocupi all the space -->
        <h3 id="title" @mouseenter="show_menu = true">Menu</h3>
        <div v-if="show_menu" id="content" @mouseleave="show_menu = false">
            <a>Categories</a>
            <a>About Us</a>
            <a>Policy</a>
        </div>
    </div>
</template>

<style scoped>
#title {
    text-align: center;
    padding: 1rem;
}

#wraper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    position: relative;
}

#content {
    position: absolute;
    display: flex;
    flex-direction: column;
    width: 20rem;
    top: 100%;
    right: 0px;

    box-sizing: border-box;
    border-top: 1px solid white;
    padding: 1rem;
    padding-left: 2rem;

    background: black;
}

a {
    font-size: 1rem;
    min-width: 10rem;
    padding: 0.5em;
    padding-left: 1em;
    text-align: left;
    transition: 0.3s;
}

a:hover {
    color: var(--hover-color);
    cursor: pointer;
}
</style>
