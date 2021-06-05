<template>
    <div class="container-fluid">
        <router-link :to="{name: 'photos'}">PHOTOS</router-link>
        <router-link to="/map">MAP</router-link>


        <router-view></router-view>
    </div>
</template>