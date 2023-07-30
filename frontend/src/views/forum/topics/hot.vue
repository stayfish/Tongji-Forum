<template>
    <el-card>
        <el-row>
            热门
        </el-row>
        <el-row v-for="(article, index) in state.articles" :key="article.id" class="flex-nowrap justify-between"
            @click="enter(article.id)">
            <el-text>{{ index + 1 }}</el-text>
            <el-text>{{ article.title }}</el-text>
            <el-text>{{ article.visits }}</el-text>
        </el-row>
    </el-card>
</template>

<script setup>
import { reactive } from 'vue';
import axios from '@/api'
import { useRouter } from 'vue-router';
const router = useRouter()

const state = reactive({
    articles: []
})

async function getHot(n) {
    try {
        let res = await axios.get(`/api/hot/${n}`)
        if (res.status == 200) {
            state.articles = res.data.articles
        }
        else {
            console.log(res.status)
        }
    }
    catch (error) {
        console.log(error)
    }
}
async function enter(id) {
    router.push(`/forum/index/article/${id}`)
}
getHot(5)
</script>