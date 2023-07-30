<template>
    <el-container class="full flex flex-col">
        <el-menu class="full" default-active="1" mode="vertical" @open="handleOpen" @close="handleClose">
            <el-menu-item index="1" @click="router.push('/forum/index/')">
                <span>用户</span>
            </el-menu-item>
            <el-menu-item index="2">
                <span>文章</span>
            </el-menu-item>
        </el-menu>
    </el-container>
</template>
  
<script lang="ts" setup>
import { useRouter } from 'vue-router';
const router = useRouter()
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
</script>

<style scoped>
.full {
    height: 100%;
    width: 100%;
}
</style>
  