<template>
    <span class="loader" v-if="images.requesting">Loading...</span>
    <span class="loader" v-if="images.error">Sorry!</span>
    <router-link :to="{name: 'new_istoria'}">
        <a href="#" class="btn btn-primary add-new-journey">Add my journey</a>
    </router-link>
    
    <div class="images_container" v-if="images.list">
        <div 
            v-for="image in images.list" v-bind:key="image.id">
            <div
                @mouseover="rolloverImage(image.id)"
                @mouseleave="rollover_image_id = 0"
                class="image_card rounded" v-bind:style="imageCardStyle(image)">
                <div class="istoria_title">
                    {{ image.istoria.title }}
                    <div v-if="image.id == rollover_image_id">
                        <router-link :to="{name: 'istoria', params: {journey_selected: image.istoria.pk }}">
                            <a href="#">See more..</a>
                        </router-link>
                        <p>
                            {{ $filters.shorten(image.istoria.description, 75) }}
                        </p>
                        <span>Uploaded by {{ image.istoria.creator.fullname }}</span>
                        <span class="expand-arrows"><svg  @click="selectImgObject(image.image)" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrows-angle-expand" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M5.828 10.172a.5.5 0 0 0-.707 0l-4.096 4.096V11.5a.5.5 0 0 0-1 0v3.975a.5.5 0 0 0 .5.5H4.5a.5.5 0 0 0 0-1H1.732l4.096-4.096a.5.5 0 0 0 0-.707zm4.344-4.344a.5.5 0 0 0 .707 0l4.096-4.096V4.5a.5.5 0 1 0 1 0V.525a.5.5 0 0 0-.5-.5H11.5a.5.5 0 0 0 0 1h2.768l-4.096
                        4.096a.5.5 0 0 0 0 .707z"/></svg></span>
                    </div>
                </div>
            </div>
            <span>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-hand-thumbs-up" viewBox="0 0 16 16">
                    <path d="M8.864.046C7.908-.193 7.02.53 6.956 1.466c-.072 1.051-.23 2.016-.428 2.59-.125.36-.479 1.013-1.04 1.639-.557.623-1.282 1.178-2.131 1.41C2.685 7.288 2 7.87 2 8.72v4.001c0 .845.682 1.464 1.448 1.545 1.07.114 1.564.415 2.068.723l.048.03c.272.165.578.348.97.484.397.136.861.217 1.466.217h3.5c.937 0 1.599-.477 1.934-1.064a1.86 1.86 0 0 0 .254-.912c0-.152-.023-.312-.077-.464.201-.263.38-.578.488-.901.11-.33.172-.762.004-1.149.069-.13.12-.269.159-.403.077-.27.113-.568.113-.857 0-.288-.036-.585-.113-.856a2.144 2.144 0 0 0-.138-.362 1.9 1.9 0 0 0 .234-1.734c-.206-.592-.682-1.1-1.2-1.272-.847-.282-1.803-.276-2.516-.211a9.84 9.84 0 0 0-.443.05 9.365 9.365 0 0 0-.062-4.509A1.38 1.38 0 0 0 9.125.111L8.864.046zM11.5 14.721H8c-.51 0-.863-.069-1.14-.164-.281-.097-.506-.228-.776-.393l-.04-.024c-.555-.339-1.198-.731-2.49-.868-.333-.036-.554-.29-.554-.55V8.72c0-.254.226-.543.62-.65 1.095-.3 1.977-.996 2.614-1.708.635-.71 1.064-1.475 1.238-1.978.243-.7.407-1.768.482-2.85.025-.362.36-.594.667-.518l.262.066c.16.04.258.143.288.255a8.34 8.34 0 0 1-.145 4.725.5.5 0 0 0 .595.644l.003-.001.014-.003.058-.014a8.908 8.908 0 0 1 1.036-.157c.663-.06 1.457-.054 2.11.164.175.058.45.3.57.65.107.308.087.67-.266 1.022l-.353.353.353.354c.043.043.105.141.154.315.048.167.075.37.075.581 0 .212-.027.414-.075.582-.05.174-.111.272-.154.315l-.353.353.353.354c.047.047.109.177.005.488a2.224 2.224 0 0 1-.505.805l-.353.353.353.354c.006.005.041.05.041.17a.866.866 0 0 1-.121.416c-.165.288-.503.56-1.066.56z"/>
                </svg>
                <router-link :to="{name: 'photos', params: {selected_id: image.id }}">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chat-dots" viewBox="0 0 16 16">
                        <path d="M5 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
                        <path d="m2.165 15.803.02-.004c1.83-.363 2.948-.842 3.468-1.105A9.06 9.06 0 0 0 8 15c4.418 0 8-3.134 8-7s-3.582-7-8-7-8 3.134-8 7c0 1.76.743 3.37 1.97 4.6a10.437 10.437 0 0 1-.524 2.318l-.003.011a10.722 10.722 0 0 1-.244.637c-.079.186.074.394.273.362a21.673 21.673 0 0 0 .693-.125zm.8-3.108a1 1 0 0 0-.287-.801C1.618 10.83 1 9.468 1 8c0-3.192 3.004-6 7-6s7 2.808 7 6c0 3.193-3.004 6-7 6a8.06 8.06 0 0 1-2.088-.272 1 1 0 0 0-.711.074c-.387.196-1.24.57-2.634.893a10.97 10.97 0 0 0 .398-2z"/>
                    </svg>
                </router-link>
            </span>
        </div>
        <div class="image_selected" v-show="!!$route.params.selected_id">
            <div tabindex="-1" role="dialog">
                <div class="modal-dialog modals-lg" role="document">
                    <span class="loader" v-if="comments.requesting">Loading...</span>
                    <span class="loader" v-if="comments.error">Sorry!</span>
                    <div class="modal-content">
                        <div class="modals-header">
                            <router-link :to="{name: 'photos'}" class="viewer-button viewer-close">
                                <span class="closes">&times;</span>
                            </router-link>
                            <span v-for="image in images.list" v-bind:key="image.id">
                                <span v-if="image.id == $route.params.selected_id">
                                    <h4 class="modal-title" id="gridSystemModalLabel">{{ image.istoria.title }}</h4>
                                </span>
                            </span>
                        </div>
                        <div class="modal-body">
                            <div class="row">
                                <div class="col-md-6">
                                    <!--
                                    <div class="row">
                                        <div class="col-md-12">
                                            <p>Hosi | April 22, 2021 - April 23, 2021</p>
                                        </div>
                                    </div>
                                    -->
                                    <div class="row modal-img">
                                        <div class="col-md-12">
                                            <img v-bind:src="selectedImageSrc" class="size_images rounded"/>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12" v-for="image in images.list" v-bind:key="image.id">
                                            <span v-if="image.id == $route.params.selected_id">
                                                <p class="card-text"><small class="text-muted">Foto hosi {{ image.istoria.creator.fullname !== "" ? image.istoria.creator.fullname: image.istoria.creator.username }} {{ $filters.formatDate(image.istoria.created_at) }}</small></p>
                                            </span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="row">
                                        <h4 class="modal-title" id="gridSystemModalLabel">Comments</h4>
                                        <div class="col-md-12 comment_scroll">
                                            <div class="modal-content">
                                                <div class="modal-body">
                                                    <span v-for="comment in comments.list" v-bind:key="comment.id">
                                                        <span v-if="comment.phototimor == $route.params.selected_id">
                                                            <b>{{ comment.user.fullname != "" ? comment.user.fullname : comment.user.username }} - <small>{{ $filters.formatDate(comment.sutmit_at) }}</small></b>
                                                            <p>{{ comment.comment }}</p>
                                                        </span>
                                                    </span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-md-12">
                                            <!-- Default form -->
                                            <div v-if="amILoggedIn === null">Detecting login...</div>
                                            <div v-if="add_comment.requesting === true">Detecting add Comment...</div>
                                            <div v-if="amILoggedIn === false">
                                                You must
                                                <a v-bind:href="loginUrl" >Login</a>
                                                to add a comment
                                            </div>
                                            <form @submit.prevent="submitNewComment" v-if="amILoggedIn === true">
                                                <span v-html="csrfTokenInput" />
                                                <span class="comment_input">
                                                    <input type="hidden" name="phototimor" :value="$route.params.selected_id">
                                                    <input type="text" name="comments" placeholder="Comments..."/>
                                                    <button type="submit" class="btn btn-primary">Save</button>
                                                </span>
                                            </form>
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
    height: 100%;
    width: 100%;
}
.modal-img {
   height: calc(88vh - 64px - 14px); 
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
    right: 20px;
    height: calc(77vh - 64px - 14px);
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
.expand-arrows {
    right: 0;
    bottom: 1em;
    background-color: hsla(0,0%,100%,.4);
    -webkit-backdrop-filter: blur(20px);
    backdrop-filter: blur(20px);
    border-radius: 5px;
    height: 32px;
    width: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>

<script>
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'
    import { mapGetters } from 'vuex'
    import 'viewerjs/dist/viewer.css'
    import { api as viewerApi } from "v-viewer"

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
            ...mapState(['images', 'comments', 'add_comment', 'amILoggedIn']),
            ...mapGetters(['csrfTokenInput']),
            loginUrl() {
                return `/en/accounts/login?next=${location.origin}/en/vue/#/photos/${this.$route.params.selected_id}`;
            }
        },
        methods: {
            ...mapActions(['requestImages', 'requestComment', 'submitNewComment', 'detectLogin']),
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
            this.requestComment();
            this.detectLogin();
        },
    }
</script>
