<template>
    <div class="footer">
        <p align="center">
            Copyright <a href="http://pykafe.org" target="_blank">
            <LogoPyKafe></LogoPyKafe>
            </a> 
            {{ new Date().getFullYear() }}
        </p>
    </div>
</template>
<style scoped>

    p {
        margin-top:20px;
    }
    a:hover {
        text-decoration: none;
    }
    .footer {
        text-align: center;
        padding-bottom: 20px;
        padding-top: 20px;
        border-top: 1px solid #ffffff;
        margin: 75px;
        margin-bottom: 0px;
        line-height: 3;
    }
</style>
<script>
    import LogoPyKafe from './LogoPyKafe.vue';
    export default {
        components: {
            LogoPyKafe,
        }

    }
</script>