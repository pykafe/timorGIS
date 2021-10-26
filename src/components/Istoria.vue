<template>
    <span class="loader" v-if="istoria.requesting">Loading...</span>
    <span class="loader" v-if="istoria.error">Sorry!</span>
    <div class="row">
        <div class="col-md-5">
            <div class="row">
                <div class="col-md-12">
                    <h5 class="card-title">{{ selectedIstoria.title}}</h5>
                    <p class="card-text"><small class="text-muted">Hosi | April 22, 2021 - April 23, 2021</small></p>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12">
                    <img v-bind:src="selectedImageSrc" class="size_images rounded"/>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12">
                    <p class="card-text"><small class="text-muted">Kria hosi {{ selectedImage.istoria.creator.fullname !== "" ?selectedImage.istoria.creator.fullname: selectedImage.istoria.creator.username }} {{ $filters.formatDate(selectedImage.istoria.created_at) }}</small></p>
                </div>
            </div>
        </div>
        <div class="col-md-7">
            <div class="viazen_card">
                <div class="card mb-3">
                    <div class="card-body">
                        <p class="card-text">{{ selectedIstoria.description }}</p>
                        <!--<p class="card-text"><small class="text-muted">Created at: {{ selectedIstoria.created_at }}</small></p>-->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style  scoped>
.size_images {
    width: 100%;
}
.loader {
    position: absolute;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    text-align: center;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    z-index: 401;
    font-size: 32px;
    background-color: rgb(8 8 8 / 87%);
    color: var(--white);
}
</style>

<script>
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        props: [
            'url_media',
        ],
        computed: {
            selectedImage() {
                return this.images.list.find(image => image.istoria.pk == this.$route.params.journey_selected);
            },
            selectedImageSrc() {
                return this.selectedImage !== undefined
                    ? `${ this.url_media }${ this.selectedImage.image}`
                    : ""
            },
            selectedIstoria(){
                return this.istoria.list.find(viazen => viazen.pk == this.$route.params.journey_selected);
            },
            ...mapState(['istoria', 'images']),
        },
        methods: {
            ...mapActions(['requestIstoria', 'requestImages']),
        },
        mounted() {
            this.requestIstoria();
            this.requestImages();
        },
    }
</script>
