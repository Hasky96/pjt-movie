<template>
    <div style="border: 5px solid black;">
        {{movie}}
        <button @click="endModal">exit</button>
    </div>
</template>
<script>
export default {
    name : 'MovieDetailModal',
    props: {
        movie : Object
    },
    methods:{
        endModal(){
            this.$emit('end-modal')
        }
    }
}
</script>
<style>
    
</style>