<template>
  <div class="dashboard-container bg-base-100">
    <div class="charts-container">
      <div class="income-expense-chart">
        <IncomeExpenseChart />
      </div>
      <div class="budget-chart">
        <BudgetChart />
      </div>
    </div>
    <div class="summary-line-container">
      <div class="summary-container">
        <Summary />
      </div>
      <div class="line-container">
        <LineChart />
      </div>
    </div>
  </div>
</template>

<script>
import IncomeExpenseChart from '@/components/IncomeExpenseChart.vue'
import BudgetChart from '@/components/BudgetChart.vue'
import Summary from '@/components/Summary.vue'
import LineChart from '@/components/LineChart.vue'

export default {
  name: 'Dashboard',
  components: {
    IncomeExpenseChart,
    BudgetChart,
    Summary,
    LineChart,
  },
}
</script>

<style scoped>
.charts-container {
  display: flex;
  height: 60vh;
}
.income-expense-chart {
  flex: 0 0 65%;
  padding: 20px 10px 10px 20px;
}
.budget-chart {
  flex: 0 1 35%;
  padding: 20px 20px 10px 10px;
}
.summary-line-container {
  display: flex;
  height: 40vh;
}
.summary-container {
  flex: 0 0 30%;
  padding: 20px 10px 20px 20px;
}
.line-container {
  flex: 1 1 70%;
  padding: 20px 20px 20px 10px;
}
</style>
