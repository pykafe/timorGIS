import { createRouter, createWebHashHistory } from 'vue-router';
import PhotoTimor from './components/PhotoTimor.vue';
import Istoria from './components/Istoria.vue';
import Map from './components/Map.vue';
import AddIstoria from './components/AddIstoria.vue';
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default function getRouter(properties) {

    const routes = [
        { 
            path: '/photos/:selected_id(\\d+)?',
            alias: '/',
            name: 'photos',
            components: {
                default: PhotoTimor,
                header: Header,
                footer: Footer,
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
                header: Header,
                footer: Footer,
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
                header: Header,
                footer: Footer,
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