import { createApp } from 'vue';
import App from './App.vue';
import getRouter from './Router.js';
import getStore from './Store.js';

export function mountApp(element, properties) {

    const app = createApp(App)

    app.config.globalProperties.$filters = {
         description(text){
            let length = 50;
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

    const store = getStore(properties);
    app.use(store);

    app.mount(element);
}
