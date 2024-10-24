<template>
  <div class="card bordered">
    <div class="card-body">
      <div class="title-and-button flex justify-between items-center mb-3">
        <div class="title text-secondary">
          <p class="font-semibold text-sm">Expense</p>
        </div>
        <div class="text-accent text-sm font-semibold">
          <button>Add Expense</button>
        </div>
      </div>

      <table class="table table-sm">
        <!-- head -->
        <thead>
          <tr>
            <th>ID</th>
            <th>Date</th>
            <th>Category</th>
            <th>Description</th>
            <th>Amount</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          <!-- row 1 -->
          <tr v-for="expense in expenses" :key="expense">
            <th>{{ expense.id }}</th>
            <td>{{ expense.date }}</td>

            <td>{{ expense.category }}</td>
            <td>{{ expense.description }}</td>
            <td>{{ expense.amount }}</td>
            <td>{{ expense.notes }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ExpenseTable',
  data() {
    return {
      expenses: [
        {
          id: '#457',
          amount: '2000',
          category: 'Transportation',
          description: 'Car Payment',
          date: '2024-11-10',
          notes: '',
        },
        {
          id: '#342',
          amount: '450',
          category: 'Food',
          description: 'Eat out - Pf Changs',
          date: '2024-12-10',
          notes: '',
        },
      ],
    }
  },
}
</script>
