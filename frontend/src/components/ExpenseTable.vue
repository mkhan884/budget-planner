<template>
  <div class="card bordered bg-base-100">
    <div class="card-body">
      <div class="title-and-button flex justify-between items-center mb-3">
        <div class="title text-secondary">
          <p class="font-semibold text-sm">Expenses</p>
        </div>
        <div class="button">
          <button
            class="btn btn-secondary btn-sm"
            onclick="addExpense.showModal()"
          >
            Add Expense
          </button>
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

  <div class="form">
    <dialog id="addExpense" class="modal">
      <div class="modal-box w-1/3 max-w-5xl">
        <h3 class="text-lg font-bold mb-4">Add Expense</h3>
        <form>
          <!-- Amount input -->
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Amount</span>
            </label>
            <input
              type="number"
              placeholder="Enter amount"
              class="input input-bordered w-full"
              required
            />
          </div>

          <!-- Date input -->
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Date</span>
            </label>
            <input type="date" class="input input-bordered w-full" required />
          </div>

          <!-- Category input -->
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Category</span>
            </label>
            <input
              type="text"
              placeholder="Enter category"
              class="input input-bordered w-full"
              required
            />
          </div>

          <!-- Description input -->
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Description</span>
            </label>
            <input
              type="text"
              placeholder="Enter description"
              class="input input-bordered w-full"
            />
          </div>

          <!-- Submit and Close buttons -->
          <div class="modal-action">
            <button class="btn btn-primary">Save</button>
            <button
              class="btn btn-secondary"
              type="button"
              onclick="document.getElementById('addExpense').close()"
            >
              Close
            </button>
          </div>
        </form>
      </div>
    </dialog>
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
