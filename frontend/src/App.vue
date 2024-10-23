<template>
  <div>
    <!-- <Sidebar  />
    <Summary />
    <IncomeTable />
    <ExpenseTable />
    <BudgetChart />
    <IncomeExpenseChart /> -->
    <Dashboard />
    <!-- <LineChart /> -->
  </div>
</template>

<script>
import IncomeTable from './components/IncomeTable.vue'
import Sidebar from './components/Sidebar.vue'
import Summary from './components/Summary.vue'
import ExpenseTable from './components/ExpenseTable.vue'
import BudgetChart from './components/BudgetChart.vue'
import IncomeExpenseChart from './components/IncomeExpenseChart.vue'
import Dashboard from './views/Dashboard.vue'
import LineChart from './components/LineChart.vue'

export default {
  name: 'App',
  components: {
    Sidebar,
    Summary,
    IncomeTable,
    ExpenseTable,
    BudgetChart,
    IncomeExpenseChart,
    Dashboard,
    LineChart,
  },
}
</script>
