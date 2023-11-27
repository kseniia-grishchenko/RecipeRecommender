<template>
  <div class="banner">
    <el-image :src="imageUrl"></el-image>
    <div class="shadow-layer">
      <span class="banner-title">{{ title || defaultTitle }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    defaultTitle:
      'Unlock the flavors and unleash your culinary creativity with our exquisite recipe collection!'
  }),
  props: {
    imageUrl: {
      type: String,
      default: 'default_banner.png'
    },
    title: {
      type: String
    }
  }
};
</script>

<style scoped>
.banner {
  margin: 0 -20px;
  position: relative;
}
.shadow-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 50%);
  display: flex;
  align-items: center;
  justify-content: center;
}
.banner-title {
  color: #fff;
  font-size: 24px;
  font-weight: 700;
}
</style>
