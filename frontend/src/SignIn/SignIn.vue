<template>
  <el-container class="sign-in" v-if="active">
    <el-main class="content">
      <h2>Welcome to RecipeRec</h2>
      <el-form status-icon label-width="120px" class="user-info">
        <el-form-item label="Username" prop="username">
          <el-input placeholder="Username" />
        </el-form-item>
        <el-form-item label="Password" prop="pass">
          <el-input type="password" autocomplete="off" placeholder="Password" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" class="sign-in-btn">Sign In</el-button>
        </el-form-item>
      </el-form>
      <div class="additional">
        <span>Forgot password?</span>
        <el-link @click="openEmailModal">Enter email to reset</el-link>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import { ElMessage } from 'element-plus';
import { ElMessageBox } from 'element-plus';

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
      // this.active = location.hash.match('sign-in');
      this.active = true;
    },
    openEmailModal() {
      ElMessageBox.prompt('Please input your e-mail', {
        confirmButtonText: 'OK',
        cancelButtonText: 'Cancel',
        inputPattern:
          /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
        inputErrorMessage: 'Invalid Email'
      }).then(({ value }) => {
        ElMessage({
          type: 'success',
          message: `Your email is:${value}`
        });
      });
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
