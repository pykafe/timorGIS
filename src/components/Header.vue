<template>
    <nav class="navbar navbar_header navbar-expand-md navbar-light bg-light">
        <div class="container">
            <a href="" class="navbar-brand logo">Timor Journey</a>
            <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <div class="navbar-nav ml-auto">
                    <ul class="nav navbar-nav navbar-right">
                        <li class="dropdown">
                            <template v-if="amILoggedIn">
                                <b>
                                    Welcome 
                                    {{ userName }}
                                </b>
                                <span class="vertical-line"></span>
                            </template>

                            <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                                Settings
                            </a>
                            <ul class="dropdown-menu">
                                <template v-if="amILoggedIn">
                                    <a v-bind:href="url_changepassord">
                                        Change password {{ url_changepassord }}
                                    </a>
                                    <a href="{ url_logout_django }}">
                                        Log out
                                    </a>
                                </template>
                                <template v-if="!amILoggedIn">
                                    <a href="{{ url_login_django }}">
                                        Login
                                    </a>
                                </template>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        computed: {
            ...mapState(['amILoggedIn', 'userName']),
        },
        methods: {
            ...mapActions(['detectLogin']),
        },
        mounted() {
            this.detectLogin();
        },
    }
</script>
