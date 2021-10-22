<template>
    requesting or not? {{ istoria.requesting }}
    error? {{ istoria.error }}
    <div v-if="istoria.list">
        <div v-for="viazen in istoria.list" v-bind:key="viazen.pk" class="viazen_card">
            <div class="card mb-3">
                <div class="card-body">
                    <div class="dropdown dropdown-edit-and-delete">
                        <span class="dropdown-toggle edit-and-delete-toggle" type="button" data-toggle="dropdown"></span>
                        <ul class="dropdown-menu menu-dropdown">
                            <li class="hover-list">
                                <router-link :to="{name: 'update_istoria'}">
                                    <a href="#" class="btn btn-primary add-new-journey">Edit journey</a>
                                </router-link>
                            </li>
                        </ul>
                    </div>
                    <h5 class="card-title">{{ viazen.title}}</h5>
                    <p class="card-text">{{ viazen.description }}</p>
                    <p class="card-text"><small class="text-muted">Created at: {{ viazen.created_at }}</small></p>
                </div>
            </div>
        </div>
    </div>
</template>

<style  scoped>
</style>

<script>
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        computed: {
            ...mapState(['istoria']),
        },
        methods: {
            ...mapActions(['requestIstoria']),
        },
        mounted() {
            this.requestIstoria();
        },
    }
</script>