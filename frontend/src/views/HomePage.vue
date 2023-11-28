<template>
  <el-container class="home-page" v-if="active" v-loading="loading">
    <h2>Most searched recipes</h2>
    <div class="recipe-list">
      <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
    </div>
    <el-button class="go-catalog"
      ><el-link href="#/recipes" class="go-link">Go to catalog</el-link>
    </el-button>
  </el-container>
</template>

<script>
import { getRequest } from '../api.js';
import RecipeCard from '../components/RecipeCard.vue';

export default {
  data: () => ({
    recipes: [],
    active: false,
    loading: false
  }),
  methods: {
    hashChangeHandler() {
      this.active = location.hash.match(/#\/$/);
    },
    async fetchMostSearched() {
      this.loading = true;
      const { data: popular } = await getRequest('/api/recipes/popular-recipes/');
      this.loading = false;

      this.recipes = popular
        .map(({ recipe }) => ({
          ...recipe,
          image: 'http://127.0.0.1:8000' + recipe.image
        }))
        .slice(0, 3);
    }
  },
  watch: {
    active(active) {
      if (!active) return;
      this.fetchMostSearched();
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  },
  components: {
    RecipeCard
  }
};
</script>

<style scoped>
.home-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
}
.recipe-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 20px;
}

.go-catalog {
  background-color: var(--main-bg);
  border: none;
  padding: 10px 20px;
  border-radius: 20px;
  cursor: pointer;
  font-weight: bold;
}

.go-link {
  color: #2c2b2b;
}
</style>
