<template>
    <el-card class="reply">
        <el-row justify="start" class="info font-light text-xs">
            <el-link @click="state.dialogVisible = true">
                <el-icon>
                    <UserFilled size="0.75rem" />
                </el-icon>
                <span class="text-xs font-light">
                    {{ props.reply.username }}
                </span>
            </el-link>
            <el-dialog v-model="state.dialogVisible" title="用户信息" width="30%">
                <Profile :username="props.reply.username"></Profile>
            </el-dialog>
        </el-row>
        <el-row justify="end">
            <time class="time text-xs font-light">{{ props.reply.time }}</time>
        </el-row>
        <span class="text-lg font-medium">{{ props.reply.content }}</span>

    </el-card>
</template>

<script setup>
import {
    UserFilled,
} from '@element-plus/icons-vue'
import { reactive } from 'vue';
import Profile from './Preview.vue'
const props = defineProps(['reply'])
const state = reactive({
    dialogVisible: false
})
</script>

<style scoped>
.reply {
    margin: 8px;
}
</style>