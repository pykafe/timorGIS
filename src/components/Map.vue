<template>
    <div id="expand">
            <span>Click the map icon for expand</span>
    </div>
    <div id="map_container">
        <div id="mapid">
            <span class="loader" v-if="map.requesting">Loading Districts...</span>
        </div>
    </div>
</template>

<style  scoped>
#expand {
    position: fixed;
    top: 140px;
    right: 170px;
}
#map_container {
    position: fixed;
    top: 90px;
    right: 12px;
}
#map_container button {
    position: absolute;
    right: 20px;
    top: 20px;
    z-index: 500;
}
#mapid {
    border-radius: 15px;
    border-width: 5px;
    border-color: black;
    padding: 5px;
    height: 70px;
    width: 140px;
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
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        props: [
            'url_openstreetmap',
        ],
        data() {
            return {
                expanded: false,
            }
        },
        computed: {
            ...mapState(['map']),
        },
        methods: {
            ...mapActions(['requestMap']),
            toggleExpand() {
                this.expanded = !this.expanded;
            },
            renderMap: function() {
                const points = {
                    'DEFAULT_CENTER': [-8.8315139, 125.6199236,9],
                    'DEFAULT_ZOOM': 9,
                }
                this.timormap = L.map('mapid').setView(points.DEFAULT_CENTER, points.DEFAULT_ZOOM);
                L.tileLayer(this.url_openstreetmap, {minZoom: 8, maxZoom: 18}).addTo(this.timormap);
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
        watch: {
            "map.list": function() {
                this.renderGeoJSON(this.map.list);
            }
        },
        mounted() {
            this.renderMap();
            this.requestMap();
        },
    }
</script>
