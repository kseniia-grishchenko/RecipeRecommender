<template>
  <el-container v-if="active" class="add-recipe-container">
    <el-form status-icon label-width="120px" class="recipe-add" ref="authorizationForm">
      <el-form-item label="Title" prop="title">
        <el-input v-model="form.title" />
      </el-form-item>
      <el-form-item label="Description" prop="description">
        <el-input :rows="4" type="textarea" v-model="form.description" />
      </el-form-item>
      <el-form-item label="Ingredients" prop="ingredients">
        <el-input
          :rows="8"
          type="textarea"
          placeholder="Put each ingredient on new line"
          v-model="form.ingredients"
        />
      </el-form-item>
      <el-form-item label="Instructions" prop="instructions">
        <el-input :rows="10" type="textarea" v-model="form.instructions" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">Add recipe</el-button>
      </el-form-item>
    </el-form>
  </el-container>
</template>

<script>
import { postRequest } from '../api.js';

export default {
  data: () => ({
    active: false,
    form: {
      title: '',
      ingredients: '',
      description: '',
      instructions: ''
    }
  }),
  methods: {
    async submitForm() {
      try {
        console.log(this.form.ingredients.split('\n'));
        const { data: recipe } = await postRequest('/api/recipes/', {
          title: this.form.title,
          description: this.form.description,
          instructions: this.form.instructions,
          ingredients: this.form.ingredients.split('\n').map((name) => ({ name })),
          author: 0
        });
        console.log(recipe);

        this.$notify({
          title: 'Успішно',
          message: 'Recipe is added to the recipes list',
          type: 'success'
        });
        this.form = {
          title: '',
          ingredients: '',
          description: '',
          instructions: ''
        };
        location.hash = '#/my-recipes';
      } catch (err) {
        this.$notify.error({
          title: 'Error occurred while adding recipe',
          message: JSON.stringify(err.response.data),
          showClose: false
        });
      }
    },
    hashChangeHandler() {
      this.active = location.hash.match('add-recipe');
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  }
};
</script>

<style scoped>
.add-recipe-container {
  margin-top: 20px;
}
.recipe-add {
  width: 100%;
}
</style>
