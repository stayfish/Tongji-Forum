import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            user: {}
        }
    },
    mutations: {
        set_userinfo(state, user) {
            state.user = user
        }
    }
})

export default store