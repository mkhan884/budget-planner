<template>
  <div class="card bg-base-100 bordered">
    <div class="card-body">
      <div class="title-and-button flex justify-between items-center mb-3">
        <div class="title text-secondary">
          <p class="font-semibold text-sm">Income</p>
        </div>
        <div class="text-accent text-sm font-semibold">
          <button>Add Income</button>
        </div>
      </div>
      <div class="table">
        <table class="table table-sm">
          <!-- head -->
          <thead>
            <tr>
              <th>ID</th>
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
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IncomeTable',
  data() {
    return {
      incomes: [
        {
          id: '#23',
          amount: '30000',
          source: 'Salary',
          date: '2024-11-10',
          notes: 'Salary from Virgin Mobile',
        },
        {
          id: '#24',
          amount: '7000',
          source: 'Rental Income',
          date: '2024-12-10',
          notes: 'Rental Income from the apartment',
        },
      ],
    }
  },
}
</script>
