<template>
  <div class="header">
    <div class="logo">
      <el-icon><CoffeeCup /></el-icon>
      <span>RecipeRec</span>
    </div>
    <div class="sections">
      <el-link href="#/">Home</el-link>
      <el-link href="#/recipes">Recipes</el-link>
      <el-link href="#/profile">Profile</el-link>
    </div>
    <div class="action-section">
      <el-icon v-if="loggedIn"><Star /></el-icon>
      <el-input
        v-model="input2"
        class="search-bar"
        size="medium"
        placeholder="Search..."
        :prefix-icon="Search"
      />
      <el-button @click="$emit('log-out')">Log out</el-button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    loggedIn: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style scoped>
.header {
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  padding-top: 10px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-right: 30px;
}

.sections {
  display: flex;
  gap: 20px;
}

.action-section {
  align-self: flex-end;
  display: flex;
  align-items: center;
  justify-content: end;
  gap: 6px;
}

.search-bar {
  width: 200px;
}
</style>
