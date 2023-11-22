import { createStore } from 'vuex'

export default createStore({
    state: {
        firstName: 'Tanner',
        lastName: 'Doe',
        favorites: []
    },
    mutations: {
        UPDATE_FAVORITES(state, payload) {
            state.favorites = payload
        }
    },
    actions: {
        addToFavorites(context, payload) {
            const favorites = context.state.favorites
            favorites.push(payload)
            context.commit('UPDATE_FAVORITES', payload)
        }
    },
    getters: {

    }
})