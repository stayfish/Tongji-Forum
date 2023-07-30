<template>
  <el-row class="min-h-screen">
    <el-col :lg="16" :md="12" class="bg-sky-800 center items-center justify-center">
      <div class="font-bold text-5xl mb-4">
        Welcome
      </div>
      <div class="text-gray-200 text-sm">
        同济社区是一个智能化社区，在这里分享你的瞬间
      </div>
    </el-col>
    <el-col :lg="8" :md='12' class="bg-light-50 center items-center justify-center">
      <div class="flex items-end justify-between">
        <h2 class="font-bold text-3xl text-gray-800">欢迎回来</h2>
        <el-text class="text-xs">
          没有账号？
          <el-link @click="changeRoute" type="primary" :underline="false" class="text-xs">注册</el-link>
        </el-text>
      </div>
      <div class="flex items-center justify-center my-5">
        <span class="h-[2px] w-60 bg-gray-200"></span>
      </div>
      <el-form ref="formRef" :model="form" :rules="rules" class="flex flex-col items-center justify-center w-50">
        <el-form-item prop="entry">
          <el-input v-model="form.entry" autocomplete='off' placeholder="请输入账号" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="form.password" type='password' autocomplete='off' placeholder="请输入密码" show-password />
        </el-form-item>
        <el-form-item>
          <el-button round type="primary" @click="onSubmit(formRef)" class="bg-sky-800 w-50">登 录</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>

<script setup>
import { ref, reactive } from 'vue'
import axios from '@/api'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
// import Cookies from 'js-cookie'

const store = useStore()
const router = useRouter();
const formRef = ref();
const form = reactive({
  entry: '',
  password: '',
})

const rules = reactive({
  entry: [
    { required: true, message: '请输入账号', trigger: 'blur' },
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
  ]
})


const onSubmit = (formRef) => {
  console.log(import.meta.env)
  console.log(axios.defaults.baseURL)
  // 校验
  formRef.validate(async valid => {
    if (valid) {
      // 发送请求
      try {
        let res = await axios.post('api/user/', form);
        if (res.status === 200) {
          ElNotification({
            title: 'Success',
            message: '登录成功',
            type: 'success'
          })
          const username = form['entry']
          store.commit('set_userinfo', {
            username: username,
            level: res.data['level']
          })
          Cookies.set('token', res.data.token, { expires: 1 })
          Cookies.set('username', username, { expires: 1 })
          Cookies.set('level', res.data['level'], { expires: 1 })
          router.push('/forum/index')
        }
        else
          console.log(res.status)
      } catch (error) {
        ElNotification({
          title: 'Failure',
          message: '登录失败',
          type: 'error'
        })
      }

    }

    else {
      ElNotification({
        title: 'Failure',
        message: '请输入正确的格式',
        type: 'error'
      })
    }
    // 跳转页面
  })
}

const changeRoute = () => {
  router.push('/signup')
}
</script>

<style scoped>
/* .el-row {
  margin-bottom: 20px;
} */
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