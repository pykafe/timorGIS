<template>
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
</template>