
<template>
    <div class="images_container">

        <div v-for="image in images" v-bind:key="image.pk" class="image_card">
            {{ image.pk }}
            <!--<img src="/media/photos/3AA92B55-4CE5-4D1B-A967-0A1D98FA45AB_FlsuDPE.jpeg" width="200"> -->
        </div>
    </div>
    <Map
     v-bind:url_openstreetmap="urls.openstreetmap"
     v-bind:url_geojson="urls.geojson" />
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

    export default {
        props: [
            'urls'
        ],
        components: {
            Map,
        },
        data() {
            return {
                images: []
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
            }
        },
        mounted() {
            this.getImages().then(this.renderImages);
        },
    }
</script>