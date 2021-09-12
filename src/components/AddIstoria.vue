<template>
    <span class="loader" v-if="add_istoria.requesting">Submitting please wait...</span>
    <div class="container">
        <span class="loader" v-if="add_istoria.error">Sorry!</span>
        <div class="row">
            <div class="col-md-12 back-button">
                <a href="#" class="btn btn-default">Back</a>
            </div>
        </div>
        <!-- Default form -->
        <form v-if="amILoggedIn === true" @submit.prevent="submitNewJourney" >
            <fieldset v-bind:disabled="add_istoria.requesting">
                <span v-html="csrfTokenInput" />
                <div class="form-row">
                    <div class="form-group col-md-6"> <!-- Title -->
                        <label class="control-label" for="title">Title</label>
                        <input class="form-control" id="title" name="title" placeholder="" type="text" required minlength="5" maxlength="80" />
                    </div>
                    <div class="form-group col-md-6"> <!-- Image -->
                        <label class="control-label" for="file">Image</label>
                        <input type="file" name="photos" accept="image/.jpeg, .jpg" multiple>
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group col-md-6"> <!-- Description -->
                        <label class="control-label" for="description">Description</label>
                        <textarea type="text" id="description" name="description" class="form-control" rows="3"></textarea>
                    </div>
                    <div class="form-group col-md-6"> <!-- Date input -->
                        <label class="control-label" for="duration">Duration of trip</label>
                        <input type="date" class="fromDate" name="fromDate" select=":first" required="" />
                        <input type="date" class="toDate" name="toDate" select=":last" required=""/>
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group col-md-12"> <!-- Description input -->
                        <button class="btn btn-primary btn-pull-right" >Submit</button>
                        <a href="#" class="btn btn-default btn-pull-right">Clear</a>
                    </div>
                </div>
            </fieldset>
        </form>
        <!-- Default form -->
        <div v-if="amILoggedIn === null">Detecting login...</div>
        <div v-if="add_istoria.requesting === true">Detecting add Istoria...</div>
        <div v-if="amILoggedIn === false">
            You must
            <a v-bind:href="loginUrl" >Login</a>
            to add a journey
        </div>
    </div>
</template>
<style scoped>
    input.fromDate, input.toDate {
        margin: 2px;
    }

    input#title {
        padding: 24px;
    }

    .back-button {
        padding-top: 15px;
        padding-bottom: 15px;
    }
    .loader {
        background-color: rgb(8 8 8 / 87%);
        position: absolute;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        text-align: center;
        top: 0px;
        width: 100%;
        height: 100%;
        z-index: 401;
        color: var(--white);
        font-size: 32px;
    }
</style>

<script>
    import { mapState } from 'vuex'
    import { mapGetters } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        computed: {
            ...mapState(['amILoggedIn', 'add_istoria']),
            ...mapGetters(['csrfTokenInput']),
            loginUrl() {
                return `/en/accounts/login?next=${location.href}`;
            }
        },
        methods: {
            ...mapActions(['detectLogin', 'submitNewJourney']),
        },
        mounted() {
            this.detectLogin();
        },
    }
</script>
