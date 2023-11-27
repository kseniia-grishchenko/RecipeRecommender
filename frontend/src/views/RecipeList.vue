<template>
  <div class="recipe-list" v-if="active">
    <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
  </div>
</template>

<script>
import { getRequest } from '../api.js';
import RecipeCard from '../components/RecipeCard.vue';

export default {
  data: () => ({
    recipes: [],
    active: false
  }),
  methods: {
    hashChangeHandler() {
      this.active = location.hash.match('recipes');
    },
    async fetchRecipes() {
      try {
        const { data: recipes } = await getRequest('/api/recipes/');

        this.recipes = recipes;
      } catch (err) {
        console.error(err);
      }
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
}
</style>
