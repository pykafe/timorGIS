
<template>
    <div class="loader" v-if="loading"></div>
    <div id="mapid" v-show="isShown"></div>
</template>

<style  scoped>
.loader, .loader:before, .loader:after {
    background: #ffffff;
    animation: load1 1s infinite ease-in-out;
    width: 1em;
}

.loader {
    color: #ffffff;
    margin: 88px auto;
    font-size: 11px;
    transform: translateZ(0);
    animation-delay: -0.16s;
}

.loader:before, .loader:after {
    position: absolute;
    top: 0;
    content: '';
}

.loader:before {
    left: -1.5em;
    animation-delay: -0.32s;
}

.loader:after {
    left: 1.5em;
}

@keyframes load1 {
     0%, 80%, 100% {
        box-shadow: 0 0;
        height: 4em;
    }
    40% {
        box-shadow: 0 -2em;
        height: 5em;
    }
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
                isShown: true,
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
                var vm = this;
                vm.loading = true;
                vm.isShown = false;
                console.log(`Getting the GeoJson...`);
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.url_geojson).then(response => {
                    vm.loading = false;
                    vm.isShown = true;
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
        },
        mounted() {
            this.renderMap();
            this.getGeoJSON().then(this.renderGeoJSON);
        },
    }
</script>
