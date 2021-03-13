
<template>
    <div id="mapid"></div>
</template>

<style  scoped>
</style>

<script>
    export default {
        props: [
            'url_openstreetmap',
            'url_geojson',
        ],
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
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.url_geojson).then(response => {
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
        },
        mounted() {
            this.renderMap();
            this.getGeoJSON().then(this.renderGeoJSON);
        },
    }
</script>