<template>
  <div class="flex-col justify-center items-center">
    <el-form ref="formRef" :model="form" status-icon :rules="rules"
      class="flex flex-col items-center justify-center w-50">
      <el-form-item prop="username">
        <el-input v-model="form.username" autocomplete='off' placeholder="请输入用户名" />
      </el-form-item>
      <el-form-item prop="name">
        <el-input v-model="form.name" autocomplete='off' placeholder="请输入姓名" />
      </el-form-item>
      <el-form-item prop="email">
        <el-input v-model="form.email" autocomplete='off' placeholder="请输入邮箱" />
      </el-form-item>
      <el-form-item prop="password">
        <el-input v-model="form.password" type='password' autocomplete='off' placeholder="请输入密码" show-password />
      </el-form-item>
      <el-form-item prop="confirm">
        <el-input v-model="form.confirm" type='password' autocomplete='off' placeholder="确认密码" show-password />
      </el-form-item>
      <el-form-item>
        <el-button round type="primary" @click="onSubmit(formRef)" class="bg-sky-800 w-50">注 册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router'
import axios from '@/api'
const router = useRouter();
const checkConfirm = (rule, value, callback) => {
  if (value !== form.password)
    callback(new Error('两次输入密码需要相同'))
  else
    callback()
}
const rules = reactive({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
  ],
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
  ],
  confirm: [
    { required: true, message: '请重复密码', trigger: 'blur' },
    { validator: checkConfirm, trigger: 'blur' }
  ],
})
const formRef = ref();
const form = reactive({
  username: '',
  name: '',
  password: '',
  confirm: '',
  email: '',
})

const onSubmit = (formRef) => {
  formRef.validate(async valid => {
    if (valid) {
      let type = ''
      let msg = ''
      try {
        let res = await axios.post(`api/user/${form.username}`, form)
        if (res.status === 200) {
          router.push('/login')
          type = 'success'
          msg = '注册成功'
        }
        else
          console.log(response.status)
      }
      catch (error) {
        console.log(error)
        type = 'error'
        msg = '用户名已存在'
      }
      ElNotification({
        title: type,
        message: msg,
        type: type
      })
    } else {
      ElNotification({
        title: 'Failure',
        message: '注册失败',
        type: 'error'
      })
    }
  })

}
</script>