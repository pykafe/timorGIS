
<template>
    <div class="container-fluid">

        <PhotoTimor
            v-bind:url_media="urls.media_url"
            v-bind:url_images="urls.images" />

        <Map
            v-bind:url_openstreetmap="urls.openstreetmap"
            v-bind:url_geojson="urls.geojson" />
    </div>
</template>

<style  scoped>
    div {
        color:REd;
    }
    .image_card {
        margin: 5px;
    }
</style>

<script>
    import PhotoTimor from "./components/PhotoTimor.vue";
    import Map from "./components/Map.vue";
    import Istoria from "./components/Istoria.vue";

    export default {
        props: [
            'urls',
        ],
        components: {
            PhotoTimor,
            Map,
            Istoria,
        },
    }
</script>