<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <header-comp :loggedIn="loggedIn"></header-comp>
      </el-header>
      <el-main>
        <page-banner></page-banner>
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
import SignIn from './views/SignIn.vue';
import SignUp from './views/SignUp.vue';
import FooterComp from './components/FooterComp.vue';
import HeaderComp from './components/HeaderComp.vue';
import PageBanner from './components/PageBanner.vue';

export default {
  data: () => ({
    loggedIn: false
  }),
  components: {
    HeaderComp,
    SignUp,
    FooterComp,
    PageBanner
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
