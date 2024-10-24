<template>
  <div class="card">
    <div class="card-body">
      <div class="income-table-container pb-4">
        <IncomeTable />
      </div>
      <div class="expenese-table-container">
        <ExpenseTable />
      </div>
    </div>
  </div>
</template>

<script>
import ExpenseTable from '@/components/ExpenseTable.vue'
import IncomeTable from '@/components/IncomeTable.vue'
export default {
  name: 'Transactions',
  components: {
    IncomeTable,
    ExpenseTable,
  },
}
</script>
