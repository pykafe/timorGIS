<template>
    <div class="images_container">
        <div v-for="image in images" v-bind:key="image.pk" class="image_card"
            v-bind:style="imageCardStyle(image)">
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
            }
        },
        methods: {
            imageCardStyle(image) {
                return `background-image: url(${ this.url_media }${ image.fields.image})`;
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