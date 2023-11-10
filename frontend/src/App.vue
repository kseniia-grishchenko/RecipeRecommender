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
        <sign-up></sign-up>
        <sign-in></sign-in>
      </el-main>
      <el-footer>
        <footer-comp></footer-comp>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import SignIn from './SignIn/SignIn.vue';
import SignUp from './SignUp/SignUp.vue';
import FooterComp from './components/FooterComp.vue';
import HeaderComp from './components/HeaderComp.vue';

export default {
  data: () => ({
    loggedIn: false
  }),
  components: {
    HeaderComp,
    SignUp,
    FooterComp,
    SignIn
  }
};
</script>

<style>
.el-header {
  border-top: 12px solid var(--main-bg);
}
.el-footer {
  height: auto;
  padding: 12px 20px;
  background-color: var(--main-bg);
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

.el-input__wrapper.is-focus {
  box-shadow: 0 0 0 1px var(--main-bg);
}
.el-link:hover {
  color: var(--main-bg);
}
.el-link.is-underline:hover:after {
  border-color: var(--main-bg);
}

.el-button:focus,
.el-button:hover {
  color: var(--main-bg);
  border-color: var(--main-bg);
  background-color: initial;
  outline: 0;
}
.el-button--primary {
  background-color: var(--main-bg);
  border-color: var(--main-bg);
}
</style>
