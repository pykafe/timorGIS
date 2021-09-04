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
</style>
<script>
    import LogoPyKafe from './LogoPyKafe.vue';
    export default {
        components: {
            LogoPyKafe,
        }

    }
</script>