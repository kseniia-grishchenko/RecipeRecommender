<template>
  <div class="footer">
    <div class="logo">
      <el-icon><CoffeeCup /></el-icon>
      <span>RecipeRec</span>
    </div>
    <div class="nav-links">
      <el-link>Home</el-link>
      <el-link>Profile</el-link>
      <el-link>Catalog</el-link>
      <el-link>Favourites</el-link>
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
.footer {
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-links {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
}

.nav-links a:hover {
  color: #fff !important;
}
</style>
