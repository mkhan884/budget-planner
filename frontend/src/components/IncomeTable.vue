<template>
  <table class="table table-sm custom-table">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Amount</th>
        <th>Source</th>
        <th>Date</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr v-for="income in incomes" :key="income">
        <th>{{ income.id }}</th>
        <td>{{ income.amount }}</td>
        <td>{{ income.source }}</td>
        <td>{{ income.date }}</td>
        <td>{{ income.notes }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
    name: 'IncomeTable',
    data(){
        return {
            incomes: [
                {
                    "id": '#23',
                    "amount": "30000",
                    "source": "Salary",
                    "date": "2024-11-10",
                    "notes": "Salary from Virgin Mobile"
                }
            ]
        }
    }
}
</script>

<style scoped>
    .custom-table {
        width: fit-content;
    }
</style>