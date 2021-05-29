// hello this is a comment
console.log('YAAY');

import { createApp } from 'vue';
import App from './App.vue';

export function mountApp(element, properties) {
    console.log('mounting app')
    const app = createApp(App, properties)
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
    app.mount(element);
}
