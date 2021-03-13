
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

        <div v-for="viazen in istoriaviazen" v-bind:key="viazen.pk" class="viazen_card">
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">{{ viazen.fields.title}}</h5>
                    <p class="card-text">{{ viazen.fields.description }}</p>
                    <p class="card-text"><small class="text-muted">Created at: {{ viazen.fields.created_at }}</small></p>
                </div>
            </div>
        </div>
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

    export default {
        props: [
            'urls',
        ],
        components: {
            Map,
        },
        data() {
            return {
                images: [],
                istoriaviazen: [],
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
            getIstoriaviazen: function() {
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.urls.istoriaviazen).then(response => {
                    return response.json()
                });
            },
            renderImages: function(images) {
                console.log(images);
                this.images = images;
            },
            renderIstoriaviazen: function(istoriaviazen) {
                console.log(istoriaviazen);
                this.istoriaviazen = istoriaviazen;
            }
        },
        mounted() {
            this.getImages().then(this.renderImages);
            this.getIstoriaviazen().then(this.renderIstoriaviazen);
        },
    }
</script>