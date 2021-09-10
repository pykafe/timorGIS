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
        <div class="image_selected" v-show="!!$route.params.selected_id">
            <div tabindex="-1" role="dialog">
                <div class="modal-dialog modal-lg modals-lg" role="document">
                    <div class="modal-content">
                        <div class="modals-header">
                            <router-link :to="{name: 'photos'}" class="close close_comment">
                                <span class="closes">&times;</span>
                            </router-link>
                            <h4 class="modal-title" id="gridSystemModalLabel">Ilha Jaco</h4>
                        </div>
                        <div class="modal-body">
                            <div class="row">
                                <div class="col-md-5">
                                    <!--
                                    <div class="row">
                                        <div class="col-md-12">
                                            <p>Hosi | April 22, 2021 - April 23, 2021</p>
                                        </div>
                                    </div>
                                    -->
                                    <div class="row">
                                        <div class="col-md-12">
                                            <img v-bind:src="selectedImageSrc" class="size_images"/>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12">
                                            <p>Kria hosi Mario April 29, 2021, 12:34 p.m.</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-7">
                                    <div class="row">
                                        <div class="col-md-12 comment_scroll">
                                            <div class="modal-content">
                                                <div class="modal-body">
                                                <b>Joanico Barros  12:33 AM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                <b>Mariano de Deus  2:33 PM</b>
                                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12">
                                            <span class="comment_input">
                                                <input type="text" name="comments" placeholder="Comments..."/>
                                                <button type="submit" class="btn btn-primary">Save</button>
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
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
.size_images {
    height: calc(88vh - 64px - 14px);
    width: 100%;
}
.comment_input {
    display: inline-block;
    width: 85%;
    position: relative;
    bottom: -0.5rem;
    white-space: nowrap;
}
.comment_scroll {
    overflow-y: auto;
    min-height: 0;
    max-height: 480px;
    right: 20px;
}

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px grey;
  border-radius: 10px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: grey;
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: var(--blue-2);
}
.close_comment {
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 50%;
    cursor: pointer;
    height: 80px;
    overflow: hidden;
    position: absolute;
    right: -40px;
    top: -40px;
    -webkit-transition: background-color 0.15s;
    transition: background-color 0.15s;
    width: 80px;
}
.closes {
    color: white;
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
