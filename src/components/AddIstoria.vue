<template>
    <span class="loader" v-if="add_istoria.requesting">Submitting please wait...</span>
    <span class="loader" v-if="add_istoria.error">Sorry!</span>
    <div class="card mb-3">
        <div class="card-body">
            <!-- Default form -->
            <form v-if="amILoggedIn === true" @submit.prevent="validateAndSubmitNewJourney" >
                <fieldset v-bind:disabled="add_istoria.requesting">
                    <span v-html="csrfTokenInput" />
                    <a href="#" type="button" class="btn btn-outline-info">Back</a>
                    <br/>
                    <div class="row">
                        <div class="col"> <!-- Title -->
                            <label class="control-label" for="title">Title</label>
                            <input class="form-control" id="title" name="title" placeholder="" type="text" required minlength="5" maxlength="80" />
                        </div>
                        <div class="col"> <!-- Image -->
                            <label class="control-label" for="file">Image</label>
                            <input type="file" name="photos" accept="image/.jpeg, .jpg" multiple>
                        </div>
                    </div>
                    <br/>
                    <div class="row">
                        <div class="col"> <!-- Description -->
                            <label class="control-label" for="description">Description</label>
                            <textarea type="text" id="description" name="description" class="form-control" rows="4"></textarea>
                        </div>
                        <div class="col"> <!-- Date input -->
                            <label class="control-label" for="fromDate">From </label>
                            <input type="date" class="fromDate" name="fromDate" select=":first" required="" v-model="fromDate" />
                            <br/>
                            <label class="control-label" for="toDate">To</label>
                            <input type="date" class="toDate" name="toDate" select=":last" required="" v-model="toDate" />
                            <p v-if="errors.length" style="color: red;">
                                <b>Please correct following this error:</b>
                                <ul>
                                    <li v-for="e in errors" v-bind:key="e.id">
                                        {{e}}
                                    </li>
                                </ul>
                            </p>
                        </div>
                    </div>
                    <br/>
                    <div class="form-row">
                        <div class="form-group col-md-12">
                            <button class="btn btn-primary btn-pull-right" >Save journey</button>
                            <a href="#" class="btn btn-default btn-pull-right">Cancel</a>
                        </div>
                    </div>
                </fieldset>
            </form>
        </div>
    </div>
        <!-- Default form -->
        <div v-if="amILoggedIn === null">Detecting login...</div>
        <div v-if="add_istoria.requesting === true">Detecting add Istoria...</div>
        <div v-if="amILoggedIn === false"> 
            You must
            <a v-bind:href="loginUrl" >Login</a> 
            to add a journey
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

<style scoped>
/* STYLING FOR INPUT ELEMENTS */

.white-theme textarea {
    height: 125px;
    border: 1px solid var(--blue-1);
    background: var(--white-2);
}

input[type=text]:focus, [type=email]:focus, [name=messages]:focus, textarea:not([type="submit"]):focus {
    z-index: 2;
    box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px var(--blue-2);
    border-radius: 2px;
    position: sticky;
}

input:not([type="submit"]), textarea:not([type="submit"]) {
    border-radius: 2px;
    border: 1px solid #31d9ff;
    background: #f0f2f5;
    color: #151313;
    width: 100%;
    padding: 11px;
    cursor: unset;
}

input[type="file"] {
    cursor: pointer;
}

/* BUTTONS STYLES */
/* This button using for "Add" and  "Cancel", This is only on gray theme*/
.btn-default {
    color: #fbf5f5;
}

.btn-default:hover {
    background-color: var(--white-1);
}

/* This button using for "Submit" form*/
.btn-primary {
    color: var(--white-1);
    background-color: var(--blue-2);
    border-radius: 15px;
}

.btn-primary:hover {
    background-color: var(--blue-1);
    border-color: var(--blue-2);
}

a.btn.btn-default.btn-pull-right {
    background-color: #f4a20dfa;
    border-radius: 10px;
}

label.control-label {
    margin: 5px;
}

a.btn.btn-outline-info {
    border-radius: 16px;
    color: black;
    margin-bottom: 30px;
    font-size: small;
}
</style>

<script>
    import { mapState } from 'vuex'
    import { mapGetters } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        data(){
            return {
                errors:[],
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
                this.errors=[];
                if(this.fromDate > this.toDate){
                    this.errors.push("End date must be greater than start date")
                }
                if( this.errors.length === 0 ) {
                    this.submitNewJourney(e);
	            }
            }
        },
        mounted() {
            this.detectLogin();
        },
    }
</script>
