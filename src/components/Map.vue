<template>
    <div id="mapid">
        <span class="loader" v-if="loading">Loading Districts...</span>
    </div>
</template>

<style  scoped>
#mapid {
    position: fixed;
    bottom: 50px;
    right: 50px;
    height: 250px;
    width: 600px;
}
.loader {
    position: absolute;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    text-align: center;
    top: 0px;
    width: 100%;
    height: 100%;
    z-index: 401;
    font-size: 32px;
}
</style>

<script>
    export default {
        props: [
            'url_openstreetmap',
            'url_geojson',
        ],
        data() {
            return {
                loading: false,
            }
        },
        methods: {
            renderMap: function() {
                const points = {
                    'DEFAULT_CENTER': [-8.8315139, 125.6199236,9],
                    'DEFAULT_ZOOM': 9,
                }
                this.timormap = L.map('mapid').setView(points.DEFAULT_CENTER, points.DEFAULT_ZOOM);
                L.tileLayer(this.url_openstreetmap, {minZoom: 8, maxZoom: 18}).addTo(this.timormap);
            },
            getGeoJSON: function() {
                console.log(`Getting the GeoJson...`);
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.url_geojson).then(response => {
                    console.log(`Yes, got GeoJson already`);
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
            hideLoader: function () {
                this.loading = false;
            },
        },
        mounted() {
            this.renderMap();
            this.loading = true;
            this.getGeoJSON()
              .then(this.renderGeoJSON)
              .then(this.hideLoader);
        },
    }
</script>
