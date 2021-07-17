<template>
    requesting or not? {{ istoria.requesting }}
    error? {{ istoria.error }}
    <div v-if="istoria.list">
        <div v-for="viazen in istoria.list" v-bind:key="viazen.pk" class="viazen_card">
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">{{ viazen.fields.title}}</h5>
                    <p class="card-text">{{ viazen.fields.description }}</p>
                    <p class="card-text"><small class="text-muted">Created at: {{ viazen.fields.created_at }}</small></p>
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