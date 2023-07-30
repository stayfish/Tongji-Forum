<template>
    <el-row class="preview">
        <el-card @click="enter" :body-style="{ padding: '0px' }" shadow="hover" style="width: 100%">
            <div style="padding: 14px">
                <el-row justify="start" class="info font-light text-xs">
                    <el-link @click="state.dialogVisible = true">
                        <el-icon>
                            <UserFilled size="0.75rem" />
                        </el-icon>
                        <span class="text-xs font-light">
                            {{ props.article.username }}
                        </span>
                    </el-link>
                    <el-dialog v-model="state.dialogVisible" title="用户信息" width="30%">
                        <Profile :username="props.article.username"></Profile>
                    </el-dialog>
                </el-row>
                <el-row justify="end">
                    <time class="time text-xs font-light">{{ props.article.time }}</time>
                </el-row>
                <span class="text-lg font-medium">{{ props.article.title }}</span>
                <div class="bottom">
                    <span class="text-sm">{{ content }}</span>
                    <el-divider></el-divider>
                    <el-row style="width: 75%">
                        <el-col :span="8">
                            <el-icon>
                                <ChatDotSquare />
                            </el-icon>
                            {{ props.article.replies }}
                        </el-col>
                        <el-col :span="8">
                            <el-icon>
                                <Star v-if="!props.article.alreadyStars" />
                                <StarFilled v-if="props.article.alreadyStars" color="#409EFF" />
                            </el-icon>
                            {{ props.article.stars }}
                        </el-col>
                        <el-col :span="8">
                            <el-icon>
                                <View />
                            </el-icon>
                            {{ props.article.visits }}
                        </el-col>
                    </el-row>
                </div>
            </div>
        </el-card>
    </el-row>
</template>

<script setup>
import { computed, reactive } from 'vue';
import {
    ChatDotSquare,
    Star,
    StarFilled,
    View,
    UserFilled
} from '@element-plus/icons-vue'
import { useRouter } from 'vue-router';
import Profile from '../profile/profile.vue'
const router = useRouter()
const state = reactive({
    dialogVisible: false,
})


const props = defineProps(['article'])
const content = computed(() => {
    if (props.article.content.length > 20)
        return props.article.content.slice(0, 20) + '...'
    return props.article.content
})
async function enter() {
    console.log("id: ", props.article.id)
    router.push(`/forum/index/article/${props.article.id}`)
}
</script>

<style scoped>
.preview {
    /* margin-top: 8px; */
    /* margin-bottom: 8px; */
    margin: 8px;
}
</style>