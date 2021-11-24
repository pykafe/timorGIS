<template>
    <span class="loader" v-if="images.requesting">Loading...</span>
    <span class="loader" v-if="images.error">Sorry!</span>
    <div class="search-input-container">
        <input class="form-control" type="text" v-model="searchJourney" placeholder="Search journey">
    </div>
    <router-link :to="{name: 'new_istoria'}">
        <a href="#" class="btn btn-primary add-new-journey">Add my journey</a>
    </router-link>
    <div class="images_container" v-if="images.list">
        <div 
            v-for="image in resultJourneyQuery" v-bind:key="image.id" @click="selectImgObject(image.image)">
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
                            {{ $filters.shorten(image.istoria.description, 75) }}
                        </p>
                        <span>Uploaded by {{ image.istoria.creator.fullname }}</span>
                    </div>
                </div>
            </div>
        </div>
        <p class="centered" v-if="resultJourneyQuery.length === 0">No results found for query "{{ searchJourney }}"</p>
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
    width: 95%;
    height: 95%;
    position: absolute;
    left: 10px;
    top: 10px;
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
.search-input-container {
    z-index: 1;
    width: 100%;
    max-width: 628px;
    margin: 0 auto;
    -webkit-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
}
.centered {
    position: absolute;
    margin: auto;
    display: block;
    bottom: 0px;
    top: 120px;
    left: 50%;
    transform: translate(-50%, 0);
}
</style>

<script>
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'
    import 'viewerjs/dist/viewer.css'
    import { api as viewerApi } from "v-viewer"

    export default {
        props: [
            'url_media',
        ],
        data() {
            return {
                rollover_image_id: 0,
                searchJourney: null,
            }
        },
        computed: {
            ...mapState(['images']),
            resultJourneyQuery() {
                if (this.searchJourney) {
                    return this.images.list.filter(journey => {
                        return this.searchJourney
                            .toLowerCase()
                            .split(" ")
                            .every(v => journey.istoria.title.toLowerCase().includes(v));
                    });
                } else {
                    return this.images.list;
                }
            },
        },
        methods: {
            ...mapActions(['requestImages']),
            rolloverImage(id){
                this.rollover_image_id = id;
            },
            imageCardStyle(image) {
                return `background-image: url(${ this.url_media }${ image.image})`;
            },
            selectImgObject (image) {
                let img = [];
                const urlMedia = this.url_media;
                this.images.list.forEach( function(image){
                    img.push(urlMedia + image.image)
                });
                const indexId = img.indexOf(urlMedia + image);
                const $viewer = viewerApi({
                    options: {
                        toolbar: true,
                        initialViewIndex: indexId,
                        inline: true, 
                        button: true, 
                        navbar: true, 
                        title: false, 
                        toolbar: true, 
                        tooltip: true, 
                        movable: true, 
                        zoomable: false, 
                        rotatable: false, 
                        scalable: false, 
                        transition: true, 
                        fullscreen: true, 
                        keyboard: true, 
                    },
                    images: img 
                });
            },
        },
        mounted() {
            this.requestImages();
        },
    }
</script>
