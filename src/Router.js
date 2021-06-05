import { createRouter, createWebHashHistory } from 'vue-router';
import PhotoTimor from './components/PhotoTimor.vue';
import Map from './components/Map.vue';

export default function getRouter(properties) {

    const routes = [
        { 
            path: '/photos/:selected_id(\\d+)?',
            name: 'photos',
            component: PhotoTimor,
            props: { 
                'url_images': properties.urls.images,
                'url_media': properties.urls.media_url,
            },
        },
        { 
            path: '/map',
            component: Map,
            props: { 
                'url_openstreetmap': properties.urls.openstreetmap,
                'url_geojson': properties.urls.geojson,
            },
        }
    ];

    const router = createRouter({
        // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
        history: createWebHashHistory(),
        routes, // short for `routes: routes`
    });

    return router;
}