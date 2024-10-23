<template>
  <div class="summary">
    <div class="join pb-3">
      <input
        class="join-item btn custom-font-size"
        type="radio"
        name="options"
        aria-label="Monthly"
      />
      <input
        class="join-item btn custom-font-size"
        type="radio"
        name="options"
        aria-label="Yearly"
      />
      <input
        class="join-item btn custom-font-size"
        type="radio"
        name="options"
        aria-label="Weekly"
      />
    </div>
    <div class="income-expense">
      <div class="stats shadow">
        <div class="stat place-items-center">
          <div class="stat-title">Income</div>
          <div class="stat-value">31,000</div>
          <div class="stat-desc">From January 1st to February 1st</div>
        </div>

        <div class="stat place-items-center">
          <div class="stat-title">Expenses</div>
          <div class="stat-value text-secondary">4,200</div>
          <div class="stat-desc text-secondary">↗︎ 40 (2%)</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Summary',
}
</script>

<style scoped>
.custom-font-size {
  font-size: small; /* Adjust to desired size */
}

.summary {
    /* background-color: aqua; */
    width: fit-content;
}
</style>
