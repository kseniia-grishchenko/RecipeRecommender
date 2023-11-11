<template>
  <el-container class="sign-up" v-if="active">
    <el-main class="content">
      <h2>Welcome to RecipeRec</h2>
      <el-form status-icon label-width="120px" class="user-info">
        <el-form-item label="Username" prop="username">
          <el-input placeholder="Username" />
        </el-form-item>
        <el-form-item label="Password" prop="pass">
          <el-input type="password" autocomplete="off" placeholder="Password" />
        </el-form-item>
        <el-form-item label="Email" prop="email">
          <el-input type="email" placeholder="Email" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" class="sign-up-btn">Sign Up</el-button>
        </el-form-item>
      </el-form>
      <div class="additional">
        <span>Already have an account? </span>
        <el-link href="/sign-up">Sign in</el-link>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data: () => ({
    active: false
  }),
  props: {
    loggedIn: {
      type: Boolean,
      default: false
    }
  },
  methods: {
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
