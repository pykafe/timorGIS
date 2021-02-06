
<template>
    <div class="images_container">

        <div v-for="item in items" class="image_card">
            <img src="/media/photos/3AA92B55-4CE5-4D1B-A967-0A1D98FA45AB_FlsuDPE.jpeg" width="200">
        </div>
    </div>
    <div id="mapInset">

    </div>
</template>

<script>
    export default {
        data() {
            return {
                items: [
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                    { src:"", title:"", id:3},
                ]
            }
        },
    }
</script>