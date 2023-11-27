<template>
  <div class="recipe-card">
    <div class="image-container">
      <el-image :src="recipe.image" fit="contain">
        <template #error>
          <div class="image-slot">
            <img src="default_recipe.jpg" />
          </div>
        </template>
      </el-image>
      <button class="favorite-button">❤️</button>
    </div>
    <div class="content">
      <h2 class="title">{{ recipe.title }}</h2>
      <p class="description">{{ recipe.description }}</p>
      <button class="more-button" @click="$emit('expand-recipe', recipe.id)">More...</button>
    </div>
  </div>
</template>

<script>
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
