import { createRouter, createWebHashHistory } from 'vue-router';
import PhotoTimor from './components/PhotoTimor.vue';
import Istoria from './components/Istoria.vue';
import Map from './components/Map.vue';
import AddIstoria from './components/AddIstoria.vue';
import UpdateIstoria from './components/UpdateIstoria.vue';

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
                },
                map: {
                    'url_openstreetmap': properties.urls.openstreetmap,
                }
            },
        },
        { 
            path: '/new_istoria',
            name: 'new_istoria',
            components: {
                default: AddIstoria,
            },
        },
        { 
            path: '/update_istoria',
            name: 'update_istoria',
            components: {
                default: UpdateIstoria,
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