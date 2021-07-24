<template>
    <div class="card mb-3">
        <div class="card-body">
            <!-- Default form -->
            <form v-if="amILoggedIn === true"
                method="post" enctype="multipart/form-data" novalidate>
                <p class="h4 text-center mb-4">Add Journey History</p>
                <br/>
                <div class="form-group"> <!-- Title -->
                    <label class="control-label" for="title">Title</label>
                    <input class="form-control" id="title" name="title" placeholder="" type="text"/>
                </div>
                <div class="form-group"> <!-- Date input -->
                    <label class="control-label" for="date">Date</label>
                    <input class="from_date" placeholder="Select start date" type="text" name="from_date">
                    <input class="to_date" placeholder="Select end date" type="text" name="to_date">
                </div>
                <div class="form-group"> <!-- Description input -->
                    <label class="control-label" for="description">Description</label>
                    <textarea type="text" id="description" class="form-control" rows="3"></textarea>
                </div>
                <br/>
                <div class="row choose-files">
                    <div class="col">
                        <input type="file" name="photos" accept="image/.jpeg, .jpg" multiple>
                    </div>
                </div>
                <br/>
                <div class="text-center mt-4">
                    <button type="submit" class="btn btn-primary btn-pull-right">Save Journey</button>
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
    import { mapActions } from 'vuex'

    export default {
        computed: {
            ...mapState(['amILoggedIn']),
            loginUrl() {
                return `/en/accounts/login?next=${location.href}`;
            }
        },
        methods: {
            ...mapActions(['detectLogin']),
        },
        mounted() {
            this.detectLogin();
        },
    }
</script>