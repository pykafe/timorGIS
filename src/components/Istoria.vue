<template>
    {{ count }}
    <br/>{{ countPlus5 }}
    <div v-for="viazen in istoriaviazen" v-bind:key="viazen.pk" class="viazen_card">
        <div class="card mb-3">
            <div class="card-body">
                <h5 class="card-title">{{ viazen.fields.title}}</h5>
                <p class="card-text">{{ viazen.fields.description }}</p>
                <p class="card-text"><small class="text-muted">Created at: {{ viazen.fields.created_at }}</small></p>
            </div>
        </div>
    </div>
</template>

<style  scoped>
</style>

<script>
    import { mapState } from 'vuex'
    import { mapGetters } from 'vuex'

    export default {
        props: [
            'url_istoriaviazen',
        ],
        data() {
            return {
                istoriaviazen: [],
            }
        },
        computed: {
            ...mapState(['count']),
            ...mapGetters(['countPlus5']),
        },
        methods: {
            getIstoriaviazen: function() {
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.url_istoriaviazen).then(response => {
                    return response.json()
                });
            },
            renderIstoriaviazen: function(istoriaviazen) {
                console.log(istoriaviazen);
                this.istoriaviazen = istoriaviazen;
            }
        },
        mounted() {
            this.getIstoriaviazen().then(this.renderIstoriaviazen);
        },
    }
</script>