<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <header-comp :loggedIn="loggedIn" @log-out="logOut"></header-comp>
      </el-header>
      <el-main>
        <auth-wrapper></auth-wrapper>
        <page-banner :title="selectedRecipe?.title"></page-banner>
        <sign-up v-if="!user"></sign-up>
        <sign-in v-if="!user" @log-in="handleLogIn"></sign-in>
        <home-page></home-page>
        <recipe-list></recipe-list>
        <recipe-page @recipe-selected="handleSelectedRecipe"></recipe-page>
      </el-main>
      <el-footer>
        <footer-comp></footer-comp>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import { jwtDecode } from 'jwt-decode';
import { getRequest, postRequest } from './api.js';

import SignIn from './views/SignIn.vue';
import SignUp from './views/SignUp.vue';
import FooterComp from './components/FooterComp.vue';
import HeaderComp from './components/HeaderComp.vue';
import RecipeList from './views/RecipeList.vue';
import HomePage from './views/HomePage.vue';
import PageBanner from './components/PageBanner.vue';
import AuthWrapper from './AuthWrapper.vue';
import RecipePage from './views/RecipePage.vue';

export default {
  data: () => ({
    loggedIn: false,
    selectedRecipe: null
  }),
  methods: {
    handleSelectedRecipe(recipe) {
      this.selectedRecipe = recipe;
    },
    async logIn() {
      const accessToken = localStorage.getItem('access');
      if (!accessToken) return;

      const { exp } = jwtDecode(accessToken);
      this.expiresAt = exp;

      if (this.expiresAt * 1e3 > Date.now()) {
        await this.fetchUser();
        return;
      }

      this.refreshToken();
    },

    async fetchUser() {
      try {
        const { data: user } = await getRequest('/api/auth/users/me/');

        this.user = user;
      } catch (err) {
        console.error(err);
      }
    },

    async refreshToken() {
      try {
        const { data } = await postRequest('/api/api/token/refresh/', {
          refresh: localStorage.getItem('refresh')
        });

        localStorage.setItem('access', data.access);
        this.logIn();
      } catch (err) {
        console.error(err.response.data);
      }
    },

    async handleLogIn() {
      await this.logIn();
      location.hash = '#/';
    },

    logOut() {
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');

      this.user = null;
      location.hash = '#/sign-in';
    }
  },
  created() {
    this.logIn();

    this.refresher = setInterval(() => {
      if (this.expiresAt && this.expiresAt * 1e3 > Date.now()) return;
      this.refreshToken();
    }, 60 * 1e3);

    const hashChangeHandler = () => {
      this.hash = location.hash;
    };
    window.addEventListener('hashchange', hashChangeHandler);
    hashChangeHandler();
  },
  components: {
    HeaderComp,
    SignUp,
    FooterComp,
    SignIn,
    RecipeList,
    HomePage,
    PageBanner,
    AuthWrapper,
    RecipePage
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

.el-loading-spinner .path {
  stroke: var(--main-bg);
}
</style>
