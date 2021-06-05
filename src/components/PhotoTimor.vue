<template>
    <div class="images_container">
        <router-link 
            v-for="image in images" v-bind:key="image.id"
            :to="{name: 'photos', params: {selected_id: image.id}}">
            <div
                @mouseover="rolloverImage(image.id)"
                @mouseleave="rollover_image_id = 0"
                class="image_card"
                v-bind:style="imageCardStyle(image)">
                <div class="istoria_title">
                    {{ image.istoria.title }}
                    <div v-if="image.id == rollover_image_id">
                        <a href="#">See more..</a>
                        <p>
                            {{ $filters.description(image.istoria.description) }}
                        </p>
                        <span>Uploaded by {{ image.istoria.creator }}</span>
                    </div>
                </div>
            </div>
        </router-link>
    </div>
    <router-link :to="{name: 'photos'}">
        <div class="image_selected" v-show="!!$route.params.selected_id">
            <img v-bind:src="selectedImageSrc" width="600" />
        </div>
    </router-link>
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
    width: 95%;
    height: 95%;
    position: absolute;
    left: 10px;
    top: 10px;
}
</style>

<script>
    export default {
        props: [
            'url_images',
            'url_media',
        ],
        data() {
            return {
                images: [],
                rollover_image_id: 0,
                selected_image_id: 0,
            }
        },
        computed: {
            selectedImage() {
                return this.images.find(image => image.id == this.$route.params.selected_id);
            },
            selectedImageSrc() {
                return this.selectedImage !== undefined
                    ? `${ this.url_media }${ this.selectedImage.image}`
                    : ""
            }
        },
        methods: {
            rolloverImage(id){
                this.rollover_image_id = id;
            },
            imageCardStyle(image) {
                return `background-image: url(${ this.url_media }${ image.image})`;
            },
            getImages: function() {
                // fetch is returning a Promise which will succeed with some geojson
                // OR fail with an error
                return fetch(this.url_images).then(response => {
                    return response.json()
                });
            },
            renderImages: function(images) {
                this.images = images;
            },
        },
        mounted() {
            this.getImages().then(this.renderImages);
        },
    }
</script>
