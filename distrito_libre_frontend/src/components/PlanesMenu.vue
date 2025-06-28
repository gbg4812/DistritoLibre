<template>
    <div id="wraper">
        <TransitionGroup name="horiztrans" appear>
            <label
                v-for="(val, key, idx) in politicalMap"
                :key="key"
                :for="key"
                :style="{
                    '--offset': (idx - 2) * 200 + 'px',
                    '--rotZ': (idx - 2) * 33 + 'deg',
                }"
                class="plane horiztrans"
                :plane="key"
                :tabindex="idx"
                @click="onClickPlane"
            >
                <input
                    :id="key"
                    class="plradio hidden"
                    type="radio"
                    name="plane"
                />
                <div
                    v-for="v in val.slice(4)"
                    :key="v"
                    :seccio="v"
                    class="seccio"
                    @click="onSeccioClick"
                >
                    <label>{{ v.replace("_", " ") }}</label>
                </div>
                <h1 class="plane-title">
                    {{ key.replace("_", " ") }}
                </h1>
                <span> </span>
                <div
                    v-for="v in val.slice(4, undefined)"
                    :key="v"
                    :seccio="v"
                    class="seccio"
                    @click="onSeccioClick"
                >
                    <label>{{ v.replace("_", " ") }}</label>
                </div>
            </label>
        </TransitionGroup>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import { politicalMap } from "../constants";
import { isElement } from "../type_utils.ts";
import { store } from "../store";

const router = useRouter();

function onClickPlane(ev: Event) {
    if (isElement(ev.currentTarget))
        ev.currentTarget.scrollIntoView({ behavior: "auto", block: "center" });
}

function onSeccioClick(ev: Event) {
    if (isElement(ev.currentTarget)) {
        if (ev.currentTarget.parentElement === document.activeElement) {
            const seccio = ev.currentTarget.getAttribute("seccio");
            if (seccio) {
                store.tags.length = 0;
                store.tags.push(seccio);
            }
            router.push("/buildings/");
        }
    }
}
</script>

<style scoped>
#wraper {
    --seccio-width: 100px;
    --seccio-height: 100px;
    --gap: 10px;
    width: calc(var(--seccio-width) * 3 + 3 * var(--gap));
    height: calc(var(--seccio-height) * 12 + 3 * var(--gap));
    margin: auto;
    position: relative;
}
.plane {
    --color-orange: #ffa200;
    --color-orange-blur: #ffcd75;
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
    transition: transform 0.2s ease-in;
}

.plane-title {
    transform-style: preserve-3d;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) translateY(-0.5em) rotateZ(-45deg)
        rotateZ(calc(var(--rotZ) * -1)) rotateX(-90deg) translateY(-1em);
    transition: transform 0.1s ease-in;
}

.plane:focus:has(> :checked) {
    transform: translateY(calc(var(--offset) * -1)) scale(1.5);
    z-index: 1;
}

.plane:focus:has(> :checked) .seccio > label {
    display: initial;
}

.plane:focus:has(> :checked) > h1 {
    transform: translate(-50%, -50%) scale(0.8);
}

.plane:focus ~ .plane {
    z-index: -1;
}

.plane:hover > .plane-title {
    transform: translate(-50%, -50%) translateY(-0.5em) rotateZ(-45deg)
        rotateZ(calc(var(--rotZ) * -1)) rotateX(-90deg) translateY(-1.5em);
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
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.seccio:hover {
    transform: translateZ(10px);
    box-shadow: 0px 0px 10px 10px var(--color-orange-blur);
}

.seccio > label {
    display: none;
    font-size: 0.75rem;
    padding: 0px;
}
</style>
