// hello this is a comment
console.log('YAAY');

import { createApp } from 'vue';
import App from './App.vue';

export function mountApp(element, properties) {
    console.log('mounting app')
    createApp(App, properties).mount(element);
}
