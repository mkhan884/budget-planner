<template>
    <div class="card bg-base-100 w-3/5 bordered">
        <div class="card-body">
            <div class="title text-secondary mb-4">
                <p class="font-semibold text-base">
                    Monthly Budget vs Actual Expenses
                </p>
            </div>
            <div class="chart-container">
                <Bar 
                    id="barChartId"
                    :options="chartOptions"
                    :data="chartData"
                />
            </div>
        </div>
    </div>
</template>

<script>
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
    name: "BarChart",
    components: {
        Bar
    },
    data () {
        return {
            chartData: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                datasets: [
                    {
                        barThickness: 14,
                        label: 'Budget',
                        data: [1000, 1200, 1100, 1300, 900, 950, 1100, 1200, 1400, 1300, 1250, 1150], // Example budget data
                        backgroundColor: '#393E46' // Budget color
                    },
                    {
                        barThickness: 14,
                        label: 'Actual Expenses',
                        data: [800, 1150, 1300, 1200, 850, 900, 1000, 1100, 1350, 1250, 1300, 1100], // Example actual expense data
                        backgroundColor: '#00ADB5' // Actual expense color
                    }
                ]
            },
            chartOptions: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        }
    }
}
</script>

<style>
.chart-container {
    height: 300px; /* Adjust height as needed */
}
</style>
