<template>
  <el-row class="recipe-card" v-if="active">
    <el-col :span="18">
      <div class="ingredients">
        <h2>Ingredients</h2>
        <ul>
          <li v-for="ingredient in recipe.ingredients" :key="ingredient.name">
            {{ ingredient.name }}
          </li>
        </ul>
      </div>
      <div class="method">
        <h2>Description</h2>
        <p>{{ recipe.description }}</p>
        <h2>Instructions</h2>
        <p>{{ recipe.instructions }}</p>
      </div>
    </el-col>
    <el-col :span="2"></el-col>
    <el-col :span="4">
      <el-button type="primary" @click="addToFavorites" class="add-to-fav"
        >Add to favorites</el-button
      >
    </el-col>
  </el-row>
</template>

<script>
import { getRequest } from '../api.js';

export default {
  data: () => ({
    recipe: null,
    active: false
  }),
  methods: {
    hashChangeHandler() {
      const match = location.hash.match(/recipes\?id=(\d+)/);
      this.active = !!match;
      this.recipe = {};
      if (!this.active) return;
      const [, recipeId] = match;
      this.fetchRecipe(recipeId);
    },
    async fetchRecipe(id) {
      try {
        const { data: recipe } = await getRequest(`/api/recipes/${id}/`);

        this.recipe = recipe;
      } catch (err) {
        console.error(err);
      }
    }
  },
  watch: {
    recipe(recipe) {
      this.$emit('recipe-selected', recipe);
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  }
};
</script>

<style scoped>
.add-to-fav {
  margin-top: 20px;
}
</style>
