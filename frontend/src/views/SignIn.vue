<template>
  <el-container class="sign-in" v-if="active">
    <el-main class="content">
      <h2>Welcome to RecipeRec</h2>
      <el-form status-icon label-width="120px" class="user-info" ref="authorizationForm">
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
        <el-form-item>
          <el-button type="primary" class="sign-in-btn" @click="submitForm">Sign In</el-button>
        </el-form-item>
      </el-form>
      <div class="additional">
        <span>Do not have an account yet? </span>
        <el-link href="/#/sign-up">Sign up</el-link>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import { postRequest } from '../api.js';

export default {
  data: () => ({
    active: false,
    form: {
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
        const {
          data: { access, refresh }
        } = await postRequest('/api/api/token/', {
          username: this.form.username,
          password: this.form.password
        });

        localStorage.setItem('access', access);
        localStorage.setItem('refresh', refresh);

        this.$emit('log-in');
      } catch (err) {
        this.$notify.error({
          title: 'Error occurred',
          message: JSON.stringify(err.response.data),
          showClose: false
        });
      }
    },
    hashChangeHandler() {
      this.active = location.hash.match('sign-in');
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

.sign-in-btn {
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
