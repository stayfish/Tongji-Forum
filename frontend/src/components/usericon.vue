<template>
    <div class="flex" style="align-items: center;">
        <el-avatar @click="jump" :icon="UserFilled" src="" />
        <div class="flex flex-col">
            <el-link @click="jump">
                {{ $store.state.user['username'] }}
            </el-link>
            <Logout />
        </div>
    </div>
</template>

<script setup>
import router from '../router';
// import Logout from '@/components/logout.vue'
import { UserFilled } from '@element-plus/icons-vue'

const jump = () => {
    router.push('/home')
}

</script>