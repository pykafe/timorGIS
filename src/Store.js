import { createStore } from 'vuex'

export default function getStore(properties) {
    // Create a new store instance.
    const store = createStore({
        state () {
            return {
                amILoggedIn: null,
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
                map: {
                    list: null,
                    requesting: false,
                    error: null,
                },
            }
        },
        getters: {
            csrfTokenInput: state => {
                return properties.csrfTokenInput;
            }
        },
        mutations: {
            setLoggedIn(state, payload) {
                state.amILoggedIn = payload.amILoggedIn;
            },
            requestingImages(state, payload) {
                state.images.requesting = payload.requesting;
            },
            setImagesList(state, payload) {
                state.images.list = payload.images;
            },
            setImagesError(state, payload) {
                state.images.error = payload;
            },

            requestingIstoria(state, payload) {
                state.istoria.requesting = payload.requesting;
            },
            setIstoriaList(state, payload) {
                state.istoria.list = payload.istoria;
            },
            setIstoriaError(state, payload) {
                state.istoria.error = payload;
            },

            requestingMap(state, payload) {
                state.map.requesting = payload.requesting;
            },
            setMapList(state, payload) {
                state.map.list = payload.map;
            },
            setMapError(state, payload) {
                state.map.error = payload;
            },
        },
        actions: {
            submitNewJourney(context, payload) {
                // TODO: commit a mutation to tell the app we are submitting a new istoria

                // build the body required
                const formData = new FormData(payload.srcElement);

                fetch(properties.urls.add_journey, { method: 'POST', body: formData }).then(response=> {
                    // react to success or failure of request
                    return response.json()
                }).then(response_data => {
                    // TODO add the data to the state here using a mutation
                    console.log(response_data.photos)
                }).catch((err) => {
                    // TODO We have an error, tel the user about it
                }).finally(() => {
                    // TODO: commit a mutation to tell the app we are done submitting a new istoria
                    // TODO: route the app to the istoria list, or the istoria page
                });
            },
            detectLogin(context) {
                fetch(properties.urls.login).then(response => {
                    if ( response.status === 401) {
                        context.commit('setLoggedIn', {amILoggedIn: false});
                    }
                    if ( response.status === 200) {
                        context.commit('setLoggedIn', {amILoggedIn: true});
                    }
                });
            },
            requestImages(context) {
                // request the images are retrieved
                if (context.state.images.list === null) {
                    context.commit('requestingImages', {requesting: true});

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
                    context.commit('requestingIstoria', {requesting: true});

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
            },
            requestMap(context) {
                // request the images are retrieved
                if (context.state.map.list === null) {
                    context.commit('requestingMap', {requesting: true});

                    // go get the images
                    fetch(properties.urls.geojson).then(response => {
                        return response.json();
                    }).then(map => {
                        // everything is good, we have the istoria
                        context.commit('setMapList', {map});
                    }).catch((err) => {
                        // something bad has happened, show an error
                        context.commit('setMapError', {err});
                    }).finally(() => {
                        // we have definitely finished requesting
                        context.commit('requestingMap', false);
                    });
                }
            }
        },
        strict: process.env.NODE_ENV !== 'production',
    })
    return store;
}