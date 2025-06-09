<template>
    <div id="wraper">
        <TransitionGroup name="horiztrans" appear>
            <div
                v-for="el in 3"
                id="plane"
                :key="el"
                :style="{
                    '--offset': (el - 2) * 200 + 'px',
                    '--rotZ': (el - 2) * 22 + 'deg',
                }"
                class="horiztrans"
            >
                <div class="seccio"></div>
                <div class="seccio"></div>
                <div class="seccio"></div>
                <div class="seccio"></div>
                <span></span>
                <div class="seccio"></div>
                <div class="seccio"></div>
                <div class="seccio"></div>
                <div class="seccio"></div>
            </div>
        </TransitionGroup>
    </div>
</template>

<script setup lang="ts"></script>

<style scoped>
#wraper {
    --seccio-width: 100px;
    --seccio-height: 100px;
    --gap: 10px;
    width: calc(var(--seccio-width) * 3 + 3 * var(--gap));
    height: calc(var(--seccio-height) * 6 + 3 * var(--gap));
    margin: auto;
    position: relative;
}
#plane {
    --color-orange: #ffa200;
    --color-orange-blur: #ffcd75;
    top: 25%;
    position: absolute;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    text-align: center;
    color: #000000;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--gap);
    width: min-content;
    height: min-content;
    transform-style: preserve-3d;
}

.horiztrans {
    transform: rotateX(60deg) rotateZ(45deg) rotateZ(var(--rotZ))
        translateZ(var(--offset));
}

.horiztrans-enter-active {
    transition: transform 1s;
}

.horiztrans-enter-from {
    transform: initial;
}

.seccio {
    background-color: var(--color-orange);
    width: var(--seccio-width);
    height: var(--seccio-height);
    transition: transform 0.5s background-color 0.5s box-shadow 0.5s;
    box-shadow: 0px 0px 5px 0px var(--color-orange-blur);
}

.seccio:hover {
    transform: translateZ(10px);
    box-shadow: 0px 0px 10px 10px var(--color-orange-blur);
}
</style>
