<template>
  <div class="home-page" v-if="active">
    <h2>Most searched recipes</h2>
    <div class="recipe-list">
      <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
    </div>
    <el-button class="go-catalog"
      ><el-link href="#/recipes" class="go-link">Go to catalog</el-link>
    </el-button>
  </div>
</template>

<script>
import recipes from '../assets/data/recipes.js';
import RecipeCard from '../components/RecipeCard.vue';

export default {
  data: () => ({
    recipes: recipes.slice(0, 3),
    active: false
  }),
  methods: {
    hashChangeHandler() {
      this.active = location.hash.match(/#\/$/);
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
