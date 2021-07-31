<template>
    <div class="card mb-3">
        <div class="card-body">
            <!-- Default form -->
            <form v-if="amILoggedIn === true" @submit.prevent="submitNewJourney" >
                <span v-html="csrfTokenInput" />
                <p class="h4 text-center mb-4">Add Journey History</p>
                <br/>
                <div class="form-group"> <!-- Title -->
                    <label class="control-label" for="title">Title</label>
                    <input class="form-control" id="title" name="title" placeholder="" type="text"  required minlength="5" maxlength="80" />
                </div>
                <div class="form-group"> <!-- Date input -->
                    <label for="fromDate">From </label>
                    <input type="date" class="fromDate" select=":first" required="" style="width: 400px; margin: 8px;" />
                    <label for="toDate">to</label>
                    <input type="date" class="toDate" select=":last" required="" style="width: 400px; margin: 8px;" />
                </div>
                <div class="form-group"> <!-- Description input -->
                    <label class="control-label" for="description">Description</label>
                    <textarea type="text" id="description" class="form-control" rows="3"></textarea>
                </div>
                <br/>
                <div class="form-group">
                    <input type="file" name="photos" style="width: 300px;" accept="image/.jpeg, .jpg" multiple>
                </div>
                <br/>
                <div class="text-center mt-4">
                    <button class="btn btn-primary btn-pull-right">Save Journey</button>
                    <a href="#" class="btn btn-default btn-pull-right">Cancel</a>
                </div>
            </form>
            <!-- Default form -->
            <div v-if="amILoggedIn === null">Detecting login...</div>
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
        computed: {
            ...mapState(['amILoggedIn']),
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