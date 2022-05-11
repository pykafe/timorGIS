<template>
    <span class="loader" v-if="istoria.requesting">Loading...</span>
    <span class="loader" v-if="istoria.error">Sorry!</span>
    <div class="row" v-if="istoria.list !== null">
        <div class="col-md-5">
            <div class="row">
                <div class="col-md-12">
                    <a href="#" type="button" class="btn btn-default back-button">Back</a>
                    <p class="card-text">
                        <small class="text-muted">Hosi | {{ $filters.formatDuration(selectedIstoria.duration_of_trip) }}</small>
                    </p>
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
            <div class="card-body">
                <h5 class="card-title">{{ selectedIstoria.title}}</h5>
                <p class="card-text">{{ selectedIstoria.description }}</p>
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
    .back-button {
        font-size: .7rem ;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
        margin-right: 0.5rem;
        border-radius: 2rem;
        background: #fff;
        color: rgba(29,161,242,1.00);
        padding-right: 1rem;
        padding-left: 1rem;
        padding-top: 7px;
        padding-bottom: 4px;
        border: 1px solid rgba(29,161,242,1.00);
        letter-spacing: .8px;
        border-color: rgba(29,161,242,1.00);
        margin-top: 0.9rem;
        font-weight: bolder;
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
                return this.images.list.find(image => image.id == this.$route.params.selected_image);
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
            ...mapActions(['requestImages', 'requestIstoria']),
        },
        mounted() {
            this.requestImages();
            this.requestIstoria();
        },
    }
</script>
