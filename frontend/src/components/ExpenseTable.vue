<template>
  <table class="table table-sm custom-table">
    <!-- head -->
    <thead>
      <tr>
        <th>Date</th>
        <th>Amount</th>
        <th>Category</th>
        <th>Description</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr v-for="expense in expenses" :key="expense">
        <td>{{ expense.date }}</td>
        <td>{{ expense.amount }}</td>
        <td>{{ expense.category }}</td>
        <td>{{ expense.description }}</td>
        <td>{{ expense.notes }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'ExpenseTable',
  data() {
    return {
      expenses: [
        {
          amount: '2000',
          category: 'Transportation',
          description: 'Car Payment',
          date: '2024-11-10',
          notes: '',
        },
      ],
    }
  },
}
</script>

<style scoped>
.custom-table {
  width: fit-content;
}
</style>
