import { createApp } from 'vue';
import App from './App.vue';
import getRouter from './Router.js';
import getStore from './Store.js';

export function mountApp(element, properties) {

    const app = createApp(App)

    app.config.globalProperties.$filters = {
        shorten(text, length){
            let suffix = '...';
            if (text.length > length) {
                return text.substring(0, length) + suffix;
            } else {
                return text;
            }
        },
    }

    const router = getRouter(properties);
    app.use(router);

    const store = getStore(properties, router);
    app.use(store);

    app.mount(element);
}
