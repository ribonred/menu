import Vue from 'vue'
import ExampleComponent from './component/template.vue';

Vue.component('example-component', ExampleComponent);

let vue = new Vue({
  //
}).$mount('#app')