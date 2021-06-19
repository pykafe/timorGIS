import { createStore } from 'vuex'

export default function getStore(properties) {
    // Create a new store instance.
    const store = createStore({
        state () {
            return {
                count: 0
            }
        },
        mutations: {
            increment(state) {
                state.count++
            }
        },
        getters: {
            countPlus5(state) {
              return state.count + 5;
            }
        },
    })
    return store;
}