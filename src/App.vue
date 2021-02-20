
<template>
    <div class="images_container">

        <div v-for="item in items" class="image_card">
            <img src="/media/photos/3AA92B55-4CE5-4D1B-A967-0A1D98FA45AB_FlsuDPE.jpeg" width="200">
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
            'url_openstreetmap',
            'districts',
            'api_url'
        ],
        data() {
            return {
                items: [
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                ]
            }
        },
        methods: {
            renderMap: function() {
                const points = {
                    'DEFAULT_CENTER': [-8.8315139, 125.6199236,9],
                    'DEFAULT_ZOOM': 9,
                }
                var timormap = L.map('mapid').setView(points.DEFAULT_CENTER, points.DEFAULT_ZOOM);
                L.tileLayer(this.url_openstreetmap, {minZoom: 8, maxZoom: 18}).addTo(timormap);
                L.geoJSON(this.districts, {
                    style: function (feature) {
                        return {color: 'orange'};
                    }
                }).bindPopup(function (layer) {
                    var name = layer.feature.properties.name;
                        return 'Distritu: ' + name[0] + name.substr(1).toLowerCase();
                }).addTo(timormap);
            },
            getApiData: function() {
                fetch(this.api_url).then(response => console.log(response))
            }
        },
        mounted() {
            this.renderMap();
            this.getApiData();
        },
    }
</script>