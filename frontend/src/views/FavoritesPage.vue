<template>
  <el-container class="recipe-list" v-if="active" v-loading="loading">
    <RecipeCard
      v-for="recipe in recipes"
      :key="recipe.id"
      :recipe="recipe"
      @expand-recipe="handleRecipeRedirect"
    />
    <div v-if="!recipes.length">No favourites yet</div>
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
      this.active = location.hash.match(/favorites$/);
      console.log(this.active);
    },
    async fetchRecipes() {
      try {
        this.loading = true;
        const response = await getRequest('/api/favorites/list/');

        this.recipes = response.data.map((rec) => rec.recipe);
        console.log(this.recipes);
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
