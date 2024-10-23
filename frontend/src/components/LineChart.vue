<template>
  <div class="card bg-base-100 h-full bordered">
    <div class="card-body">
      <div class="title text-secondary mb-4">
        <p class="font-semibold text-sm">Monthly Expenses</p>
      </div>
      <div class="chart-container h-full">
        <Line id="lineChartId" :options="chartOptions" :data="chartData" />
      </div>
    </div>
  </div>
</template>

<script>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
)

export default {
  name: 'LineChart',
  components: {
    Line,
  },
  data() {
    return {
      chartData: {
        labels: [
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December',
        ],
        datasets: [
          {
            label: 'Expenses',
            data: [
              800, 1150, 1300, 1200, 850, 900, 1000, 1100, 1350, 1250, 1300,
              1100,
            ], // Example expense data
            fill: false,
            borderColor: '#00ADB5',
            tension: 0.3, // Adds slight curve to the line
            pointRadius: 0,
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Amount', // Label for the y-axis
            },
          },
        },
        plugins: {
          legend: {
            display: false,
          },
          tooltip: {
            enabled: true, // Tooltips enabled by default
            mode: 'nearest', // Show tooltip when hovering near the line
            intersect: false, // Ensures tooltip shows when hovering over the line, not just at data points
          },
        },
      },
    }
  },
}
</script>
