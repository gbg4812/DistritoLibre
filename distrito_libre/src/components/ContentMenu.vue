<script setup>
import { ref } from "vue";

const show_menu = ref(false);
</script>

<template>
    <div id="wraper">
        <!-- we need the item before the content to ocupi all the space -->
        <div id="title-wraper">
            <h3 id="title" @mouseenter="show_menu = true">Menu</h3>
        </div>
        <div v-if="show_menu" id="content" @mouseleave="show_menu = false">
            <a>Categories</a>
            <a>About Us</a>
            <a>Policy</a>
        </div>
    </div>
</template>

<style scoped>
#wraper {
    height: 100%;
    margin: 0px;
}

#title-wraper {
    height: 100%;
    display: flex;
    flex-direction: column;
    margin-right: 1rem;
}

#title {
    margin: auto;
    position: static;
    text-align: center;
}

#content {
    position: absolute;
    display: flex;
    flex-direction: column;
    width: 100vw;
    right: 0px;

    box-sizing: border-box;
    border-top: 1px solid gray;
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
