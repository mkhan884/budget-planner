<template>
 <div class="app">
    <div v-if="$route.path !== '/' && $route.path !== '/register'" class="sidebar-container">
      <Sidebar />
    </div>
    <div class="main-content">
      <RouterView />  
    </div>
 </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'

export default {
  name: 'App',
  components: {
    Sidebar  
  },
}
</script>

<style scoped>
.app{
  display: flex;
  height: 100vh;  
}

.main-content {
  flex: 1 ;
  align-content: center;
}
</style>
