<template>
    <nav class="navbar navbar_header navbar-expand-md navbar-light bg-light">
        <div class="container">
            <a href="" class="navbar-brand logo">
                <header-logo />
            </a>
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
                                    &nbsp;
                                </b>
                                <img src="../icons/people-circle.svg" class="rounded-circle" alt="{{ userName }}" width="25" height="25"> 
                                <span class="vertical-line"></span>
                            </template>

                            <header-settings-dropdown/>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
</template>
<style scoped>
    span.vertical-line {
        border-left: 1px solid #1b1a1838;
        margin-left: 6px;
        margin-right: 6px;
    }
</style>
<script>
    import HeaderLogo from './HeaderLogo.vue'
    import HeaderSettingsDropdown from './HeaderSettingsDropdown.vue'
    import { mapState } from 'vuex'
    import { mapActions } from 'vuex'

    export default {
        components: {
            HeaderLogo,
            HeaderSettingsDropdown
        },
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
