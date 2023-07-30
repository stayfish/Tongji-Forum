<template>
    <el-card class="article-card">
        <el-row style="margin-bottom: 8px;" @click="goback">
            <el-icon>
                <ArrowLeftBold />
            </el-icon>
        </el-row>
        <el-row justify="start" class="info font-light text-xs">
            <el-link @click="state.dialogVisible = true">
                <el-icon>
                    <UserFilled size="0.75rem" />
                </el-icon>
                <span class="text-xs font-light">
                    {{ state.username }}
                </span>
            </el-link>
            <el-dialog v-model="state.dialogVisible" title="用户信息" width="30%">
                <Profile :username="state.username"></Profile>
            </el-dialog>
        </el-row>
        <el-row justify="end">
            <time class="time text-xs font-light">{{ state.time }}</time>
        </el-row>
        <span class="text-lg font-medium">{{ state.title }}</span>
        <v-md-preview :text="state.content" height="400px"></v-md-preview>
        <el-row style="width: 75%">
            <el-col :span="8">
                <el-icon>
                    <ChatDotSquare />
                </el-icon>
                {{ state.replies.length }}
            </el-col>
            <el-col :span="8" @click="star">
                <el-icon>
                    <Star v-if="!state.alreadyStars" />
                    <StarFilled v-if="state.alreadyStars" color="#409EFF" />
                </el-icon>
                {{ state.stars }}
            </el-col>
            <el-col :span="8">
                <el-icon>
                    <View />
                </el-icon>
                {{ state.visits }}
            </el-col>
        </el-row>
        <el-row style="margin-bottom: 16px; margin-top: 8px;">
            <el-input v-model="state.myreply" :rows="2" type="textarea" placeholder="Please input" />
        </el-row>
        <el-row>
            <el-button type="primary" @click="reply">回复</el-button>
        </el-row>
        <el-divider></el-divider>
        <el-row justify="center">
            <el-empty v-if="state.replies.length == 0" description="暂时还没有评论~" />
            <div v-else class="comments" style="width: 100%">
                <span class="font-bold text-lg;">评论</span>
                <div class="flex flex-col align-middle">
                    <Reply v-for="reply in state.replies" :reply="reply" :key="reply.id"></Reply>
                </div>
            </div>
        </el-row>
    </el-card>
</template>


<script setup>
import { computed, onMounted, reactive, watch, ref } from 'vue';
import axios from '@/api'
import { useRoute, useRouter } from 'vue-router'
import {
    ChatDotSquare,
    Star,
    StarFilled,
    View,
    UserFilled,
    ArrowLeftBold
} from '@element-plus/icons-vue'
import Profile from '../profile/profile.vue'
import Reply from './Reply.vue'
import { useStore } from 'vuex'
const store = useStore()
const route = useRoute()
const router = useRouter()
const state = reactive({
    dialogVisible: false,
    id: '',
    title: '',
    content: '',
    time: '',
    username: '',
    visits: '',
    tag: '',
    stars: '',
    alreadyStars: false,
    replies: [],
    myreply: '',
})
const id = ref(route.params.id)
function goback() {
    router.push('/forum/index/display')
}
async function reply() {
    if (state.myreply.length == 0) {
        ElNotification({
            title: 'error',
            message: '评论不能为空',
            type: 'error'
        })
        return
    }
    try {
        let res = await axios.post('/api/reply/', {
            reply: state.myreply,
            aid: state.id,
        })
        if (res.status == 200) {
            ElNotification({
                title: 'Success',
                message: '回复成功',
                type: 'success'
            })
            state.replies = res.data.replies
            state.myreply = ''
        }
        else {
            console.log(res.status)
        }
    }
    catch (error) {
        console.log(error)
    }
}
async function loadArticle() {
    state.id = route.params.id
    try {
        let res = await axios.get(`/api/article/${state.id}`)
        if (res.status == 200) {
            console.log(res.data)
            const article = res.data.articles[0]
            console.log(article)
            state.title = article.title
            state.content = article.content
            state.time = article.time
            state.username = article.username
            state.visits = article.visits
            state.tag = article.tag
            state.stars = article.stars
            state.alreadyStars = article.alreadyStars
        } else {
            console.log(res.status)
        }
    }
    catch (error) {
        console.log(error)
    }
}
async function loadReplies() {
    try {
        let res = await axios.get(`/api/reply/${state.id}`)
        if (res.status == 200) {
            state.replies = res.data.replies
        }
        else {
            console.log(res.status)
        }
    }
    catch (error) {
        console.log(error)
    }
}
async function star() {
    const data = {
        username: store.state.user.username,
        id: state.id,
    }
    try {
        let res = await axios.post('/api/star/', data)
        if (res.status == 200) {
            state.stars = res.data.stars
            state.alreadyStars = res.data.alreadyStars
            const msg = state.alreadyStars ? '关注成功' : '取消关注'
            ElNotification({
                title: 'Success',
                message: msg,
                type: 'success'
            })
        }
        else {
            console.log(res.status)
        }
    }
    catch (error) {
        console.log(error)
    }
}
// onMounted(() => {
//     loadArticle()
//     loadReplies()
// })
watch(() => route.params.id, async (newId) => {
    location.reload()
})
loadArticle()
loadReplies()

</script>

<style scoped>
.article-card {
    margin: 8px;
}
</style>