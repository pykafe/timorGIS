<template>
    <div class="images_container">
        <div @mouseover="selectedTitle(image.id)" @mouseleave="image_id = 0" v-for="image in images" v-bind:key="image.id" class="image_card"
            v-bind:style="imageCardStyle(image)">
            <div class="istoria_title">
                {{ image.istoria.title }}
                <div v-if="image.id == image_id">
                    <a href="#">See more..</a>
                    <p>
                        {{ $filters.description(image.istoria.description) }}
                    </p>
                    <span>Uploaded by {{ image.istoria.creator }}</span>
                </div>
            </div>
        </div>
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
                image_id: 0,
            }
        },
        methods: {
            selectedTitle(id){
                this.image_id = id;
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
