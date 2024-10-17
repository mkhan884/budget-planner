<template>
  <div>
    <Sidebar />
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'

export default {
  name: 'App',
  components: {
    Sidebar,
  },
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
  #app {
    font-family: 'Montserrat', sans-serif !important;
  }
</style>
