<template>
  <el-container v-if="active" direction="vertical">
    <el-row class="add-recipe">
      <el-link href="#/add-recipe"><el-button>Add new recipe</el-button></el-link>
    </el-row>

    <el-container class="recipe-list" v-loading="loading">
      <RecipeCard
        v-for="recipe in recipes"
        :key="recipe.id"
        :recipe="recipe"
        @expand-recipe="handleRecipeRedirect"
      />
      <div v-if="!recipes.length">You don't have recipes yet</div>
    </el-container>
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
      this.active = location.hash.match(/my-recipes$/);
    },
    async fetchRecipes() {
      try {
        this.loading = true;
        const { data: recipes } = await getRequest('/api/recipes/my-recipes/');

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
.add-recipe {
  justify-content: center;
  margin-top: 20px;
}
.recipe-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 20px;
  margin-top: 20px;
}
</style>
