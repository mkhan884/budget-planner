<template>
  <div class="card bg-base-100 h-full bordered">
    <div class="card-body">
      <div class="title-and-button flex justify-between items-center mb-3">
        <div class="title text-secondary">
          <p class="font-semibold text-sm">Monthly Budget</p>
          <p class="text-secondary text-xs italic">Total: $1000</p>
        </div>
        <div class="text-accent text-sm font-semibold">
          <button>Manage Budget</button>
        </div>
      </div>
      <div class="chart-container h-4/5">
        <Doughnut id="chartId" :options="chartOptions" :data="chartData" />
      </div>
    </div>
  </div>
</template>

<script>
import { Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale)

export default {
  name: 'BudgetChart',
  components: {
    Doughnut,
  },
  data() {
    return {
      chartData: {
        labels: [
          'Transportation',
          'Food',
          'Utilities',
          'Subscriptions',
          'Misc.',
        ],
        datasets: [
          {
            data: [2000, 3000, 1000, 150, 600],
            backgroundColor: [
              '#FF6384', // Color for 'Transportation'
              '#36A2EB', // Color for 'Food'
              '#FFCE56', // Color for 'Utilities'
              '#4BC0C0', // Color for 'Subscriptions'
              '#9966FF', // Color for 'Misc.'
            ],
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              usePointStyle: true,
            },
          },
        },
      },
    }
  },
}
</script>

<style></style>
