<template>
    <div class="container-fluid">
        <router-view name="header"></router-view>
        <router-view></router-view>
        <router-view name="map"></router-view>
        <router-view name="footer"></router-view>
    </div>
</template>
<style scoped>
    @font-face {
        font-family: 'Montserrat';
        src: url("./fonts/Montserrat-Regular.woff2");
    }
    div.container-fluid {
        color: var(--black-1);
        font-family: 'Montserrat';
    }
</style>