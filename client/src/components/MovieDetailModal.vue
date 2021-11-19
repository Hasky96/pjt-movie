<template>
    <div>
        {{movie}}
        <button @click="$emit('end-modal')"></button>
    </div>
</template>
<script>
export default {
    name : 'MovieDetailModal',
    props: {
        movie : Object
    },

}
</script>
<style>
    
</style>