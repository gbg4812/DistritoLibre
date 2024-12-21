<!-- eslint-disable no-unused-vars -->
<script setup>
import { onMounted, ref } from "vue";
onMounted(() => {
    let promise = fetch("http://localhost:8080/assets/index-map/sectionid.svg");
    promise
        .then((resp) => resp.text())
        .then((svgcode) => {
            const svg = document.createElement("svg");
            svg.innerHTML = svgcode;
            const imgs = Array.from(svg.querySelectorAll("image"));
            imgs.forEach((img) => {
                let src = img.getAttributeNS(
                    "http://www.w3.org/1999/xlink",
                    "href"
                );
                src = "assets/index-map/".concat(src);
                img.setAttributeNS("http://www.w3.org/1999/xlink", "href", src);
                img.addEventListener("click", (ev) => {
                    console.log(ev.currentTarget.id);
                });
                console.log(img);
            });

            console.log(svg);
            document.querySelector("#index-map-cont").replaceChildren(svg);
        });
});
</script>

<template>
    <div class="image-container" id="index-map-cont"></div>
</template>

<style scoped>
.image-container {
    width: 100%;
}
</style>
