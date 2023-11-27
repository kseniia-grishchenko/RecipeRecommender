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
      <el-button type="primary" @click="toggleFavorite" class="add-to-fav">
        {{ isFavorite ? 'Прибрати з улюбленого' : 'Додати до улюблених' }}
      </el-button>
    </el-col>
  </el-row>
</template>

<script>
import { getRequest, postRequest } from '../api.js';

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
        this.checkIfFavorite(id);
      } catch (err) {
        console.error(err);
      }
    },
    async checkIfFavorite(id) {
      try {
        const { data } = await getRequest(`/api/favorites/${id}/is_favorite/`);
        this.isFavorite = data.is_favorite;
      } catch (err) {
        console.error(err);
      }
    },
    async toggleFavorite() {
      try {
        const response = await postRequest('/api/favorites/', { recipe: this.recipe.id });
        if (response.status === 201) {
          this.isFavorite = true;
          this.$notify({
            title: 'Успішно',
            message: 'Рецепт додано до списку улюблених.',
            type: 'success'
          });
        } else if (response.status === 204) {
          this.isFavorite = false;
          this.$notify({
            title: 'Успішно',
            message: 'Рецепт видалено зі списку улюблених.',
            type: 'success'
          });
        }
      } catch (error) {
        console.error(error);
        this.$notify({
          title: 'Помилка',
          message: 'Сталася помилка. Будь ласка, спробуйте ще раз.',
          type: 'error'
        });
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
