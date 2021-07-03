import { createStore } from 'vuex'

export default function getStore(properties) {
    // Create a new store instance.
    const store = createStore({
        state () {
            return {
                images: {
                    list: null,
                    requesting: false,
                    error: null,
                },
                istoria: {
                    list: null,
                    requesting: false,
                    error: null,
                },
            }
        },
        mutations: {
            requestingImages(state, requesting) {
                state.images.requesting = requesting;
            },
            setImagesList(state, payload) {
                state.images.list = payload.images;
            },
            setImagesError(state, payload) {
                state.images.error = payload;
            },
            requestingIstoria(state, requesting) {
                state.istoria.requesting = requesting;
            },
            setIstoriaList(state, payload) {
                state.istoria.list = payload.istoria;
            },
            setIstoriaError(state, payload) {
                state.istoria.error = payload;
            },
        },
        getters: {
        },
        actions: {
            requestImages(context) {
                // request the images are retrieved
                if (context.state.images.list === null) {
                    context.commit('requestingImages', true);

                    // go get the images
                    fetch(properties.urls.images).then(response => {
                        return response.json();
                    }).then(images => {
                        // everything is good, we have the images
                        context.commit('setImagesList', {images});
                    }).catch((err) => {
                        // something bad has happened, show an error
                        context.commit('setImagesError', {err});
                    }).finally(() => {
                        // we have definitely finished requesting
                        context.commit('requestingImages', false);
                    });
                }
            },
            requestIstoria(context) {
                // request the images are retrieved
                if (context.state.istoria.list === null) {
                    context.commit('requestingIstoria', true);

                    // go get the images
                    fetch(properties.urls.istoriaviazen).then(response => {
                        return response.json();
                    }).then(istoria => {
                        // everything is good, we have the istoria
                        context.commit('setIstoriaList', {istoria});
                    }).catch((err) => {
                        // something bad has happened, show an error
                        context.commit('setIstoriaError', {err});
                    }).finally(() => {
                        // we have definitely finished requesting
                        context.commit('requestingIstoria', false);
                    });
                }
            }
        },
        strict: process.env.NODE_ENV !== 'production',
    })
    return store;
}