<template>
<div>
  <h1>{{ message }}</h1>
  <h2>{{ backend[0].email }}</h2>
  <button>change text</button>
</div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

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
    computed: mapState({
      products: state => state.products.all
    }),
    watch: {
      products (update, old) {
        
      }
    },
    methods: mapActions('cart', [
      'addProductToCart'
    ]),
    created () {
      this.$store.dispatch('products/getAllProducts')
    },
    mounted () {
    }
};
</script>