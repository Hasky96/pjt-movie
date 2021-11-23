<template>

<vue-carousel :data="datas" :controls="true"></vue-carousel>



</template>

<script>
export default {
  data() {
    return {
      datas: [
        '<div class="example-slide">Slide 1</div>',
        '<div class="example-slide">Slide 2</div>',
        '<div class="example-slide">Slide 3</div>',
      ],
    };
  },
};
</script>
