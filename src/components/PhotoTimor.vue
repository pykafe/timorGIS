<template>
    requesting or not? {{ images.requesting }}
    error? {{ images.error }}
    <div class="images_container" v-if="images.list">
        <router-link 
            v-for="image in images.list" v-bind:key="image.id"
            :to="{name: 'photos', params: {selected_id: image.id}}">
            <div
                @mouseover="rolloverImage(image.id)"
                @mouseleave="rollover_image_id = 0"
                class="image_card rounded"
                v-bind:style="imageCardStyle(image)">
                <div class="istoria_title">
                    {{ image.istoria.title }}
                    <div v-if="image.id == rollover_image_id">
                        <a href="#">See more..</a>
                        <p>
                            {{ $filters.shorten(image.istoria.description, 75) }}
                        </p>
                        <span>Uploaded by {{ image.istoria.creator }}</span>
                    </div>
                </div>
            </div>
        </router-link>
        <router-link :to="{name: 'photos'}">
            <div class="image_selected" v-show="!!$route.params.selected_id">
                <div tabindex="-1" role="dialog">
                    <div class="modal-dialog modal-lg modals-lg" role="document">
                        <div class="modal-content">
                            <div class="modals-header">
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                                <h4 class="modal-title" id="gridSystemModalLabel">Modal title</h4>
                            </div>
                             <div class="modal-body">
                                <img v-bind:src="selectedImageSrc" width="600"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </router-link>
    </div>
</template>
<style scoped>
.images_container {
    padding-top: 15px;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    column-gap: 15px;
    row-gap: 15px;
}
.image_card {
    height: 200px;
    background-size: cover;
    cursor: pointer;
}
.image_card .istoria_title {
    color:  rgb(255, 255, 255);
    margin: 5px;
    padding: 3px;
    background-color: rgba(44, 44, 43, 0.336);
    border-radius: 3px;
}
.image_selected {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 1px;
    right: 10px;
    top: 1px;
}
.modals-lg {
    max-width: 100%!important;
    margin: 0px!important;
}
.modals-header {
    display: -ms-flexbox;
    /* display: flex; */
    -ms-flex-align: start;
    align-items: flex-start;
    -ms-flex-pack: justify;
    justify-content: space-between;
    padding: 1rem 1rem;
    /* border-bottom: 1px solid #dee2e6; */
    border-top-left-radius: calc(.3rem - 1px);
    border-top-right-radius: calc(.3rem - 1px);
}

</style>

<script>
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        props: [
            'url_media',
        ],
        data() {
            return {
                rollover_image_id: 0,
                selected_image_id: 0,
            }
        },
        computed: {
            selectedImage() {
                return this.images.list.find(image => image.id == this.$route.params.selected_id);
            },
            selectedImageSrc() {
                return this.selectedImage !== undefined
                    ? `${ this.url_media }${ this.selectedImage.image}`
                    : ""
            },
            ...mapState(['images']),
        },
        methods: {
            ...mapActions(['requestImages']),
            rolloverImage(id){
                this.rollover_image_id = id;
            },
            imageCardStyle(image) {
                return `background-image: url(${ this.url_media }${ image.image})`;
            },
        },
        mounted() {
            this.requestImages();
        },
    }
</script>
