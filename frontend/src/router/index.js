import { createRouter, createWebHistory } from 'vue-router'
import Transactions from '@/views/Transactions.vue'
import Dashboard from '@/views/Dashboard.vue'
import Login from '@/views/Login.vue'
import Registration from '@/views/Registration.vue'

const routes = [
  { path: '/', component: Login},
  { path: '/register', component: Registration},
  { path: '/dashboard', component: Dashboard },
  { path: '/transactions', component: Transactions },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router 