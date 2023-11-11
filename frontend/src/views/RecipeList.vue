<template>
  <div class="recipe-list" v-if="active">
    <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
  </div>
</template>

<script>
import recipes from '../assets/data/recipes.js';
import RecipeCard from '../components/RecipeCard.vue';

export default {
  data: () => ({
    recipes,
    active: false
  }),
  methods: {
    hashChangeHandler() {
      this.active = location.hash.match('recipes');
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
