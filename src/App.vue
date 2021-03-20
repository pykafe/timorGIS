
<template>
    <div class="container-fluid">
        <div class="images_container">
            <div v-for="image in images" v-bind:key="image.pk" class="image_card">
                <img v-bind:src="`${urls.media_url}${ image.fields.image}`" width="200"/>
            </div>
        </div>
        <div id="mapInset">
            <div id="mapid"></div>
        </div>
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
    export default {
        props: [
            'urls',
        ],
        data() {
            return {
                images: [],
                istoriaviazen: [],
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
            getImages: async function() {
                // Do we have this response in our cache???
                const cache = await caches.open("timorgis");
                let apiMatch = await cache.match(this.urls.images);
                if (apiMatch === undefined) {
                    // we don't have a match
                    await cache.add(this.urls.images);
                    apiMatch = await cache.match(this.urls.images);
                }

                // Do the conditional request
                const response = await fetch(this.urls.images, {
                    headers: {'If-Modified-Since': apiMatch.headers.get('Last-Modified')}
                });

                // is the response a 200 or a 304?
                if( response.ok ) {
                    cache.put(this.urls.images, response);
                    return response.json();
                } else {
                    return apiMatch.json();
                }

            },
            getIstoriaviazen: function() {
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.urls.istoriaviazen).then(response => {
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
            },
            renderIstoriaviazen: function(istoriaviazen) {
                console.log(istoriaviazen);
                this.istoriaviazen = istoriaviazen;
            }
        },
        mounted() {
            this.renderMap();
            this.getGeoJSON().then(this.renderGeoJSON);
            this.getImages().then(this.renderImages);
            this.getIstoriaviazen().then(this.renderIstoriaviazen);
        },
    }
</script>