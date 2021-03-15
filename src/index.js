// hello this is a comment
console.log('YAAY');

import { createApp } from 'vue';
import App from './App.vue';
import Istoria_viazen from './Istoria_viazen.vue';

export function mountApp(element, properties) {
    console.log('mounting app')
    createApp(App, properties).mount(element);
    createApp(Istoria_viazen, properties).mount(element);
}
