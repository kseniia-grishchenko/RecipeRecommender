<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <header-comp></header-comp>
      </el-header>
      <el-main>Main</el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>

<script setup>
import HeaderComp from './components/HeaderComp.vue';
</script>

<style scoped>
.el-header {
  border-top: 12px solid var(--main-bg);
}
</style>
