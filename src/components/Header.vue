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
                            <!--
                            <a href="{% url 'home' %}"  class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{% trans 'Settings' %}
                            </a>
                        
                            <ul class="dropdown-menu">
                                {% if user.is_authenticated %}
                                <a href="{% url 'password_change' %}">
                                    <li><img src="{% static 'icons/lock.svg' %}" alt="icon" width="25" height="25" title="Change password">{% trans 'Change password' %}</li>
                                </a>
                                <a href="{% url 'logout' %}">
                                    <li><img src="{% static 'icons/box-arrow-left.svg' %}" alt="icon" width="25" height="25" title="Logout">{% trans 'log out' %}</li>
                                </a>
                                {% else %}
                                <a href="{% url 'login' %}?next={{ request.path }}">
                                    <li><img src="{% static 'icons/power.svg' %}" alt="icon" width="25" height="25" title="Login">{% trans 'Log In' %}</li>
                                </a>
                                {% endif %}
                            </ul>
                            -->
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
