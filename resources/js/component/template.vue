<template>
<div>
  <h1>{{ message }}</h1>
  <h2>{{ backend[0].email }}</h2>
  
</div>
</template>

<script>
export default {
    props: {

    mess: {
      type: String,
    },

  },
  data() {
    return {
      message: "Welcome to Vue!",
      backend: JSON.parse(this.mess)
    };
  },
  mounted() {
    
  }
};
</script>