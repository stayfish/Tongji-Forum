<template>
  <div class="common-layout min-h-screen">

    <el-row class="min-h-screen">
      <el-col :lg="8" :md='12' class="bg-light-50 center items-center justify-center">
        <div class="flex items-end justify-between">
          <h2 class="font-bold text-3xl text-gray-800">注册</h2>
          <el-text class="text-xs">
            已有账号？
            <el-link @click="changeRoute" type="primary" :underline="false" class="text-xs">登录</el-link>
          </el-text>
        </div>
        <div class="flex items-center justify-center my-5">
          <span class="h-[2px] w-60 bg-gray-200"></span>
        </div>
        <SignupForm></SignupForm>
      </el-col>
      <el-col :lg="16" :md="12" class="bg-sky-800 center items-center justify-center">
        <div class="font-bold text-5xl mb-4">
          Welcome
        </div>
        <div class="text-gray-200 text-sm">
          欢迎加入同济社区
        </div>
      </el-col>

    </el-row>

  </div>
</template>
  

<script setup>
// import { routerKey } from 'vue-router';
import { useRouter } from 'vue-router'
import SignupForm from './SignupForm.vue'
const router = useRouter();

const changeRoute = () => {
  router.push('/login')
}
</script>

<style scoped>
.center {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  display: -webkit-flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  -webkit-flex-direction: column;
  flex-direction: column;
}
</style>