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
                count: 0
            }
        },
        mutations: {
            increment(state) {
                state.count++
            },
            requestingImages(state, requesting) {
                state.images.requesting = requesting;
            },
            setImagesList(state, payload) {
                state.images.list = payload.images;
            },
            setImagesError(state, payload) {
                state.images.error = payload;
            }
        },
        getters: {
            countPlus5(state) {
                return state.count + 5;
            }
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
                        context.commit('setImagesList', {images: images});
                    }).catch((err) => {
                        // something bad has happened, show an error
                        context.commit('setImagesError', {err});
                    }).finally(() => {
                        // we have definitely finished requesting
                        context.commit('requestingImages', false);
                    });
                }
            }
        },
        strict: process.env.NODE_ENV !== 'production',
    })
    return store;
}