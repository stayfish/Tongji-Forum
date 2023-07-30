<template>
    <el-link @click="onclick" type="danger">
        退出登录
    </el-link>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()

const onclick = () => {
    Cookies.remove('token')
    Cookies.remove('username')
    router.push('/login')
}
</script>