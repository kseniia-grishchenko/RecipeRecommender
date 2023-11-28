<template>
  <div class="recipe-card">
    <div class="image-container">
      <el-image :src="recipe.image" fit="contain">
        <template #error>
          <div class="image-slot">
            <img :src="defaultRecipeImage" />
          </div>
        </template>
      </el-image>
      <button class="favorite-button" @click="toggleFavorite">
        {{ isFavorite ? '❤️' : '🤍' }}
      </button>
    </div>
    <div class="content">
      <h2 class="title">{{ recipe.title }}</h2>
      <p class="description">{{ recipe.description }}</p>
      <button class="more-button" @click="$emit('expand-recipe', recipe.id)">More...</button>
    </div>
  </div>
</template>

<script>
import { getRequest, postRequest } from '../api.js';

export default {
  props: {
    recipe: {
      type: Object,
      required: true,
      default: () => ({
        image: '',
        title: 'Title',
        description: 'Description of the recipe'
      })
    }
  },
  data() {
    return {
      isFavorite: false
    };
  },
  async created() {
    try {
      const response = await getRequest('api/favorites/');
      const favoriteRecipeIds = response.data.map((fav) => fav.recipe);

      this.isFavorite = favoriteRecipeIds.includes(this.recipe.id);
    } catch (error) {
      console.error('Помилка при виконанні GET-запиту:', error);
    }
  },
  methods: {
    async toggleFavorite() {
      try {
        const response = await postRequest('api/favorites/', { recipe: this.recipe.id });

        if (response.status === 201) {
          this.$notify({
            title: 'Успішно',
            message: 'Рецепт додано до списку улюблених.',
            type: 'success'
          });
        } else if (response.status === 204) {
          this.$notify({
            title: 'Успішно',
            message: 'Рецепт видалено зі списку улюблених.',
            type: 'success'
          });
        } else {
          this.$notify({
            title: 'Помилка',
            message: 'Сталася помилка. Будь ласка, спробуйте ще раз.',
            type: 'error'
          });
        }

        this.isFavorite = response.status === 201;
      } catch (error) {
        console.error('Помилка при виконанні POST-запиту:', error);
        this.$notify({
          title: 'Помилка',
          message: 'Сталася помилка. Будь ласка, спробуйте ще раз.',
          type: 'error'
        });
      }
    }
  }
};
</script>
<style scoped>
.recipe-card {
  max-width: 300px;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  margin: 10px;
}

.image-container {
  position: relative;
}

.favorite-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  box-shadow: 1px 2px 2px rgba(0, 0, 0, 0.6);
  border-radius: 20px;
}

img {
  width: 100%;
  display: block;
}

.content {
  padding: 15px;
}

.title {
  font-size: 18px;
  margin: 0 0 10px 0;
}

.description {
  font-size: 14px;
  margin: 0 0 15px 0;
  color: #666;
}

.more-button {
  background-color: var(--main-bg);
  border: none;
  padding: 10px 20px;
  border-radius: 20px;
  cursor: pointer;
  font-weight: bold;
}
</style>
