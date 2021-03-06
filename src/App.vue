
<template>
    <div class="images_container">

        <div v-for="image in images" v-bind:key="image.pk" class="image_card">
            {{ image.pk }}
            <!--<img src="/media/photos/3AA92B55-4CE5-4D1B-A967-0A1D98FA45AB_FlsuDPE.jpeg" width="200"> -->
        </div>
    </div>
    <div id="mapInset">
        <div id="mapid"></div>
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
    export default {
        props: [
            'urls'
        ],
        data() {
            return {
                images: []
            }
        },
        methods: {
            renderMap: function() {
                const points = {
                    'DEFAULT_CENTER': [-8.8315139, 125.6199236,9],
                    'DEFAULT_ZOOM': 9,
                }
                this.timormap = L.map('mapid').setView(points.DEFAULT_CENTER, points.DEFAULT_ZOOM);
                L.tileLayer(this.urls.openstreetmap, {minZoom: 8, maxZoom: 18}).addTo(this.timormap);
            },
            getGeoJSON: function() {
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.urls.geojson).then(response => {
                    return response.json()
                });
            },
            getImages: function() {
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.urls.images).then(response => {
                    return response.json()
                });
            },
            renderGeoJSON: function(geojson) {
                L.geoJSON(geojson, {
                    style: function (feature) {
                        return {color: 'orange'};
                    }
                }).bindPopup(function (layer) {
                    var name = layer.feature.properties.name;
                        return 'Distritu: ' + name[0] + name.substr(1).toLowerCase();
                }).addTo(this.timormap);
            },
            renderImages: function(images) {
                console.log(images);
                this.images = images;
            }
        },
        mounted() {
            this.renderMap();
            this.getGeoJSON().then(this.renderGeoJSON);
            this.getImages().then(this.renderImages);
        },
    }
</script>