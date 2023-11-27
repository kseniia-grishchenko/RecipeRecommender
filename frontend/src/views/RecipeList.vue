<template>
  <el-container class="recipe-list" v-if="active" v-loading="loading">
    <RecipeCard
      v-for="recipe in recipes"
      :key="recipe.id"
      :recipe="recipe"
      @expand-recipe="handleRecipeRedirect"
    />
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
      this.active = location.hash.match(/recipes$/);
    },
    async fetchRecipes() {
      try {
        this.loading = true;
        const { data: recipes } = await getRequest('/api/recipes/');

        this.recipes = recipes;
        this.loading = false;
      } catch (err) {
        console.error(err);
      }
    },
    handleRecipeRedirect(recipeId) {
      location.hash = `#/recipes?id=${recipeId}`;
    }
  },
  watch: {
    active(active) {
      if (!active) return;
      this.fetchRecipes();
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
.recipe-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 20px;
  margin-top: 20px;
}
</style>
