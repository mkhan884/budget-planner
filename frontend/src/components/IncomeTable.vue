<template>
  <div class="card bg-base-100 bordered">
    <div class="card-body">
      <div class="title-and-button flex justify-between items-center mb-3">
        <div class="title text-secondary">
          <p class="font-semibold text-sm">Income</p>
        </div>
        <div class="text-accent text-sm font-semibold">
          <button
            class="btn btn-secondary btn-sm"
            onclick="addModal.showModal()"
          >
            Add Income
          </button>
        </div>
      </div>
      <div class="table">
        <table class="table table-sm">
          <!-- head -->
          <thead>
            <tr>
              <th>ID</th>
              <th>Source</th>
              <th>Date</th>
              <th>Amount</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            <!-- row 1 -->
            <tr v-for="income in incomes" :key="income">
              <th>{{ income.id }}</th>
              <td>{{ income.source }}</td>
              <td>{{ income.date }}</td>
              <td>{{ income.amount }}</td>
              <td>{{ income.notes }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="form">
    <dialog id="addModal" class="modal">
      <div class="modal-box w-1/3 max-w-5xl">
        <h3 class="text-lg font-bold mb-4">Add Income</h3>
        <form>
          <!-- Source input -->
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Source</span>
            </label>
            <input
              type="text"
              placeholder="Enter income source"
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

          <!-- Notes input -->
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Notes</span>
            </label>
            <textarea
              placeholder="Enter additional notes"
              class="textarea textarea-bordered w-full"
            ></textarea>
          </div>

          <!-- Submit button -->
          <div class="modal-action">
            <button class="btn btn-primary">Save</button>
            <button
              class="btn btn-secondary"
              type="button"
              onclick="document.getElementById('addModal').close()"
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
  name: 'IncomeTable',
  data() {
    return {
      showForm: false,
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
