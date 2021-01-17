import Vue from 'vue'
import ExampleComponent from './component/template.vue';
import store from './store'

Vue.component('example-component', ExampleComponent);

let vue = new Vue({
    el: '#app',
    store,
  //
}).$mount('#app')