import { createRouter, createWebHashHistory } from 'vue-router';
import PhotoTimor from './components/PhotoTimor.vue';
import Istoria from './components/Istoria.vue';
import Map from './components/Map.vue';

export default function getRouter(properties) {

    const routes = [
        { 
            path: '/photos/:selected_id(\\d+)?',
            alias: '/',
            name: 'photos',
            components: {
                default: PhotoTimor,
                map: Map,
            },
            props: {
                default: {
                    'url_media': properties.urls.media_url,
                },
                map: {
                    'url_openstreetmap': properties.urls.openstreetmap,
                    'url_geojson': properties.urls.geojson,
                }
            },
        },
        { 
            path: '/istoria',
            name: 'istoria',
            components: {
                default: Istoria,
                map: Map,
            },
            props: {
                default: {
                    'url_istoriaviazen': properties.urls.istoriaviazen,
                },
                map: {
                    'url_openstreetmap': properties.urls.openstreetmap,
                    'url_geojson': properties.urls.geojson,
                }
            },
        },
    ];

    const router = createRouter({
        // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
        history: createWebHashHistory(),
        routes, // short for `routes: routes`
    });

    return router;
}