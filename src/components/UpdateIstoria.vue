<template>
    <div class="card mb-3">
        <div class="card-body">
            <h1>The form will update here</h1>
            <form @submit.prevent="getFormValues">
                <div class="form-group"> <!-- Title -->
                    <label class="control-label" for="title">Title</label>
                    <input class="form-control" id="title" name="title" placeholder="" type="text" required minlength="5" maxlength="80" />
                </div>
            </form>
        </div>
    </div>
</template>