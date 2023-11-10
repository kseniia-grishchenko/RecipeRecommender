<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <header-comp :loggedIn="loggedIn"></header-comp>
      </el-header>
      <el-main>
        <div class="banner">
          <el-image src="default_banner.png"></el-image>
          <div class="shadow-layer"></div>
        </div>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>

<script>
import HeaderComp from './components/HeaderComp.vue';

export default {
  data: () => ({
    loggedIn: false
  }),
  components: {
    HeaderComp
  }
};
</script>

<style scoped>
.el-header {
  border-top: 12px solid var(--main-bg);
}

.banner-wrapper {
  background: rgba(0, 0, 0, 50%);
}
.banner {
  margin: 0 -20px;
  position: relative;
}
.shadow-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 50%);
}
</style>
