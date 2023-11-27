<template>
  <el-container class="sign-up" v-if="active">
    <el-main class="content">
      <h2>Welcome to RecipeRec</h2>
      <el-form status-icon label-width="120px" class="user-info">
        <el-form-item label="Username" prop="username">
          <el-input placeholder="Username" v-model="form.username" />
        </el-form-item>
        <el-form-item label="Password" prop="pass">
          <el-input
            type="password"
            autocomplete="off"
            placeholder="Password"
            v-model="form.password"
          />
        </el-form-item>
        <el-form-item label="Email" prop="email">
          <el-input type="email" placeholder="Email" v-model="form.email" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" class="sign-up-btn" @click="submitForm">Sign Up</el-button>
        </el-form-item>
      </el-form>
      <div class="additional">
        <span>Already have an account? </span>
        <el-link href="/#/sign-in">Sign in</el-link>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import { postRequestUnauthorized } from '../api.js';

export default {
  data: () => ({
    active: false,
    form: {
      email: '',
      username: '',
      password: ''
    }
  }),
  props: {
    loggedIn: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    async submitForm() {
      try {
        await postRequestUnauthorized('/api/auth/users/', {
          username: this.form.username,
          email: this.form.email,
          password: this.form.password
        });

        this.$notify({
          title: 'Success',
          message: 'Account created',
          type: 'success',
          showClose: false
        });
        location.hash = '#/sign-in';
      } catch (err) {
        this.$notify.error({
          title: 'Error occurred',
          message: JSON.stringify(err.response.data),
          showClose: false
        });
      }
    },
    hashChangeHandler() {
      this.active = location.hash.match('sign-up');
    }
  },
  created() {
    window.addEventListener('hashchange', this.hashChangeHandler);
    this.hashChangeHandler();
  }
};
</script>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

h2 {
  text-align: center;
  color: #888787;
}

.user-info {
  margin-top: 30px;
  width: 50%;
}

.sign-up-btn {
  width: 100%;
  background-color: var(--main-bg);
  border-color: var(--main-bg);
}

.additional {
  display: flex;
  gap: 4px;
  align-items: center;
}
</style>
