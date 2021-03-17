
<template>
    <div class="container-fluid">
        <div class="images_container">
            <div v-for="image in images" v-bind:key="image.pk" class="image_card">
                <img v-bind:src="`${urls.media_url}${ image.fields.image}`" width="200"/>
            </div>
        </div>

        <Map
            v-bind:url_openstreetmap="urls.openstreetmap"
            v-bind:url_geojson="urls.geojson" />

        <Istoria 
            v-bind:url_istoriaviazen="urls.istoriaviazen" />
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
    import Map from "./Map.vue";
    import Istoria from "./Istoria.vue";

    export default {
        props: [
            'urls',
        ],
        components: {
            Map,
            Istoria,
        },
        data() {
            return {
                images: [],
            }
        },
        methods: {
            getImages: function() {
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.urls.images).then(response => {
                    return response.json()
                });
            },
            renderImages: function(images) {
                console.log(images);
                this.images = images;
            },
        },
        mounted() {
            this.getImages().then(this.renderImages);
        },
    }
</script>