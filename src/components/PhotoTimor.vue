<template>
    <span class="loader" v-if="images.requesting">Loading...</span>
    <span class="loader" v-if="images.error">Sorry!</span>
    <div class="addjourney-mapicon">
        <router-link :to="{name: 'new_istoria'}">
            <a href="#" class="btn btn-primary add-new-journey">Add my journey</a>
        </router-link>
        <input class="form-control search-input-container" type="text" v-model="searchJourney" placeholder="Search journey">
        <router-link :to="{name: 'map'}">
            <a href="#">
                <img src="./icons/maps.svg" alt="maps" width="50" height="50">
            </a>
        </router-link>
    </div>
    <div class="images_container" v-if="images.list">
        <div 
            v-for="image in resultJourneyQuery" v-bind:key="image.id">
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
                                    <div class="modal-img">
                                        <img v-bind:src="selectedImageSrc" class="size_images rounded"/>
                                    </div>
                                    <div v-for="image in images.list" v-bind:key="image.id">
                                        <p class="posted-by" v-if="image.id == $route.params.selected_id">
                                            Posted by
                                            <b class="your-name">{{ image.istoria.creator.fullname !== "" ? image.istoria.creator.fullname: image.istoria.creator.username }}</b> in <small>{{ $filters.formatDate(image.istoria.created_at) }}</small>
                                        </p>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="modal-content">
                                        <div class="modal-body">
                                            <div class="comment-header">
                                                <h4 class="modal-title" id="gridSystemModalLabel">Comments ({{ commentsList.length }})</h4>
                                                <div v-if="amILoggedIn === null">Detecting login...</div>
                                                <div v-if="add_comment.requesting === true">Adding a comment . . .</div>
                                                <div v-if="amILoggedIn === false">
                                                    You must
                                                    <a v-bind:href="loginUrl" >Login</a>
                                                    to add a comment
                                                </div>
                                                <form @submit.prevent="submitNewComment" v-if="amILoggedIn === true">
                                                  <span v-html="csrfTokenInput" />
                                                   <span class="comment_input">
                                                      <input type="hidden" name="phototimor" :value="$route.params.selected_id">
                                                      <discord-picker input type="text" git-format="html" :value="value" @update:value="value = $event" name="comments" placeholder="Write a comment . . ."/>
                                                      <button type="submit" class="btn btn-primary button_submit">Submit</button>
                                                  </span>
                                                </form>
                                            </div>
                                            <div class="comment_scroll">
                                                <span v-if="comments.list">
                                                    <span v-for="comment in commentsList" v-bind:key="comment.id">
                                                        <b class="your-name">{{ comment.user.fullname != "" ? comment.user.fullname : comment.user.username }}</b> - <small>{{ $filters.formatDate(comment.sutmit_at) }}</small>
                                                        <p>{{ comment.comment }}</p>
                                                    </span>
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
        <p class="centered" v-if="resultJourneyQuery.length === 0">No results found for query "{{ searchJourney }}"</p>
    </div>
</template>
<style scoped>
    .search-input-container {
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
    .addjourney-mapicon {
        justify-content: space-between;
        display: flex;
        align-items: center;
        padding-top: 8px;
    }
    .images_container {
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
        object-position: center;
        object-fit: cover;
    }
    .modal-img {
        height: calc(88vh - 64px - 14px);
    }
    .comment-header {
        border-bottom: 1px solid rgba(0,0,0,.2);
        padding-bottom: 12px;
    }
    .comment_input {
        display: flex;
        width: 99%;
        position: relative;
        bottom: -0.5rem;
        white-space: nowrap;
    }
    .comment_input input {
        margin-right: 5px;
        border-radius: 0.25rem;
    }
    .comment_input button {
        padding: 9px;
    }
    .comment_scroll {
        padding-top: 12px;
        overflow-y: auto;
        min-height: 0;
        right: 20px;
        height: calc(77vh - 64px - 14px);
    }
    .your-name {
        text-transform: capitalize;
    }
    .posted-by {
        margin-top: 10px;
        margin-bottom: 10px;
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
    .button_submit {
        margin-top: 25px;
    }
</style>

<script>
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'
    import { mapGetters } from 'vuex'
    import 'viewerjs/dist/viewer.css'
    import { api as viewerApi } from "v-viewer"
    import DiscordPicker from 'vue3-discordpicker'

    export default {
        components: { DiscordPicker },
        props: [
            'url_media',
        ],
        data() {
            return {
                rollover_image_id: 0,
                selected_image_id: 0,
                value: '',
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
            selectedImage() {
                return this.images.list.find(image => image.id == this.$route.params.selected_id);
            },
            selectedImageSrc() {
                return this.selectedImage !== undefined
                    ? `${ this.url_media }${ this.selectedImage.image}`
                    : ""
            },
            commentsList(){
                return this.comments.list.filter(comment => comment.phototimor == this.$route.params.selected_id);
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
                if(image.image_thumbnail == ""){
                    return ""
                }else{
                    return `background-image: url(${ this.url_media }${ image.image_thumbnail})`;
                };
            },
            selectImgObject (image) {
                let img = [];
                const urlMedia = this.url_media;
                this.images.list.forEach((image) =>{
                    img.push(urlMedia + image.image)
                });
                const indexId = img.indexOf(urlMedia + image.image);
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
