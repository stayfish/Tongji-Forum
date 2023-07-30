<template>
    <div class="flex flex-col justify-start mt-16 w-full" style="align-items: center;">
        <div class="justify-center" style="width: 70vw;">
            <el-row>
                <el-card class="w-full margin">
                    <el-row>
                        <Profile :username="route.params.username" home="true" class="w-full"></Profile>
                    </el-row>
                </el-card>
            </el-row>
            <el-row>
                <el-col :sm="16" class="margin">

                    <el-card style="height: 50vh; overflow-y: scroll;">
                        <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
                            <el-tab-pane label="发文" name="first">
                                <div v-for="article in state.articles" :key="article.id">
                                    <Preview :article="article"></Preview>
                                </div>

                            </el-tab-pane>
                            <el-tab-pane label="收藏" name="second">
                                <div v-for="article in state.stars" :key="article.id">
                                    <Preview :article="article"></Preview>
                                </div>
                            </el-tab-pane>
                        </el-tabs>
                    </el-card>
                </el-col>
                <el-col :sm="8" class="margin">
                    <el-card header="社交" style="height: 50vh;">
                        <el-statistic @click="state.visible1 = (state.followed.length) != 0 ? true : false" :title="msg1"
                            :value="state.followed.length" />
                        <el-dialog v-model="state.visible1" :title="msg1" width="30%">
                            <div v-for="user in state.followed" :key="user.username" class="m-4">
                                <router-link :to="'/forum/homepage/' + user.username" class="text-base">
                                    {{ user.username }}
                                </router-link>
                            </div>
                        </el-dialog>
                        <el-statistic @click="state.visible2 = (state.followers.length) != 0 ? true : false" :title="msg2"
                            :value="state.followers.length" />
                        <el-dialog v-model="state.visible2" :title="msg2" width="30%">
                            <div v-for="user in state.followers" :key="user.username" class="m-4">
                                <router-link :to="'/forum/homepage/' + user.username" class="text-base">
                                    {{ user.username }}
                                </router-link>
                            </div>
                        </el-dialog>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted, reactive, watch } from 'vue';
import Profile from './profile.vue'
import Preview from '@/views/forum/topics/Preview.vue'
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
const route = useRoute()
import axios from '@/api'
const store = useStore()

const msg1 = computed(() => {
    return (store.state.user['username'] == route.params.username) ?
        '我的关注' : '他的关注'
})

const msg2 = computed(() => {
    return (store.state.user['username'] == route.params.username) ?
        '关注我的' : '关注他的'
})

const state = reactive({
    articles: [],
    stars: [],
    followers: [],
    followed: [],
    visible1: false,
    visible2: false,
    activeName: '发文'
})

async function loadFollowed() {
    try {
        let res = await axios.get(`/api/user/followed/${route.params.username}`)
        if (res.status == 200) {
            state.followed = res.data.users
        } else {
            console.log(res.status)
        }
    } catch (error) {
        console.log(error)
    }
}

async function loadFollower() {
    try {
        let res = await axios.get(`/api/user/follower/${route.params.username}`)
        if (res.status == 200) {
            state.followers = res.data.users
        } else {
            console.log(res.status)
        }
    } catch (error) {
        console.log(error)
    }
}

async function loadArticle() {
    try {
        let res = await axios.get(`/api/article/searchuser/${route.params.username}`)
        if (res.status == 200) {
            state.articles = res.data.articles
        } else {
            console.log(res.status)
        }
    } catch (error) {
        console.log(error)
    }
}

async function loadStars() {
    try {
        let res = await axios.get(`/api/article/star/${route.params.username}`)
        if (res.status == 200) {
            state.stars = res.data.stars
        } else {
            console.log(res.status)
        }
    } catch (error) {
        console.log(error)
    }
}
watch(() => route.params.username, async () => {
    location.reload()
})

loadArticle()
loadFollowed()
loadFollower()
loadStars()
</script>

<style scoped>
.default-margin {
    margin: 8px;
}
</style>