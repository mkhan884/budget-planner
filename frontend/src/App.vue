<template>
  <div>
    <Sidebar  />
    <Summary />
    <IncomeTable />
    <ExpenseTable />
    <BudgetChart />
    <IncomeExpenseChart />
    
  </div>
</template>

<script>
import IncomeTable from './components/IncomeTable.vue'
import Sidebar from './components/Sidebar.vue'
import Summary from './components/Summary.vue'
import ExpenseTable from './components/ExpenseTable.vue';
import BudgetChart from './components/BudgetChart.vue';
import IncomeExpenseChart from './components/IncomeExpenseChart.vue';

export default {
  name: 'App',
  components: {
    Sidebar,
    Summary,
    IncomeTable,
    ExpenseTable,
    BudgetChart,
    IncomeExpenseChart
  },
}
</script>

<style></style>
