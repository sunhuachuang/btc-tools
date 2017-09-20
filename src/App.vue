<template>
  <div id="app">
    <div class="columns">
      <div class="column">
        <button class="button is-large">My Accounts</button>
      </div>
      <div class="column">
        <button class="button is-large">Lastest Translation</button>
      </div>
      <div class="column">
        <button class="button is-large">Translation Accounts</button>
      </div>
      <div class="column">
        <button class="button is-large">History</button>
      </div>
    </div>
      <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  text-align: center;
  margin-top: 15px;
}
</style>
