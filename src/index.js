import { createApp } from 'vue';
import App from './App.vue';
import getRouter from './Router.js';
import getStore from './Store.js';
import VueViewer from 'v-viewer'
import moment from 'moment';


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
        formatDate(value){
            if (value) {
               return moment(String(value)).format('MMMM MM, YYYY hh:mm a')
            }
        },
        formatDuration(value){
            if (value){
                let duration_of_trip = [];
                let date_slice = value.slice(2, -2);
                let date_str = date_slice.toString();
                let date_split = date_str.split(',');
                date_split.forEach(function(date){
                    const data = moment(date).format('LL');
                    duration_of_trip.push(data);
                })
                return duration_of_trip.join(" - ");
            }
        },
    }
    app.use(VueViewer)

    const router = getRouter(properties);
    app.use(router);

    const store = getStore(properties, router);
    app.use(store);

    app.mount(element);
}
