<template>
    <div class="card mb-3">
        <div class="card-body">
            <!-- Default form -->
            <form v-if="amILoggedIn === true" @submit.prevent="validateAndSubmitNewJourney" >
                <fieldset v-bind:disabled="add_istoria.requesting">
                    <span v-html="csrfTokenInput" />
                    <a href="#" type="button" class="btn btn-outline-info">Back</a>
                    <br/>
                    <div class="row">
                        <div class="col">
                            <label class="control-label" for="title">Title</label>
                            <input class="form-control" id="title" name="title" placeholder="" type="text" required minlength="5" maxlength="80" />
                        </div>
                        <div class="col">
                            <label class="control-label" for="image">Image</label>
                            <input type="file" name="photos" accept="image/.jpeg, .jpg" multiple>
                        </div>
                    </div>
                    <br/>
                    <div class="row">
                        <div class="col"> <!-- Description input -->
                            <label class="control-label" for="description">Description</label>
                            <textarea type="text" id="description" name="description" class="form-control" rows="4"></textarea>
                        </div>
                        <div class="col"> <!-- Date input -->
                            <label for="fromDate">From </label>
                            <input type="date" class="fromDate" name="fromDate" select=":first" required="" v-model="fromDate" />
                            <br/>
                            <label for="toDate">To</label>
                            <input type="date" class="toDate" name="toDate" select=":last" required="" v-model="toDate" />
                            <p v-if="error.length" style="color: red;">
                                <b>Please correct following this error:</b>
                                <ul>
                                    <li v-for="e in error" v-bind:key="e.id">
                                        {{e}}
                                    </li>
                                </ul>
                            </p>
                        </div>
                    </div>
                    <br/>
                    <div class="text-center mt-4">
                        <button class="btn btn-primary btn-pull-right" >Save Journey</button>
                        <a href="#" class="btn btn-default btn-pull-right">Cancel</a>
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
    </div>
</template>

<script>
    import { mapState } from 'vuex'
    import { mapGetters } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        data(){
            return {
                error:[],
                fromDate: null,
                toDate: null
            }
        },
        computed: {
            ...mapState(['amILoggedIn', 'add_istoria']),
            ...mapGetters(['csrfTokenInput']),
            loginUrl() {
                return `/en/accounts/login?next=${location.href}`;
            }
        },
        methods: {
            ...mapActions(['detectLogin', 'submitNewJourney']),
            validateAndSubmitNewJourney(e){
                if(this.fromDate && this.toDate){
                    console.log("submit function called")
                }
                this.error=[];
                if(this.fromDate > this.toDate){
                    this.error.push("End date must be greater than start date")
                }
                if( this.error.length === 0 ) {
                    this.submitNewJourney(e);
	            }
            }
        },
        mounted() {
            this.detectLogin();
        },
    }
</script>