<script setup>
import BuildingCard from "./BuildingCard.vue";
const buildingsWithIcons = [
    { name: "School", iconUrl: "https://api.iconify.design/mdi:school.svg" },
    {
        name: "Library",
        iconUrl: "https://api.iconify.design/mdi:bookshelf.svg",
    },
    {
        name: "Hospital",
        iconUrl: "https://api.iconify.design/mdi:hospital.svg",
    },
    {
        name: "PoliceStation",
        iconUrl: "https://api.iconify.design/mdi:police-badge.svg",
    },
    {
        name: "FireStation",
        iconUrl: "https://api.iconify.design/mdi:fire-station.svg",
    },
    {
        name: "ApartmentBuilding",
        iconUrl: "https://api.iconify.design/mdi:home-city.svg",
    },
    { name: "House", iconUrl: "https://api.iconify.design/mdi:home.svg" },
    {
        name: "OfficeBuilding",
        iconUrl: "https://api.iconify.design/mdi:office-building.svg",
    },
    {
        name: "ShoppingMall",
        iconUrl: "https://api.iconify.design/mdi:shopping.svg",
    },
    { name: "Supermarket", iconUrl: "https://api.iconify.design/mdi:cart.svg" },
    {
        name: "MovieTheater",
        iconUrl: "https://api.iconify.design/mdi:movie-open.svg",
    },
    { name: "Restaurant", iconUrl: "https://api.iconify.design/mdi:food.svg" },
    { name: "Gym", iconUrl: "https://api.iconify.design/mdi:dumbbell.svg" },
    { name: "Museum", iconUrl: "https://api.iconify.design/mdi:bank.svg" },
    {
        name: "ArtGallery",
        iconUrl: "https://api.iconify.design/mdi:palette.svg",
    },
    { name: "Church", iconUrl: "https://api.iconify.design/mdi:church.svg" },
    { name: "Mosque", iconUrl: "https://api.iconify.design/mdi:mosque.svg" },
    { name: "Temple", iconUrl: "https://api.iconify.design/mdi:temple.svg" },
    {
        name: "Train Station",
        iconUrl: "https://api.iconify.design/mdi:train.svg",
    },
    { name: "Airport", iconUrl: "https://api.iconify.design/mdi:airplane.svg" },
];
</script>

<template>
    <div id="build-cont">
        <RouterLink v-for="b in buildingsWithIcons" :key="b.name" to="/posts">
            <BuildingCard :name="b.name" :svg-img="b.iconUrl"></BuildingCard>
        </RouterLink>
    </div>
</template>

<style scoped>
#build-cont {
    display: grid;
    gap: 2rem;
    margin: 2rem;
    grid-template-columns: repeat(4, 1fr);
}

a {
    color: black;
    text-decoration: none;
}
</style>
